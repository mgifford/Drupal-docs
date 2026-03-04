---
work_package_id: WP02
title: Conversion - Semantic Markdown Transformer
lane: "doing"
dependencies: []
base_branch: main
base_commit: 145423071d31e5a07938d420fe2add327a7821f8
created_at: '2026-03-04T18:21:18.371909+00:00'
subtasks:
- T006
- T007
- T008
- T009
phase: Phase 1 - Infrastructure
shell_pid: "67378"
history:
- timestamp: '2026-03-04T12:15:00Z'
  lane: planned
  agent: system
  action: Prompt generated via /spec-kitty.tasks
---

# Work Package Prompt: WP02 – Conversion - Semantic Markdown Transformer

## Objectives & Success Criteria
- Convert raw HTML documentation into structured Markdown.
- Extract semantic metadata (RDFa/Frontmatter) for Jekyll consumption.
- Provide a unified CLI orchestrator for the sync process.

## Context & Constraints
- Depends on output from **WP01**.
- **Model Routing**: Use Ollama (`qwen2.5-coder:7b`) at `http://localhost:11434` for routine Markdown normalization and metadata extraction.
- Must preserve semantic structure (headings, lists, code blocks).

## Subtasks & Detailed Guidance

### Subtask T006 – Implement `MarkdownTransformer`
- **Purpose**: Transform HTML to high-quality Markdown.
- **Steps**:
  1. Use Pandoc or a Python library like `markdownify`.
  2. Ensure links to Drupal.org are preserved or relative-linked if the target exists in content.
- **Files**: `/crawler/transformers/md_transformer.py`.

### Subtask T007 – Implement Metadata Extractor
- **Purpose**: Extract semantic context into YAML Frontmatter.
- **Steps**:
  1. Parse HTML for Microformats/RDFa tags.
  2. Map these to defined schema fields in `data-model.md`.
- **Files**: `/crawler/transformers/metadata_extractor.py`.

### Subtask T008 – Implement `main.py` CLI orchestrator
- **Purpose**: Entry point for users and CI.
- **Steps**:
  1. Implement commands: `crawl`, `transform`, `sync` (both).
  2. Use `argparse` or `click`.
- **Files**: `/crawler/main.py`.

### Subtask T009 – Implement Contributor Extractor
- **Purpose**: Identify experts for content review.
- **Steps**:
  1. If a documentation page links to an issue queue, fetch the top contributors list.
  2. Append these usernames to the `suggested_reviewers` frontmatter.
- **Files**: `/crawler/transformers/contributor_extractor.py`.

## Risks & Mitigations
- **Risk**: Variable HTML structure on d.o causing broken Markdown.
- **Mitigation**: Implement robust sanitization and fallbacks for common d.o content wrapper patterns.

## Activity Log
- 2026-03-04T12:15:00Z – system – lane=planned – Prompt created.
