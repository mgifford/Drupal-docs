---
author: null
drupal_version: '7'
last_updated: 22 November 2017
readability_score: 53.55
source_url: /docs/7/organizing-content-with-taxonomies/guidelines-for-taxonomy-design
suggested_reviewers:
- Log in
- Create account
summary: The importance of good taxonomy design in Drupal, especially when using the
  Views module. Guidelines include keeping vocabularies below 30-40 terms, avoiding
  over-reliance on parent-child relationships, managing complexity, understanding
  client needs, dealing with legacy issues, and recognizing taxonomy as a trial and
  error process.
tags:
- taxonomy
- Drupal 7
- Views module
themes: null
title: Guidelines for taxonomy design
---

# Guidelines for taxonomy design

Last updated on 22 November 2017

**Drupal 7 will no longer be supported after January 5, 2025. Learn more and find resources for Drupal 7 sites.**

In small sites, the taxonomy scheme is usually obvious. But in larger projects -- especially when experts are categorizing content to be read by laypeople -- good taxonomy design can be the difference between an intuitive site and an information architecture nightmare. The importance of good taxonomy design has only increased with the rise of the [Views module], which relies on powerful, taxonomy-based Filters.

**General Rules**

1. Unless a vocabulary is well-known to all anticipated users -- for example, an alphabetical list of world countries -- keep it below 30-40 terms.
2. Use parent-child relationships with caution. If your taxonomy relies on these structures, think about dividing up the vocabulary. An unwieldy parent-child scheme is often a sign of poor design.

**Example**

An online art shop has taxonomized its products as follows:

- Europe
  - Lapp
  - Sami
  - Celtic
- Australia
  - Aboriginal

Even though this accurately shows how the shop classifies its items, its insistence on many small categories prevents a user from saying, "show me some European art."

Multiple-select is one way around this, but not the best way. It's better to use *two vocabularies*: one for region, one for culture. Make them both multiple-select, and our art collector can now ask: "What have you got which is Lapp, or Celtic or Chinese?"

**Too many terms**

"Perfect" taxonomies are always too complex and you need to fight to make them more manageable (especially if you have just cut up a few parent-child vocabularies into several smaller ones).

The advantage of [Views] is that the multiple taxonomy terms start to build context, and that can be captured by Views.

There are not many sites that ever need to show more than 3-4 filters to users, even if there are 5-6 more hidden ones.

Plus, building them into structure adds even more granularity.

**Example**

A site for all the small towns of America, where people are interested in their little town's stuff, using [Book] for basic structure.

Top level - states - 50 items  
Off each state - counties  
Off each county - settlements  

Click the named settlement and get a Views list with filters for news, culture and announcements.

(Hidden filters in the Views filter by State/County/Settlement)

Highly non scary - any users can use that to get what they need.

**Clients are not experts on taxonomy, not even their own**

Taxonomy is a communications issue and if there is a budget for the site it's always worth running it past an outsider -- but note that they will need to get to understand the purpose of the site and also to an extent the jargon of the subject.

This normally requires at least one decent face to face meeting to force the client to decide what is important, and what can be cut out. Trust me, these decisions will have to be made, and if they are not, then people are probably not thinking carefully enough.

**Taxonomy creates legacy issues - so get it right!**

Once you have a load of tagged data, it's hard to make changes to taxonomy structures (apart from adding terms) without rendering existing nodes much harder to find. Trust me, *no one* will go back and edit existing data, not in real life, unless there is massive funding for that purpose.

**Taxonomy is trial and error**

It should be the first thing you do on a site, but by adding test data you'll find flaws, and refine and eventually go live with something that works. In between times you solved the CSS and templating...

I once spent 3 days testing different ways to classify cars for one site -- the makes/models complexity of past 20 years is a nightmare, and there are several ways to do it, all of which work, some are more user friendly than others!