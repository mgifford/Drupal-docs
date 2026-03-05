# Drupal Documentation Style Guide

This guide establishes the standards for the automated documentation upgrade process. It draws from the [Drupal.org Style Guide](https://www.drupal.org/drupalorg/style-guide) and industry standards for technical writing.

## 1. Tone and Voice
- **Words and Phrases**: Use gender-neutral language. Prefer "they/them" over "he/she". Avoid jargon where a simpler word suffices. Define acronyms on first use.
- **Conversational but Professional**: Use a friendly tone for tutorials and a straightforward, technical tone for reference material.
- **Action-Oriented**: Focus on what the user can *do*. Use imperative verbs ("Install", "Configure", "Run").

## 2. Design Principles & Layout
- **Accessibility (CRITICAL)**: Use semantic HTML (headers in order H1, H2, H3). Provide alt text for all images. Ensure high contrast for code blocks.
- **Grid and Structure**: Use the Diátaxis framework:
    - **Tutorials**: Learning-oriented.
    - **How-to Guides**: Task-oriented.
    - **Reference**: Information-oriented.
    - **Explanation**: Understanding-oriented.
- **Scannability**: Use short paragraphs (2-5 sentences). Use bulleted and numbered lists extensively. Use bolding for key terms.

## 3. Typography and Markup
- **Typography**: Follow Drupal brand guidelines where possible. In Markdown, use backticks for `code`, `file_paths`, and `commands`.
- **Markup**: Ensure code blocks have language identifiers (e.g., ```php). Use Jekyll-specific alerts for tips and warnings:
    - `{: .important }`
    - `{: .note }`
    - `{: .warning }`

## 4. Documentation Framework (Writing Standard)
Every documentation page should aim for this structure:
1. **Introduction**: What problem does this solve?
2. **Quick Start**: How to get results in 5 minutes.
3. **Core Concepts**: Key principles and terminology.
4. **Detailed Steps**: The "meat" of the guide.
5. **FAQ/Common Pitfalls**: Anti-patterns or common errors.
6. **Change Log**: What changed in Drupal 11 vs earlier versions.

## 5. References and Gap Analysis
- Use [drupalbook.org](https://drupalbook.org/) as a secondary intelligence source to identify missing documentation gaps in our crawled content.
- Reference professional writing guides: [HeroThemes](https://herothemes.com/blog/how-to-write-documentation/), [GitHub Blog](https://github.blog/developer-skills/documentation-done-right-a-developers-guide/), and [Dev.to](https://dev.to/auden/how-to-write-technical-documentation-in-2025-a-step-by-step-guide-1hh1).
