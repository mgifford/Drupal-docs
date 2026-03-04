# Tasks: Drupal Documentation Upgrade System

This document outlines the work packages (WPs) and subtasks required to implement the automated documentation upgrade system.

## Foundational Phase

### WP01: Foundation - Crawler Engine (Priority: P1)
**Goal**: Build the core Python-based crawling engine to mirror d.o content.
- [ ] T001: Initialize Python Scrapy project in `/crawler` <!-- id: T001 -->
- [ ] T002: Implement `DocumentationSpider` for d.o docs <!-- id: T002 -->
- [ ] T003: Implement `AssetPipeline` for images/PDFs <!-- id: T003 -->
- [ ] T004: Implement persistent `SyncSession` tracking <!-- id: T004 -->
- [ ] T005: Add Scrapy throttle/rate-limiting configuration <!-- id: T005 -->

**Summary**: Sets up the base infrastructure for mirroring content.
**Success Criteria**: Running the crawler mirrors text and media assets to the local `content/` folder without triggering d.o rate limits.

---

### WP02: Conversion - Semantic Markdown Transformer (Priority: P1)
**Goal**: Transform mirrored HTML into structured Markdown with semantic metadata.
- [ ] T006: Implement `MarkdownTransformer` (HTML to MD) <!-- id: T006 -->
- [ ] T007: Implement Metadata Extractor (RDFa/Microformats to Frontmatter) <!-- id: T007 -->
- [ ] T008: Implement `main.py` CLI orchestrator <!-- id: T008 -->
- [ ] T009: Implement Contributor Extractor for reviewer suggestions <!-- id: T009 -->

**Summary**: Handles the data transformation layer using a hybrid AI approach (Ollama for routine cleanup/extraction).
**Success Criteria**: Mirrored HTML is successfully converted to `.md` files with rich YAML frontmatter.

---

## Intelligence & Automation Phase

### WP03: Intelligence - AI Merging & Gap Identification (Priority: P2)
**Goal**: Leverage Gemini to merge content and find documentation gaps.
- [ ] T010: Integrate Gemini API Client <!-- id: T010 -->
- [ ] T011: Implement "AI Merger" for d.o + Drupal CMS consolidation <!-- id: T011 -->
- [ ] T012: Implement Gap Analysis logic (detecting missing/EOL info) <!-- id: T012 -->

**Summary**: Adds the AI layer for "smart" documentation upgrades.
**Success Criteria**: AI can identify missing D11 info and merge overlapping content sources.

---

### WP04: Automation - Reporting & GitHub Actions (Priority: P2)
**Goal**: Automate the sync and reporting workflow via GitHub.
- [ ] T013: Implement GitHub Issue Creator for gaps <!-- id: T013 -->
- [ ] T014: Implement Jekyll-compatible Gap Report generator <!-- id: T014 -->
- [ ] T015: Create GitHub Action (Daily Cron) workflow <!-- id: T015 -->
- [ ] T016: Implement Comment-Triggered Workflow ("Confirmed" trigger) <!-- id: T016 -->

**Summary**: Connects the local automation to the GitHub ecosystem.
**Success Criteria**: Daily runs create GitHub issues for gaps and update the web-based report.

---

## Presentation Phase

### WP05: Portal - Jekyll Documentation Site (Priority: P3)
**Goal**: Serve the upgraded documentation via a modern interface.
- [ ] T017: Set up Jekyll site structure and theme <!-- id: T017 -->
- [ ] T018: Implement dynamic navigation from file structure <!-- id: T018 -->
- [ ] T019: Implement version-specific UI callouts <!-- id: T019 -->

**Summary**: Provides the final user interface for the documentation.
**Success Criteria**: Consolidated docs are navigable, searchable, and version-aware on GitHub Pages.
