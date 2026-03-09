---
author: N/A
drupal_version: '8'
last_updated: 17 June 2024
readability_score: 29.03
source_url: /docs/8/api/migrate-api/migrate-process-plugins/process-plugins-from-contrib-modules/other-process-plugins
suggested_reviewers:
- Log in
- Create account
summary: These process plugins are listed with a short description of each. If you
  think that any of these deserve a separate page, then add the page to this guide.
  Ask the guide maintainer(s) to add your page to the menu. Do not delete the description
  here until the new page is added to the menu.
tags:
- Drupal
- Migrate API
- Process plugins
- Contrib modules
themes: N/A
title: Other process plugins
---

# Other process plugins

Last updated on 17 June 2024

These process plugins are listed with a short description of each.

If you think that any of these deserve a separate page, then add the page to this guide. Ask the guide maintainer(s) to add your page to the menu. Do not delete the description here until the new page is added to the menu.

- **entity_field_lookup**: The Entity Field Lookup module provides a process plugin that looks up an existing entity based on an EntityQuery performed on a field that is declared in the configuration, and possible other (static) conditions.
- **make_array_associative**: The Make Array Associative module provides a process plugin that converts an indexed array of flat values to an indexed array of single-element associative arrays. That is, each flat value of the original array becomes a new associative array, whose key is defined in the plugin configuration and whose value is the original array's value of that position.
- **migrate_process_extract_regex**: The Migrate Process Extract Regex module provides a Migrate Process plugin to that accepts a Regular expression argument to match and extract a string from a string
- **migrate_process_html**: The Migrate Process HTML module provides a Migrate process plugin to enable you to use parse HTML from a url or link field such as those commonly found in RSS Feeds.
- **migrate_process_js_redirect_link**: The Migrate Process JS Redirect Link module provides a Migrate process plugin to enable to enable you to request and extract a link from a inter-linked JS enabled redirect page commonly found on Google RSS feeds. 
- **migrate_process_newspaper3k**: The Migrate Process Newspaper3k module provides a Migrate process plugin for article curation from a url endpoint.
- **migrate_process_newspaper_playwright**: The Migrate Process Newspaper Playwright module provides a Migrate process plugin for article curation from a url endpoint.
- **migrate_process_remote_image_check**: The Migrate Process Remote Image Check module provides a Migrate process plugin to enable you to check whether a migrated remote image url/string is in fact a valid address for a media asset such as an image. It does this by requesting each image url to see if it returns a valid response.
- **migrate_process_text_to_paragraphs**: The Migrate Process Text to Paragraphs module provides a Migrate process plugin to that converts a delimited string into a collection of html paragraphs (similar to nl2br()).