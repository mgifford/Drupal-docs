import os
import sys
import time
import json
import yaml
import subprocess
from transformers.md_transformer import OllamaClient, MarkdownTransformer
from transformers.metadata_extractor import MetadataExtractor
from transformers.contributor_extractor import ContributorExtractor
from intelligence.orchestrator import IntelligenceOrchestrator
from automation.github_issue_creator import GithubIssueCreator
from automation.report_generator import JekyllReportGenerator

class Orchestrator:
    def __init__(self):
        self.ollama = OllamaClient()
        self.transformer = MarkdownTransformer(self.ollama)
        self.extractor = MetadataExtractor(self.ollama)
        self.contributors = ContributorExtractor()
        self.intel = IntelligenceOrchestrator()
        self.issue_creator = GithubIssueCreator()
        self.report_gen = JekyllReportGenerator()

    def check_cooldown(self, cooldown_hours=4):
        state_file = "crawler/content/sync_state.json"
        if os.path.exists(state_file):
            mtime = os.path.getmtime(state_file)
            elapsed = (time.time() - mtime) / 3600
            if elapsed < cooldown_hours:
                print(f"Cooldown active. Last sync was {elapsed:.1f} hours ago. (Limit: {cooldown_hours}h)")
                return False
        return True

    def run_crawl(self):
        print("Starting batch crawl (limit 20 pages)...")
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        scrapy_bin = os.path.join(root_dir, "venv", "bin", "scrapy")
        
        if not os.path.exists(scrapy_bin):
            print(f"Error: Scrapy not found at {scrapy_bin}")
            return

        subprocess.run([scrapy_bin, "crawl", "documentation"], cwd="crawler")

    def run_sync(self):
        print("Syncing: Transforming downloaded HTML into Markdown...")
        downloads_dir = "crawler/downloads"
        if not os.path.exists(downloads_dir):
            print("No downloads found.")
            return

        for filename in os.listdir(downloads_dir):
            if filename.endswith(".html"):
                html_path = os.path.join(downloads_dir, filename)
                self.process_file(html_path)
        
        print("Sync complete.")

    def process_file(self, html_file_path):
        with open(html_file_path, 'r') as f:
            html = f.read()

        markdown = self.transformer.transform(html)
        metadata = self.extractor.extract(html)
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
        
        output_dir = os.path.join("content", "docs", sub_dir)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, file_name)

        with open(output_path, 'w') as f:
            f.write("---\n")
            yaml.dump(metadata, f)
            f.write("---\n\n")
            f.write(markdown)
        print(f"Processed: {output_path}")

    def run_jekyll(self):
        print("Starting Jekyll server...")
        # Use bundle exec jekyll serve
        subprocess.run(["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Drupal Docs Upgrade Orchestrator")
    parser.add_argument("--crawl", action="store_true", help="Run the conservative crawler")
    parser.add_argument("--sync", action="store_true", help="Transform all downloaded files")
    parser.add_argument("--serve", action="store_true", help="Run Jekyll server")
    parser.add_argument("--file", help="Process a single HTML file")
    parser.add_argument("--force", action="store_true", help="Bypass cooldown")
    
    args = parser.parse_args()
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
