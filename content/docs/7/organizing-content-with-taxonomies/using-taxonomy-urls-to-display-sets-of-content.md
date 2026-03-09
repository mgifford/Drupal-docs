---
author: null
drupal_version: '7'
last_updated: 22 August 2016
readability_score: 44.24
source_url: /docs/7/organizing-content-with-taxonomies/using-taxonomy-urls-to-display-sets-of-content
suggested_reviewers:
- Log in
- Create account
summary: This document explains how to use taxonomy URLs to display sets of content
  in Drupal 7. It covers how to combine Term IDs using commas and plus signs to create
  listings of nodes using either OR both taxonomy terms.
tags:
- Taxonomy
- Drupal 7
- Content organization
themes: null
title: Using taxonomy URLs to display sets of content
---

# Using taxonomy URLs to display sets of content

**Last updated on** 22 August 2016

**Deprecated**: Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners)

When displaying nodes, both in teaser listings on the Drupal home pages and in full, single-node view, many Drupal themes display the categories applied to the node. If the user selects any category term, Drupal will then display a browsable listing for all nodes tagged with that term. 

Examine the Taxonomy URL for one such category listing. The end of the URL should look something like this:

```php
taxonomy/term/1
```

And another Taxonomy URL, for a different term, something like this:

```php
taxonomy/term/2
```

Note that Taxonomy URLs always contain one or more Term IDs at the end of the URL. These numbers, 1 and 2 above, tell Drupal which categories to display.

Now combine the Term ID's above in one URL using a comma as a delimiter:

```php
taxonomy/term/1,2
```

The resulting listing represents the boolean AND operation. It includes all nodes tagged with both terms. To get a listing of nodes using either taxonomy term 1 OR 2, use a plus sign as the operator

```php
taxonomy/term/1+2 
```

Want to combine more categories? Just add more delimiters and numbers. Know that you can use the taxonomy section in Drupal site administration to find out any Term ID. Just place the cursor over any *edit term* and look to the status bar at the bottom of the browser. Then substitute the new Term ID's found there to create a different category listing.

In addition to displaying Drupal nodes by category on site, Drupal has category specific RSS feeds for other sites to access your site content. See how the URL format for the RSS feed is very similar to the Taxonomy URL:

```php
taxonomy/term/1+2/0/feed
```

This feature has been removed in Drupal 7.

Building individual Taxonomy URL's is not the most user friendly way to provide site users access to browsable listings. Nor do administrators necessarily want to build custom blocks for users with links to each category listing. To extend the means of accessing nodes by category, evaluate the following modules:

- [Taxonomy Menu](http://drupal.org/project/taxonomy_menu)
- [Dhtml Menu](http://drupal.org/project/dhtml_menu)