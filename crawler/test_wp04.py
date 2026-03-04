import os
import json
from automation.github_issue_creator import GithubIssueCreator
from automation.report_generator import JekyllReportGenerator

def test_automation():
    print("--- Starting WP04 Automation Test ---")
    
    # 1. Mock Gap Data
    mock_gaps = [
        {"severity": "High", "issue": "Missing Composer install instructions", "recommendation": "Add drupal/recommended-project snippet."},
        {"severity": "Medium", "issue": "Outdated PHP version referenced (8.1)", "recommendation": "Update to PHP 8.3 for Drupal 11."}
    ]
    
    # 2. Test Issue Creator (Mocked)
    print("\n[Step 1] Testing Issue Creator...")
    creator = GithubIssueCreator()
    creator.create_gap_issues(mock_gaps, "content/docs/test-install.md")
    
    # 3. Test Report Generator
    print("\n[Step 2] Testing Report Generator...")
    all_results = [
        {"file": "content/docs/test-install.md", "gaps": mock_gaps},
        {"file": "content/docs/managing-modules.md", "gaps": []}
    ]
    generator = JekyllReportGenerator(output_dir="content/reports/test_output/")
    generator.generate_report(all_results)
    
    print("\n[Result] Report generated at content/reports/test_output/library_health.md")
    print("--- WP04 Test Complete ---")

if __name__ == "__main__":
    test_automation()
