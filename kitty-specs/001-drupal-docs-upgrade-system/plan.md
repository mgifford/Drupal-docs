# Implementation Plan: [FEATURE]
*Path: [templates/plan-template.md](templates/plan-template.md)*


**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/kitty-specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/spec-kitty.plan` command. See `src/specify_cli/missions/software-dev/command-templates/plan.md` for the execution workflow.

The planner will not begin until all planning questions have been answered—capture those answers in this document before progressing to later phases.

## Summary

The **Drupal Documentation Upgrade System** will leverage a Python-based crawling and conversion engine to mirror `drupal.org` documentation (/docs and /documentation) into this repository. It will use GitHub Actions for automated, throttled synchronization and Gemini for intelligent content analysis and transformation. The resulting structured Markdown (frontmatter + inline RDFa) will be served via Jekyll on GitHub Pages.

### Engineering Alignment
- **Crawler Stack**: Python (Scrapy/BeautifulSoup/Pandoc)
- **Content Storage**: In-repo (mirrored Markdown and assets)
- **Deployment**: GitHub Pages (Jekyll)
- **AI Agent**: Hybrid (Gemini for Reasoning, Ollama for Transformation)
- **Local Model**: `qwen2.5-coder:7b` via Ollama (http://localhost:11434)
- **Sync Schedule**: GitHub Actions (Daily Cron)
- **Reporting Strategy**: Hybrid (GitHub Issues for Gaps + Jekyll Report Page)
- **Workflow Trigger**: Issue comments (e.g., "Confirmed") to approve/transition content.
- **Consolidation Strategy**: AI-Driven Merger (Consolidate d.o and Drupal CMS into a unified version).
- **Validation Approach**: Gemini-grounded for stable releases (D11 focus), with frontmatter highlighting version-specific instructions for D10, D11, and Drupal CMS.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11+
**Primary Dependencies**: Scrapy, Beautiful Soup 4, Pandoc/TurnDown, Jekyll
**Storage**: File-based (git repository) for Markdown and Binary assets
**Testing**: pytest for crawler/converter logic
**Target Platform**: GitHub Actions (Runner), GitHub Pages
**Project Type**: Python CLI / Automation + Jekyll Site
**Performance Goals**: Throttle-controlled sync to avoid Drupal.org load
**Scale/Scope**: ~10k+ documentation pages, multiple gigabytes of media assets

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on constitution file]

## Project Structure

### Documentation (this feature)

```
kitty-specs/001-drupal-docs-upgrade-system/
├── plan.md              # This file
├── research.md          # Implementation research findings
├── data-model.md        # Metadata and entity definitions
├── quickstart.md        # Setup guide for the new system
├── contracts/           # Crawler/API interfaces
└── tasks.md             # Work package definitions (future)
```

### Source Code (repository root)

```
crawler/                 # Python crawling/conversion engine
├── spiders/             # Scrapy spiders for d.o
├── transformers/        # HTML to Markdown + AI Logic
└── main.py              # CLI Entry point

content/                 # Mirrored Documentation (Managed by automation)
├── docs/                # Converted d.o docs
├── media/               # Mirrored assets
└── reports/             # Jekyll gap reports

.github/
└── workflows/           # Daily cron sync actions

_config.yml              # Jekyll configuration
index.md                 # Documentation Portal homepage
```

**Structure Decision**: A dual-purpose repository combining the Python automation engine (under `crawler/`) and the generated static site content (under `content/` and root).

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |