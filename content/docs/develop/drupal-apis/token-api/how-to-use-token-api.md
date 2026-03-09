---
error: Failed to parse metadata
raw: The provided text is a structured HTML document that outlines the usage and functionality
  of the Token API in Drupal. The document includes sections detailing how to use
  the `Token::replace` method, what other methods are available within the Token service,
  and how the process of replacing tokens works internally. Additionally, there is
  a section for users to help improve the documentation by suggesting edits or reporting
  issues. The document is formatted with Drupal's default theme and uses panels for
  layout, which is typical of Drupal's administrative interface.
readability_score: 48.26
suggested_reviewers:
- Log in
- Create account
---

The provided text is a detailed technical documentation page for using the Token API in a Drupal application. This API is crucial for dynamic content generation and manipulation, allowing developers to insert content, such as node titles, user names, or other data from the Drupal database, directly into HTML templates. Here's a breakdown of the key sections and features described in the documentation:

1. **Introduction to Token API**: The document begins by introducing what the Token API is, its purpose, and how it works within a Drupal site.

2. **Token::replace Method**: The core functionality of the Token API is the `replace` method, which processes a string and replaces tokens with their corresponding values. It supports both HTML and plain text replacements and can handle various options like clearing undefined tokens or applying callbacks to the replacements.

3. **Other Token API Methods**: The document lists other useful methods provided by the Token API, such as `findWithPrefix`, `generate`, `getInfo`, `replacePlain`, `resetInfo`, `scan`, and `setInfo`. Each method is briefly described and linked to its API documentation.

4. **How Token::replace Works**: A detailed explanation of how the `replace` method operates internally. It outlines the steps involved in scanning the text for tokens, generating replacements, and applying options like callbacks.

5. **Help Improve This Page**: The document concludes with a section encouraging users to contribute to improving the page content. It provides options to edit the page, discuss issues, or create new documentation issues.

6. **Footer**: The page includes a footer section, which is typically used for copyright information or links to related resources.

The documentation is structured in a way that is easy to navigate, with headings and subheadings that break down the content into manageable sections. It also includes links to detailed API documentation, which is essential for developers looking to use the Token API in their projects.