# Research: Drupal Documentation Upgrade System

This document captures the research findings and architectural decisions for the Drupal documentation upgrade automation.

## Decision Log

### Decision: Python-based Crawler
- **Rationale**: Python offers superior libraries for web scraping (Scrapy), HTML parsing (BeautifulSoup), and data transformation (Pandoc wrappers). It also integrates natively with many AI SDKs (Gemini).
- **Alternatives Considered**: Node.js (Puppeteer) was considered but identified as overkill for the mostly static Drupal.org documentation.

### Decision: Hybrid Reporting (Issues + Jekyll)
- **Rationale**: GitHub Issues provide an actionable "in-box" for community members to see gaps, while a Jekyll-rendered report provides a high-level overview of the library's health. The "Confirmed" comment trigger allows for human-in-the-loop verification before major upgrades are merged.

### Decision: AI Merger Strategy
- **Rationale**: Simplifies the documentation experience by presenting a single "best" version of a requirement, rather than forcing users to check multiple disparate sources.

### Decision: Local Model Routing (Ollama)
- **Rationale**: Use `qwen2.5-coder:7b` via http://localhost:11434 for routine Markdown cleanup and metadata extraction to save Gemini for high-level reasoning.

## Implementation Details

### Metadata Schema (RDFa/Frontmatter)
The system will inject the following mandatory fields into Markdown frontmatter:
- `source_url`: Original d.o or Drupal CMS URL.
- `drupal_version`: Primary version target (e.g., D11).
- `related_versions`: List of other supported versions covered (D10, Drupal CMS).
- `suggested_reviewers`: List of top contributors extracted from d.o issue queues.
- `last_sync`: ISO timestamp.

### Throttle Control
To avoid load on `drupal.org`, the Scrapy engine will be configured with:
- `DOWNLOAD_DELAY`: 2 seconds (minimum).
- `CONCURRENT_REQUESTS_PER_DOMAIN`: 1.
- `AUTOTHROTTLE_ENABLED`: True.

## Dependencies & Best Practices
- **Scrapy**: Use `FilesPipeline` for mirroring pdfs/images.
- **Pandoc**: Use for high-fidelity HTML-to-Markdown conversion.
- **GitHub Actions**: Use `workflow_dispatch` for manual runs and `schedule` for daily cron.
