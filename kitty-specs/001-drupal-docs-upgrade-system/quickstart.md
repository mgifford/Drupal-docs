# Quickstart: Drupal Documentation Upgrade System

## Prerequisites
- Python 3.11+
- GitHub access token (for Issue/Action automation)
- Gemini API Key

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install scrapy beautifulsoup4 pandoc-preprocessor
   ```
3. Initialize the crawler:
   ```bash
   python crawler/main.py init
   ```

## Running the Sync
The system is designed to run automatically via GitHub Actions (Daily Cron). To run manually:
```bash
python crawler/main.py sync --scope broad
```

## Reviewing Gaps
1. Check the **GitHub Issues** labeled `documentation-gap`.
2. To approve a gap fix or transition a page to "upgraded" status, comment `/confirm` on the respective issue.
