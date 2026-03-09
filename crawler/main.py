import os
import sys
import time
import json
import yaml
import subprocess
from bs4 import BeautifulSoup
from transformers.md_transformer import MarkdownTransformer
from transformers.metadata_extractor import MetadataExtractor
from transformers.contributor_extractor import ContributorExtractor
from intelligence.orchestrator import IntelligenceOrchestrator
from intelligence.llm_router import LLMRouter
from automation.github_issue_creator import GithubIssueCreator
from automation.report_generator import JekyllReportGenerator

class Orchestrator:
    def __init__(self):
        self.repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.crawler_dir = os.path.join(self.repo_root, "crawler")
        self.downloads_dir = os.path.join(self.crawler_dir, "downloads")
        self.sync_state_file = os.path.join(self.crawler_dir, "content", "sync_state.json")
        self.quality_issues_file = os.path.join(self.crawler_dir, "content", "quality_issues.json")
        self.content_docs_dir = os.path.join(self.repo_root, "content", "docs")

        self.llm = LLMRouter()
        self.transformer = MarkdownTransformer(self.llm)
        self.extractor = MetadataExtractor(self.llm)
        self.contributors = ContributorExtractor()
        self.intel = IntelligenceOrchestrator()
        self.issue_creator = GithubIssueCreator()
        self.report_gen = JekyllReportGenerator()

    def check_cooldown(self, cooldown_hours=4):
        state_file = self.sync_state_file
        if os.path.exists(state_file):
            mtime = os.path.getmtime(state_file)
            elapsed = (time.time() - mtime) / 3600
            if elapsed < cooldown_hours:
                print(f"Cooldown active. Last sync was {elapsed:.1f} hours ago. (Limit: {cooldown_hours}h)")
                return False
        return True

    def run_crawl(self):
        print("Starting batch crawl (limit 20 pages)...")
        subprocess.run(
            [sys.executable, "-m", "scrapy", "crawl", "documentation"],
            cwd=self.crawler_dir,
            check=False,
        )

    def run_sync(self):
        print("Syncing: Transforming downloaded HTML into Markdown...")
        downloads_dir = self.downloads_dir
        if not os.path.exists(downloads_dir):
            print("No downloads found.")
            return

        # Keep this report scoped to the current sync run.
        if os.path.exists(self.quality_issues_file):
            os.remove(self.quality_issues_file)

        processed = 0
        skipped = 0
        for filename in os.listdir(downloads_dir):
            if filename.endswith(".html"):
                html_path = os.path.join(downloads_dir, filename)
                if self.process_file(html_path):
                    processed += 1
                else:
                    skipped += 1
        
        print(f"Sync summary: processed={processed}, skipped={skipped}")
        print("Sync complete.")

    def extract_primary_content_html(self, html):
        soup = BeautifulSoup(html, "html.parser")

        # Remove non-content sections before selecting main container.
        for selector in ["nav", "header", "footer", "aside", "script", "style", "noscript", "form"]:
            for node in soup.select(selector):
                node.decompose()

        candidates = [
            "main",
            "main#main-content",
            "article",
            "article.node",
            "div.region-content",
            "div#main-content",
            "div.node__content",
            "div.field--name-body",
        ]

        for selector in candidates:
            node = soup.select_one(selector)
            if node and node.get_text(strip=True):
                return str(node)

        # Fallback to body if no strong content container is found.
        body = soup.body
        if body and body.get_text(strip=True):
            return str(body)
        return html

    def record_quality_issue(self, html_file_path, issue, details=None):
        payload = []
        if os.path.exists(self.quality_issues_file):
            try:
                with open(self.quality_issues_file, "r", encoding="utf-8") as f:
                    payload = json.load(f)
            except Exception:
                payload = []

        payload.append({
            "html_file": html_file_path,
            "issue": issue,
            "details": details or {},
        })

        os.makedirs(os.path.dirname(self.quality_issues_file), exist_ok=True)
        with open(self.quality_issues_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    def process_file(self, html_file_path):
        if not os.path.isabs(html_file_path):
            html_file_path = os.path.join(self.repo_root, html_file_path)

        with open(html_file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        primary_html = self.extract_primary_content_html(html)
        markdown = self.transformer.transform(primary_html)
        if self.transformer.looks_like_homepage_boilerplate(markdown):
            self.record_quality_issue(
                html_file_path,
                "boilerplate-homepage-output",
                {"message": "Detected homepage boilerplate after retry; skipped output write."},
            )
            print(f"Skipped (quality): {html_file_path}")
            return False

        metadata = self.extractor.extract(primary_html)
        metadata['suggested_reviewers'] = self.contributors.extract_from_docs_page(html)

        # Reconstruct path from filename if URL is missing in metadata
        # Filename format: www_drupal_org_docs_develop_drupal-apis_token-api_overview-of-token-api.html
        base_name = os.path.basename(html_file_path).replace('.html', '')
        parts = base_name.split('_')
        
        # Remove 'www_drupal_org' and 'docs' to get a cleaner path
        path_parts = [p for p in parts if p not in ['www', 'drupal', 'org', 'docs']]
        
        if not path_parts:
            # Fallback for homepages
            path_parts = ["index"]
            
        file_name = path_parts[-1] + ".md"
        sub_dir = "/".join(path_parts[:-1])
        
        output_dir = os.path.join(self.content_docs_dir, sub_dir)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, file_name)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            yaml.dump(metadata, f)
            f.write("---\n\n")
            f.write(markdown)
        print(f"Processed: {output_path}")
        return True

    def run_jekyll(self):
        print("Starting Jekyll server...")
        # Use bundle exec jekyll serve
        subprocess.run(["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"], cwd=self.repo_root)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Drupal Docs Upgrade Orchestrator")
    parser.add_argument("--crawl", action="store_true", help="Run the conservative crawler")
    parser.add_argument("--sync", action="store_true", help="Transform all downloaded files")
    parser.add_argument("--serve", action="store_true", help="Run Jekyll server")
    parser.add_argument("--file", help="Process a single HTML file")
    parser.add_argument("--force", action="store_true", help="Bypass cooldown")
    parser.add_argument(
        "--llm-provider",
        choices=["ollama", "copilot", "gemini"],
        help="Temporarily force an LLM provider for this run",
    )
    parser.add_argument(
        "--no-cloud-fallback",
        action="store_true",
        help="Disable cloud fallback and run local-only for this command",
    )
    
    args = parser.parse_args()
    if args.llm_provider:
        os.environ["LLM_FORCE_PROVIDER"] = args.llm_provider
    if args.no_cloud_fallback:
        os.environ["LLM_ENABLE_CLOUD_FALLBACK"] = "false"

    orch = Orchestrator()

    if args.crawl:
        if args.force or orch.check_cooldown():
            orch.run_crawl()
    elif args.sync:
        orch.run_sync()
    elif args.serve:
        orch.run_jekyll()
    elif args.file:
        orch.process_file(args.file)
    else:
        parser.print_help()
