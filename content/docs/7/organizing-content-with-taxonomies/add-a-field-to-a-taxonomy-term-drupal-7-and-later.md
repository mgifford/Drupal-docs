---
author: null
drupal_version: '7'
last_updated: 22 August 2016
readability_score: 50.63
source_url: /docs/7/organizing-content-with-taxonomies/add-a-field-to-a-taxonomy-term-drupal-7-and-later
suggested_reviewers:
- Log in
- Create account
summary: Taxonomy now depends on the Field module. This allows you to add new fields
  to your Vocabulary Terms as you would to a Content Type. Please note that in order
  to add new fields you will need to have the Field UI module enabled. Adding a field
  to a Vocabulary will add that field to all Taxonomy Terms of the Vocabulary - not
  the Vocabulary object itself.
tags:
- Drupal
- Taxonomy
- Field
- Drupal 7
themes: null
title: Add a field to a taxonomy term (Drupal 7 and later)
---

# Add a field to a taxonomy term (Drupal 7 and later)

**Last updated on:** 22 August 2016

**Deprecated:** Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners)

Taxonomy now depends on the [Field](/handbook/modules/field) module. This allows you to add new fields to your Vocabulary Terms as you would to a Content Type. Please note that in order to add new fields you will need to have the [Field UI](http://drupal.org/handbook/modules/field-ui) module enabled. Adding a field to a Vocabulary will add that field to all Taxonomy Terms of the Vocabulary - not the Vocabulary object itself.

Because Drupal 7 entities (content nodes, users, taxonomy vocabularies, etc.) uses the [Field UI](http://drupal.org/handbook/modules/field-ui) module to manage fields you can just follow the directions over at [http://drupal.org/handbook/modules/field-ui](http://drupal.org/handbook/modules/field-ui) in order to add/remove a field to/from vocabularies.

> There's a lot about Drupal 7 that is designed to be more usable by beginners, but may be confusing if you come from D6 with expectations of where to find your tools. This is one of those situations.
>
> Fields (CCK) have been moved into core, and taxonomy is treated as just another field -- not some separate and special concept.
>
> If you edit your content type (admin->structure->content types) existing vocabularies will be available in the "add existing field" widget. To create a new vocabulary and associate it with a content type, just "add new field" of type "term reference."
>
> You also can go admin->structure->taxonomy and add a vocabulary there, but (as you discovered) that doesn't glue it to the content type.
>
> Copied from this comment [http://drupal.org/node/1107028#comment-4267500](http://drupal.org/node/1107028#comment-4267500) by yelvington