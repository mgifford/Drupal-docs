---
author: null
drupal_version: null
last_updated: 24 April 2025
readability_score: 34.65
source_url: /docs/develop/drupal-apis/token-api/overview-of-token-api
suggested_reviewers:
- Log in
- Create account
summary: Token API in Drupal exists to allow replacement of placeholders in text --
  "tokens" -- with contextual values that match those placeholders. These tokens are
  formatted in a consistent pattern and are used in various cases to provide inter-operation
  between different parts of Drupal's framework.
tags:
- Token API
- Drupal API
- Use cases
themes: null
title: Overview of Token API
---

# Overview of Token API

Token API in Drupal exists to allow replacement of placeholders in text -- "tokens" -- with contextual values that match those placeholders. These tokens are formatted in a consistent pattern:

```html
[data-type:chained:values:value]
```

The data-type component might be a content entity type like node, a configuration entity type like view, or a completely custom type like site or date.

Depending on the token value you are trying to fetch, you might have to chain several values together to get to the value you are trying to reach. For example, you might have a specific node and want to print the name of the author. You might start with text formatted like so:

```html
The node's author is: [node:author:display-name]
```

This traverses through the following steps in Drupal's content hierarchy:

1. Starts with the Node itself
2. Traverses to the author
3. Fetches the display name for the author

So in the end, the text returned matches the display name of the author linked through entity references.

The output would look something like:

```html
The node's author is: Jane Doe
```

## Use cases

Tokens aren't necessarily available throughout Drupal sites in their entirety. They mainly appear in cases that provide inter-operation between different parts of Drupal's framework -- acting as a sort of "glue" that passes data from one component to another.

Some cases where you might see tokens appear include the following:

1. Where Drupal defines email templates that are personalized to the user receiving them, such as the User Accounts configuration
    - This allows emails to users to be populated with facts relevant to them, such as their username, or their first name if there's a field for it, and so on.
    - When users register new accounts, a callback in the API is called to attach additional tokens that are usually unsafe to have available, such as the dynamically generated URL that lets users reset their password.
2. Configuration for core modules
    - File upload directory names
    - Views plugins such as Row, Field or Area
3. Specific field formatters, such as Link field titles
4. Configuration for contributed modules
    - [Metatag](https://www.drupal.org/project/metatag) is a great example because it can take tokenized input to return both summarized and precise information about content entities for rendering into page markup as metatags.
    - [Pathauto](https://www.drupal.org/project/pathauto) is another great example because it provides configuration for rendering URL aliases for nodes and other content. The module renders raw URL aliases with tokens replaced to set items in the path like `[node:title]`, `[node:field_category:entity:name]` and so on -- and Pathauto finishes by normalizing out any non-ASCII characters and spaces, ensuring a clean, SEO-friendly, and above all consistent URL alias.
5. Adding additional token types and extending the capabilities of Token API
    - The [Token](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/token) contributed module does this, adding a token tree browser, additional tokens and token types, and most crucially, entity field tokens that allow deeply nested fields to be surfaced through tokens.

There are many more use cases for the Token API, but this might give you a few ideas about how you could use it.