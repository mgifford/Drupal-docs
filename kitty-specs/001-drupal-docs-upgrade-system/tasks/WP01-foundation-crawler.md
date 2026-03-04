---
work_package_id: WP01
title: Foundation - Crawler Engine
lane: "doing"
dependencies: []
base_branch: main
base_commit: d3d9fb71b522a88251b01f9bd578768897ba1657
created_at: '2026-03-04T17:19:03.657365+00:00'
subtasks:
- T001
- T002
- T003
- T004
- T005
phase: Phase 1 - Infrastructure
shell_pid: "67378"
history:
- timestamp: '2026-03-04T12:15:00Z'
  lane: planned
  agent: system
  action: Prompt generated via /spec-kitty.tasks
---

# Work Package Prompt: WP01 – Foundation - Crawler Engine

## Objectives & Success Criteria
- Initialize a Python Scrapy project capable of mirroring Drupal.org documentation.
- Implement a spider that traverses `/docs` and `/documentation`.
- Success: Running the crawler populates `content/html` and `content/media` without triggering d.o rate limits.

## Context & Constraints
- Required for all downstream transformation and AI tasks.
- Must honor defined throttle control: 2s delay, 1 concurrent request.
- Reference: [plan.md](../plan.md), [research.md](../research.md).

## Subtasks & Detailed Guidance

### Subtask T001 – Initialize Python Scrapy project
- **Purpose**: Set up the environment and Scrapy boilerplate.
- **Steps**:
  1. Create `/crawler` directory.
  2. Initialize `scrapy startproject drupal_crawler .`.
  3. Define basic item structure for `Document` (url, title, html, assets).
- **Files**: `/crawler/scrapy.cfg`, `/crawler/items.py`.

### Subtask T002 – Implement `DocumentationSpider`
- **Purpose**: Traverse and fetch d.o documentation pages.
- **Steps**:
  1. Create spider in `spiders/doc_spider.py`.
  2. Target `drupal.org/docs` and `drupal.org/documentation`.
  3. Extract title and main content area HTML.
- **Files**: `/crawler/spiders/doc_spider.py`.

### Subtask T003 – Implement `AssetPipeline`
- **Purpose**: Download and store images/PDFs.
- **Steps**:
  1. Configure `FilesPipeline`.
  2. Store files in `content/media/` preserving d.o relative paths if possible.
- **Files**: `/crawler/pipelines.py`, `/crawler/settings.py`.

### Subtask T004 – Implement `SyncSession` tracking
- **Purpose**: Support incremental crawls.
- **Steps**:
  1. Maintain a JSON file (e.g., `sync_state.json`) in `content/`.
  2. Track last crawled URL and timestamp per page.
- **Files**: `/crawler/spiders/doc_spider.py`.

### Subtask T005 – Add Scrapy throttle configuration
- **Purpose**: Ensure zero negative impact on d.o.
- **Steps**:
  1. Set `DOWNLOAD_DELAY = 2`.
  2. Set `CONCURRENT_REQUESTS_PER_DOMAIN = 1`.
  3. Enable `AUTOTHROTTLE_ENABLED = True`.
- **Files**: `/crawler/settings.py`.

## Risks & Mitigations
- **Risk**: IP Blocking by Drupal.org.
- **Mitigation**: Very aggressive throttling and user-agent rotation.

## Activity Log
- 2026-03-04T12:15:00Z – system – lane=planned – Prompt created.
