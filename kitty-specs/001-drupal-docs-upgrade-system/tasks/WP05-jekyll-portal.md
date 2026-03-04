---
work_package_id: WP05
title: Portal - Jekyll Documentation Site
lane: planned
dependencies: []
subtasks:
- T017
- T018
- T019
phase: Phase 3 - Presentation
history:
- timestamp: '2026-03-04T12:15:00Z'
  lane: planned
  agent: system
  action: Prompt generated via /spec-kitty.tasks
---

# Work Package Prompt: WP05 – Portal - Jekyll Documentation Site

## Objectives & Success Criteria
- Set up a clean, modern documentation site on GitHub Pages.
- Dynamic navigation from converted docs.
- Version-aware UI callouts.

## Objectives & Success Criteria
- Jekyll successfully renders documentation from `content/docs/`.
- Site is deployed to GitHub Pages.

## Subtasks & Detailed Guidance

### Subtask T017 – Set up Jekyll site structure
- **Purpose**: Base UI portal.
- **Steps**:
  1. Initialize Jekyll in repository root.
  2. Choose/Configure a docs-focused theme (e.g., Just the Docs).
- **Files**: `/_config.yml`, `/Gemfile`.

### Subtask T018 – Implement dynamic navigation
- **Purpose**: Ease of use.
- **Steps**:
  1. Use Jekyll collections or directory listing for navigation.
  2. Auto-generate sidebar from file folder structure.
- **Files**: `/_includes/sidebar.html`, `/_layouts/default.html`.

### Subtask T019 – Implement version UI callouts
- **Purpose**: Release clarity.
- **Steps**:
  1. Create Jekyll includes for "D11 Only", "Drupal CMS", etc.
  2. Render these callouts based on frontmatter flags.
- **Files**: `/_includes/version_notice.html`.

## Activity Log
- 2026-03-04T12:15:00Z – system – lane=planned – Prompt created.
