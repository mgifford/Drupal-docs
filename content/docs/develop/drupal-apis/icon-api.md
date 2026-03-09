---
error: Failed to parse metadata
raw: "The provided text is a detailed documentation on an Icon API for Drupal, a popular\
  \ content management system. Here's a summary of the key points:\n\n1. **Icon Packs**:\
  \ The API allows for the creation of custom icon packs, each represented by a provider\
  \ plugin. Each pack has a unique ID and can include metadata like enabled status,\
  \ label, description, links, version, and license.\n\n2. **Extractors**: These are\
  \ plugins responsible for discovering icons within a pack. The text mentions built-in\
  \ extractors for SVG and web fonts, as well as an example extractor for Iconify\
  \ Icons.\n\n3. **Rendering Icons**:\n   - **PHP**: Icons can be rendered using a\
  \ new render element called `icon`. It requires the pack ID and icon ID, and optionally\
  \ a settings array.\n   - **Twig**: A Twig function `icon()` is available for rendering\
  \ icons. It takes the pack ID, icon ID, and an optional settings array as parameters.\n\
  \n4. **Contrib Module**: The text mentions a contributed module called \"UI Icons\"\
  \ that uses this API to integrate icons into Drupal.\n\n5. **Documentation and Feedback**:\
  \ The documentation includes information on how to help improve the page, suggesting\
  \ either editing the page directly, discussing the page status, or creating a documentation\
  \ issue.\n\nThe overall goal of this API is to provide a flexible and extensible\
  \ way to integrate icons into Drupal, supporting various types of icons and allowing\
  \ for easy customization and extension."
readability_score: 52.26
suggested_reviewers:
- Log in
- Create account
---

This document provides an overview of Drupal's Icon API, which allows developers to add and use icons in their Drupal sites. The key features and concepts covered include:

1. Icon Packs: 
   - A set of related icons provided by a specific icon pack provider.
   - Defined using a YAML configuration file.

2. Extractors:
   - Plugins that discover icons from various sources (e.g. SVG files, web fonts).
   - Implement the IconExtractorInterface.

3. Rendering Icons:
   - PHP render element: #type => 'icon'
   - Twig function: {{ icon('pack_id', 'icon_id', settings) }}

4. Icon Packs Available:
   - SVG based: 
     - Material Symbols
     - Iconify
     - Font based: 
       - Material Icons
       - FontAwesome
       - Iconify

5. Adding Custom Extractors:
   - Modules can create custom extractors by implementing IconExtractorInterface.
   - Plugins are declared using PHP attributes.

6. Icon Rendering in Twig:
   - The icon() Twig function can be used to render icons directly in templates.

7. Documentation and Contribution:
   - The page mentions a contrib module called UI Icons that uses this API.
   - It provides links for users to contribute improvements or suggest changes to the documentation.

Overall, this API provides a flexible and extensible framework for integrating various icon sets and rendering them throughout a Drupal site. The documentation covers the core features and provides examples of how to use the API.