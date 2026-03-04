# Feature Specification: Drupal Documentation Upgrade System

**Feature Branch**: `001-drupal-docs-upgrade-system`  
**Created**: 2026-03-04  
**Status**: Draft  
**Input**: User description: "Improve the documentation that is available on Drupal. Consolidation and upgrade of d.o docs to D11 Markdown with semantic relationships and GitHub sync."

## Clarifications

### Session 2026-03-04
- Q: Crawler Authentication & Rate Limiting → A: Purely anonymous / public crawl with throttle control to avoid overloading Drupal.org.
- Q: Out-of-Scope Declaration (Media) → A: Mirror both text and media (images/PDFs) to ensure full documentation fidelity.
- Q: GitHub Pages UI Strategy → A: Use Jekyll (GitHub Pages default) for a simple but functional documentation experience.
- Q: Semantic Metadata Format → A: Combined approach (YAML Frontmatter for Jekyll + inline Microformats/RDFa in the content for structured data consumption).
- Q: Reviewer Suggestion Workflow → A: Passive list in page metadata ONLY (suggested reviewers added to frontmatter).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Doc Sync (Priority: P1)

As a Drupal documentation maintainer, I want the system to automatically crawl and sync HTML pages from Drupal.org (/docs and /documentation) into a GitHub repository so that they can be converted to Markdown and kept evergreen.

**Why this priority**: This is the foundational infrastructure. Without the raw content synced and converted, no further AI upgrades or semantic processing can occur.

**Independent Test**: The system successfully fetches a subset of HTML pages from d.o, converts them to Markdown files, and commits them to a designated GitHub repository via GitHub Actions.

**Acceptance Scenarios**:

1. **Given** a new or updated page exists on drupal.org/docs/7/example-page, **When** the GitHub Action runs, **Then** a corresponding `docs/7/example-page.md` file is created or updated in the repository.
2. **Given** a page is deleted from drupal.org, **When** the sync process identifies the missing source, **Then** it generates a report highlighting the page for potential deletion in the repo.

---

### User Story 2 - Semantic Markdown Conversion (Priority: P2)

As a developer or AI agent, I want the converted Markdown to include semantic frontmatter (RDFa-inspired) so that relationships between content and versions are easily discoverable.

**Why this priority**: Enhances the searchability and linkability of the documentation, moving beyond flat text to a structured knowledge base.

**Independent Test**: Converted Markdown files contain valid YAML frontmatter specifying source URL, original version (e.g., D7), and related entities.

**Acceptance Scenarios**:

1. **Given** a d.o HTML page with metadata, **When** converted to Markdown, **Then** the resulting file includes key-value pairs in frontmatter like `drupal_version: 7` and `original_author`.

---

### User Story 3 - Evergreen GitHub Pages Deployment (Priority: P3)

As a member of the Drupal community, I want to view the consolidated and upgraded documentation on a Jekyll-powered GitHub Pages site so that I have a clean, navigable interface.

**Why this priority**: Provides the end-user value and a visual dashboard for the project's progress.

**Independent Test**: The GitHub repository is successfully deployed to GitHub Pages using Jekyll, rendering the Markdown files as a navigable website with basic navigation.

**Acceptance Scenarios**:

1. **Given** a successful sync and conversion, **When** the deploy action triggers, **Then** the updated documentation is live on the project's GitHub Pages URL.

### Edge Cases

- **Duplicate Content**: How does the system handle pages that exist in both `/docs` and `/documentation` with identical or near-identical content?
- **Redirection Logic**: How are legacy D7 URLs mapped to their D11 counterparts when a direct mapping exists?
- **Sync Failures**: How does the system recover if drupal.org is temporarily unreachable during a crawl?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a crawler capable of a broad sweep of HTML content under `drupal.org/docs` and `drupal.org/documentation`.
- **FR-001.1**: Crawler MUST run as a purely anonymous/public client and MUST implement throttle control (request delays) to ensure zero negative impact on Drupal.org infrastructure.
- **FR-001.2**: Crawler MUST mirror both text content (for conversion) and binary assets (images, PDFs) associated with the targeted documentation pages.
- **FR-002**: System MUST use GitHub Actions to schedule and execute the crawl and sync process.
- **FR-003**: System MUST convert HTML content to Markdown, preserving structure (headers, lists, links).
- **FR-004**: System MUST extract and embed semantic metadata.
- **FR-004.1**: Metadata MUST be stored in YAML frontmatter (for Jekyll consumption) and MUST persist microformats/RDFa-style semantic markup within the Markdown/HTML content itself.
- **FR-005**: System MUST generate "Gap Reports" identifying missing information or EOL products that should be removed.
- **FR-006**: System MUST maintain high-fidelity tracking of original authors and contributors from the Drupal Issue Queue.
- **FR-006.1**: Suggested reviewers (based on contributor data) MUST be included as a passive list in the Markdown frontmatter for each page.
- **FR-007**: System MUST support iterative AI models for content upgrades (e.g., D7 to D11 logic) in a modular way, specifically leveraging Gemini for automated content analysis and transformation.

### Key Entities *(include if feature involves data)*

- **Documentation Page**: Represents a single page of content. Attributes: source URL, content (MD), version tags, metadata (RDfa).
- **Sync Job**: Represents an execution of the crawler/converter. Attributes: timestamp, files changed, errors encountered.
- **Gap/Obsolete Report**: A generated artifact identifying documentation that is missing or no longer relevant.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Initial "Broad Sweep" sync of d.o `/docs` and `/documentation` completes in under 2 hours for all publicly accessible HTML pages.
- **SC-002**: 100% of converted Markdown files include valid YAML frontmatter with at least 3 mandatory semantic fields (source, version, timestamp).
- **SC-003**: GitHub Pages site is updated and live within 15 minutes of a successful repository commit.
- **SC-004**: System successfully identifies and reports at least 90% of internal links that point to EOL (D7) content without a D11 alternative.
