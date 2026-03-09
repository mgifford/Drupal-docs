---
author: null
drupal_version: '7'
last_updated: 22 August 2016
readability_score: 51.85
source_url: /docs/7/organizing-content-with-taxonomies/add-a-vocabulary-to-a-content-type
suggested_reviewers:
- Log in
- Create account
summary: To use taxonomy terms to organize your content, the vocabulary must be associated
  with the content type. To add vocabulary, go to structure->taxonomy->add vocabulary.
  Here you can add a vocabulary list. Once created, you will see it appear in the
  list and can click to "view terms" and then will be able to add terms to the vocabulary
  list.
tags: null
themes: null
title: Add a vocabulary to a content type
---

# Add a vocabulary to a content type

**Last updated on:** 22 August 2016

**Deprecated:** Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners)

To use taxonomy terms to organize your content, the vocabulary must be associated with the content type. To add vocabulary, go to structure->taxonomy->add vocabulary. Here you can add a vocabulary list. Once created, you will see it appear in the list and can click to "view terms" and then will be able to add terms to the vocabulary list.

1. In order to associate taxonomy terms to your content, you must add a field of type 'term reference' on the /Administration/Structure/Content types/[your-content-type]/Manage fields page.
2. Add a new field by entering a label in the **Add new field** box, select **Term reference** from the dropdown box in Field Type, then select the relevant widget.

   ![Add a term reference field in a content type](/files/node1886980_1.jpg)

3. Click **Save**. You are immediately taken to the Field Settings page.
4. Select the vocabulary that you want to use with this term reference field, then click **Save Field Settings**.

   ![Select the vocabulary to use for the term reference](/files/node1886980_2.jpg)

5. You are taken to a page to configure the newly added term reference field. Here you can change the term label, provide some help text and provide a default value.

**Help improve this page**

Page status: No known problems

You can:
- Log in, click **Edit**, and edit this page
- Log in, click **Discuss**, update the Page status value, and suggest an improvement
- Log in and [create a Documentation issue](/node/add/project-issue/documentation?title=Suggestion%20for%3A%20%281886980%29%20Add%20a%20vocabulary%20to%20a%20content%20type) with your suggestion