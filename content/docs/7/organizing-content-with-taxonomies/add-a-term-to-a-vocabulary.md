---
author: null
drupal_version: '7'
last_updated: 22 August 2016
readability_score: 47.05
source_url: https://example.com/docs/7/organizing-content-with-taxonomies/add-a-term-to-a-vocabulary
suggested_reviewers:
- Log in
- Create account
summary: Once you have finished defining the vocabulary, you may populate it with
  terms using Add. Add terms to a vocabulary by navigating to admin/structure/taxonomy/[your-vocabulary-name]/add.
  Drupal will prompt for term name, description, parents, related terms, synonyms,
  weight, and URL alias.
tags:
- Drupal
- Taxonomy
- Content Organization
- Drupal 7
themes: null
title: Add a term to a vocabulary
---

# Add a term to a vocabulary

Last updated on 22 August 2016

Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners)

Once you have finished defining the vocabulary, you may populate it with terms using Add. Add terms to a vocabulary by navigating to admin/structure/taxonomy/[your-vocabulary-name]/add. From there, Drupal will prompt for:

- **Term name** (Required) -- The name for this term. Example: Technology.
- **Description** (Optional) -- Description of the term (this item may be used by some modules and feeds).

Advanced options:

- **Parents** (Optional): Select the term(s) under which this term is a subset.
- **Related terms** (Optional, D6 only): Choose any terms that are related to the one you are creating.
- **Synonyms** (Optional, D6 only): Enter synonyms for this term, one synonym per line. Synonyms can be used for variant spellings, acronyms, and other terms that have the same meaning as the added term, but which are not explicitly listed in this thesaurus, i.e. unauthorized terms (this item not used by many Drupal modules).
- **Weight** (Optional): The weight is used to sort the terms of this vocabulary; by default they will be sorted alphabetically.
- **URL Alias** (Optional, D7): Default is "/taxonomy/term/" but here you can specify an alias like "term1" and the final url will be "/term1".

## Help improve this page

Page status: No known problems

You can:

- Log in, click [Edit](/node/23406/edit), and edit this page
- Log in, click [Discuss](/node/23406/discuss), update the Page status value, and suggest an improvement
- Log in and [create a Documentation issue](/node/add/project-issue/documentation?title=Suggestion%20for%3A%20%2823406%29%20Add%20a%20term%20to%20a%20vocabulary) with your suggestion