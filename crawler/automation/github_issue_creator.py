import os
from github import Github

class GithubIssueCreator:
    def __init__(self, token=None, repo_name=None):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.repo_name = repo_name or os.environ.get("GITHUB_REPOSITORY")
        if not self.token or not self.repo_name:
            # Fallback for local testing or if environment isn't set
            print("Warning: GITHUB_TOKEN or GITHUB_REPOSITORY not set. Issue creation will be mocked.")
            self.gh = None
        else:
            self.gh = Github(self.token)
            self.repo = self.gh.get_repo(self.repo_name)

    def create_gap_issues(self, gaps_json, source_file):
        if not self.gh:
            print(f"Mocking issue creation for {len(gaps_json)} gaps in {source_file}")
            return

        for gap in gaps_json:
            title = f"Documentation Gap: {gap['issue']} in {os.path.basename(source_file)}"
            body = f"""
### Documentation Audit Finding

**Issue**: {gap['issue']}
**Severity**: {gap['severity']}
**Source File**: [{os.path.basename(source_file)}]({source_file})
**Recommendation**: {gap['recommendation']}

---
*Automated audit by DrupalDocsUpgradeBot*
            """
            self.repo.create_issue(
                title=title,
                body=body,
                labels=["documentation-gap", gap['severity']]
            )
            print(f"Created issue: {title}")
