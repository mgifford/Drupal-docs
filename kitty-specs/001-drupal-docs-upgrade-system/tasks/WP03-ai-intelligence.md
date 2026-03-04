---
work_package_id: WP03
title: Intelligence - AI Merging & Gap Identification
lane: planned
dependencies: []
subtasks:
- T010
- T011
- T012
phase: Phase 2 - Intelligence
history:
- timestamp: '2026-03-04T12:15:00Z'
  lane: planned
  agent: system
  action: Prompt generated via /spec-kitty.tasks
---

# Work Package Prompt: WP03 – Intelligence - AI Merging & Gap Identification

## Objectives & Success Criteria
- Integrate Gemini for content analysis.
- Unify Drupal.org and Drupal CMS documentation.
- Detect documentation gaps for D11.

## Context & Constraints
- Depends on infrastructure in **WP01** and **WP02**.
- Uses Gemini API (as decided in planning).
- Must adhere to the "Unified" consolidation strategy.

## Subtasks & Detailed Guidance

### Subtask T010 – Integrate Gemini API Client
- **Purpose**: Provide AI capabilities to the transformer.
- **Steps**:
  1. Set up `google-generativeai` package.
  2. Implement utility to send content for analysis/rewrite.
- **Files**: `/crawler/ai_client.py`.

### Subtask T011 – Implement AI Merger logic
- **Purpose**: Consolidate disparate documentation sources.
- **Steps**:
  1. Detect overlapping topics between d.o and Drupal CMS.
  2. Prompt Gemini to merge them into a single, high-fidelity Markdown page.
- **Files**: `/crawler/transformers/ai_merger.py`.

### Subtask T012 – Implement Gap Analysis logic
- **Purpose**: Identifying what's missing for Drupal 11.
- **Steps**:
  1. Compare existing documentation against AI's knowledge of D11.
  2. Generate a JSON report of "missing sections" or "outdated D7 guidance".
- **Files**: `/crawler/transformers/gap_analyzer.py`.

## Risks & Mitigations
- **Risk**: AI Hallucinations in merged documentation.
- **Mitigation**: Mandatory human review via the "Confirmed" workflow (WP04).

## Activity Log
- 2026-03-04T12:15:00Z – system – lane=planned – Prompt created.
