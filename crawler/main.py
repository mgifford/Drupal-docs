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
        state_file = "content/sync_state.json"
        if os.path.exists(state_file):
            mtime = os.path.getmtime(state_file)
            elapsed = (time.time() - mtime) / 3600
            if elapsed < cooldown_hours:
                print(f"Cooldown active. Last sync was {elapsed:.1f} hours ago. (Limit: {cooldown_hours}h)")
                return False
        return True

    def run_crawl(self):
        print("Starting batch crawl (limit 20 pages)...")
        # Run scrapy from the crawler directory
        subprocess.run(["venv/bin/scrapy", "crawl", "documentation"], cwd="crawler")

    def run_sync(self):
        # Process files in crawler/downloads (assumed logic)
        # For simplicity, we look at where scrapy stores things or defined paths
        pass

    def process_file(self, html_file_path, output_dir="content/docs/"):
        with open(html_file_path, 'r') as f:
            html = f.read()

        markdown = self.transformer.transform(html)
        metadata = self.extractor.extract(html)
        metadata['suggested_reviewers'] = self.contributors.extract_from_docs_page(html)

        filename = os.path.basename(html_file_path).replace('.html', '.md')
        output_path = os.path.join(output_dir, filename)
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, 'w') as f:
            f.write("---\n")
            yaml.dump(metadata, f)
            f.write("---\n\n")
            f.write(markdown)
        print(f"Processed: {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Drupal Docs Upgrade Orchestrator")
    parser.add_argument("--crawl", action="store_true", help="Run the conservative crawler")
    parser.add_argument("--file", help="Process a single HTML file")
    parser.add_argument("--force", action="store_true", help="Bypass cooldown")
    
    args = parser.parse_args()
    orch = Orchestrator()

    if args.crawl:
        if args.force or orch.check_cooldown():
            orch.run_crawl()
    elif args.file:
        orch.process_file(args.file)
    else:
        parser.print_help()
