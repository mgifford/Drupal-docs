---
author: null
drupal_version: '7'
last_updated: 11 July 2017
readability_score: 38.95
source_url: /docs/7/organizing-content-with-taxonomies/create-a-vocabulary
suggested_reviewers:
- Log in
- Create account
summary: In Drupal 7, vocabularies are used to group, organize, and categorize a set
  of taxonomy terms. This guide explains how to create a vocabulary and add terms
  to it.
tags:
- Drupal 7
- taxonomy
- vocabulary
themes:
- Drupal 7
title: Create a vocabulary
---

# Create a vocabulary

Last updated on 11 July 2017

**Deprecated**: Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners).

## Creating Vocabularies in Drupal 7

In D7, Vocabularies are used to group, organize and, in many cases, categorize a set of taxonomy terms. Vocabularies are fieldable entities and are given a name and vocabulary id (vid) making it referenceable by other Drupal components. So, vocabularies can be thought of as parent or root containers for taxonomy terms. Creating a vocabulary can be as simple as assigning the container a name. You can, optionally, add fields (e.g., an image field, etc.) to your vocabulary at admin/structure/taxonomy/[your-vocabulary-name]/fields.

To create a vocabulary in D7, go to admin/structure/taxonomy, then click Add Vocabulary. Drupal will prompt for:

- **Vocabulary name** (Required) -- A name for this vocabulary; for example, Topics.
- **Description** (Optional) -- A description of the vocabulary (this item may be used by some modules and feeds).

That's it, your vocabulary is created and waiting for you to add some terms to it. Other contributed modules like the [Taxonomy Menu](https://www.drupal.org/project/taxonomy_menu) module may add additional configurable settings to the admin/structure/taxonomy/add page.

Note that D7 comes with an empty 'Tags' vocabulary already setup for you. The 'Tags' vocabulary is a 'free-tagging' vocabulary that will hold user created terms that are added to the Tags vocabulary when content is created or edited. This is generally accomplished by using a term reference field with an auto-complete widget on the content creation page.

## Creating Vocabularies in Drupal 5 and 6

When setting up a vocabulary, Drupal will prompt for:

- **Vocabulary name** (Required) -- A name for this vocabulary; for example, Topics.
- **Description** (Optional) -- A description of the vocabulary (this item may be used by some modules and feeds).
- **Types** (Required) -- A vocabulary may be associated with one or more node types. So, an administrator might declare that a particular vocabulary is to be associated with stories and blogs, but not book pages. If an expected node type is unavailable, check and make sure that the module for the specific node type has been activated.
- **Hierarchy** (Optional) -- Allows a tree-like taxonomy (In Drupal 5, hierarchies are set as an option. In Drupal 6 and later, all vocabularies are hierarchical if that's how you arrange the items.).
- **Related terms** (Optional) -- Allows relationships between terms within this vocabulary. Think of these as "see also" references (this item is not used by many Drupal modules).
- **Freetagging** (Optional) -- Users create terms as they go by typing comma-separated lists of the terms they want to apply to content instead of selecting from a pre-existing list of terms. Freetagging vocabularies will present users with a text input that will autocomplete with matching terms if they exist.
- **Multiple select** (Optional) -- Allows users to categorize nodes by more than one term. Useful for cross-indexing content. Nodes may then appear on multiple taxonomy pages.
- **Required** (Optional) -- Requires a user to select a term in this vocabulary in order to submit the node. Otherwise, when creating a node, users will be offered a **none** option as the default for each vocabulary.
- **Weight** (Optional) -- Allows the administrator to set the priority of this vocabulary when listed with other vocabularies. When vocabularies are left with the default weight of zero, Drupal displays multiple vocabularies in alphabetical order. Increasing a vocabularies weight with respect to other vocabularies will cause it to appear after them in lists. Conversely, lighter vocabularies will float nearer the top of lists. Useful for specifying which vocabulary a user sees first when creating a node.