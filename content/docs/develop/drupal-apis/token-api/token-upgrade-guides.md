---
author: null
drupal_version: '11.1'
last_updated: 20 April 2025
readability_score: 44.28
source_url: /docs/develop/drupal-apis/token-api/token-upgrade-guides
suggested_reviewers:
- Log in
- Create account
summary: This page provides guides on how to upgrade the Token API in Drupal from
  different versions.
tags:
- Token API
- Drupal APIs
- Object-oriented hooks
- Drupal 11.1
- Drupal 7 to 8
- Drupal 6 to 7 upgrade guide
themes: null
title: Token upgrade guides
---

# Token upgrade guides

Last updated on 20 April 2025

This documentation **needs review**. See "Help improve this page" in the sidebar.

## Object-oriented hook system (Drupal 11.1+)

Since [Drupal 11.1](https://www.drupal.org/blog/drupal-11-1-0), hooks can be implemented as classes that use the attribute `Drupal\Core\Hook\Attribute\Hook` to denote specific methods as belonging to specific hooks.

Instead of implementing `hook_token_info` or `hook_tokens`, you would create a new PHP class, add functions that implement `hook_token_info` or `hook_tokens` within the class, and set the `#[Hook('token_info')]` or `#[Hook('tokens')]` attribute before your function declaration.

Some examples of this usage have been provided in the guides for implementing [hook_token_info](https://www.drupal.org/docs/develop/drupal-apis/token-api/token-api-hooks#s-object-oriented-implementation-example-for-drupal-111) and [hook_tokens](https://www.drupal.org/docs/develop/drupal-apis/token-api/token-api-hooks#s-object-oriented-implementation-example-for-drupal-111--2).

## Drupal 7 to 8+

Updating `hook_token_info` and `hook_tokens` for Drupal 8+ mainly involves allowing type declarations for arguments and return values, and adding `$bubbleable_metadata` for hook_tokens.

Type declarations for arguments and return values is well-supported in newer PHP versions and is highly recommended to ensure functions are being called safely.

Bubbleable metadata is required in some cases to pass cache metadata to the top-level render method, which is critical if rendering a token that may involve something that might differ due to certain caching rules, such as URLs.

For more information, consult [api.drupal.org](https://api.drupal.org)'s documentation on these two hooks and compare their example implementations from version to version.

- `hook_token_info`
  - [hook_token_info in Drupal 11.x](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Utility%21token.api.php/function/hook_token_info/11.x)
  - [hook_token_info in Drupal 7.x](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_token_info/7.x)

- `hook_tokens`
  - [hook_tokens in Drupal 11.x](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Utility%21token.api.php/function/hook_tokens/11.x)
  - [hook_tokens in Drupal 7.x](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_tokens/7.x)

## Drupal 6 to 7 upgrade guide

A comprehensive guide for updating Token API from Drupal 6 to Drupal 7 can be found at [https://www.drupal.org/documentation/modules/token/update/6/7](https://www.drupal.org/documentation/modules/token/update/6/7)