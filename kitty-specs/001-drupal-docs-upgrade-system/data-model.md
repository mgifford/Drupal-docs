# Data Model: Drupal Documentation Upgrade System

## Entities

### DocumentationPage
Represents a single documentation artifact.
- **id**: Slug derived from the source path.
- **title**: Extracted from `<title>` or `<h1>`.
- **content**: The Markdown transformed from HTML.
- **frontmatter**: Structured YAML metadata.
- **status**: `mirrored` | `upgraded` | `obsolete`.
- **version_context**: Mapping of content sections to Drupal versions (D10, D11, CMS).

### Asset
Binary file mirrored from the source.
- **original_url**: URL on d.o.
- **local_path**: Relative path in `content/media/`.
- **mimetype**: Image, PDF, etc.

### SyncSession
Record of a crawling execution.
- **timestamp**: Start/End times.
- **pages_fetched**: Count.
- **errors**: List of failed URLs and reasons.
- **gaps_identified**: List of missing information points found by AI.

## State Transitions

1. **Discovery**: Crawler identifies a URL.
2. **Mirroring**: Content is saved locally as HTML/Metadata.
3. **Conversion**: HTML is transformed into Markdown with basic frontmatter.
4. **Upgrade (Optional)**: AI (Gemini) analyzes the page, merges sources, and enhances instructions.
5. **Review**: Reporting system flags gaps; users confirm via comment triggers.
