---
author: "Di\xE1na Lakatos, Jojy Alphonso, Joe Shindelar"
drupal_version: Not explicitly mentioned
last_updated: 14 April 2025
readability_score: 56.44
source_url: /docs/user_guide/en/install-dev-sites.html
suggested_reviewers:
- Log in
- Create account
summary: Development Sites are different copies of the same site used for developing,
  updating, and testing a site without risking the integrity of the live site.
tags:
- Drupal
- Development Sites
- Documentation
themes:
- Not explicitly mentioned
title: '11.7. Concept: Development Sites'
---

# 11.7. Concept: Development Sites

Last updated on 14 April 2025

Development Sites are different copies of the same site used for developing, updating, and testing a site without risking the integrity of the live site.

An example deployment workflow for site building will usually include the sites mentioned below:

- **Local environment**: The development process starts with developers working on new features, bug fixes, theming, and configuration in their local environment. The recommended tool for setting up a local environment is DDEV. See [Setting Up an Environment with DDEV](/docs/user_guide/en/install-ddev.html).

- **Development site**: Developers push the changes they’ve been working on to the development site. For a team of more than one developer, version control is usually used. Git is a version control system that tracks your files for any changes. You can then commit those changes to a repository. Using Git allows team members to work on the same site without overriding each other’s work. It also makes it possible to easily roll back to previous stages of the development.

- **Staging site**: The staging site can be used for testing, or presenting the changes to the client for approval. QA (Quality Assurance) and UAT (User Acceptance Testing) are most often carried out on the staging site. It is recommended to have live content on both the development and staging sites, so that you can test how the new features will work with the existing content.

- **Production site**: The live site on the web available to visitors. It contains new features that have been proven safe to go live.

Based on the project’s size, scope, requirements, or stakeholders, stages from the above workflow can be removed, or additional stages can be added. For example, a testing site before staging can be added to separate testing and user acceptance processes.

## Related topics

- [Making a Development Site](/docs/user_guide/en/install-dev-making.html)
- [Setting Up an Environment with DDEV](/docs/user_guide/en/install-ddev.html)
- [Concept: Editorial Workflow](/docs/user_guide/en/planning-workflow.html)
- [Managing File and Configuration Revisions with Git](/docs/user_guide/en/extend-git.html)

**Attributions**

Written and edited by [Diána Lakatos](https://www.drupal.org/u/dianalakatos), [Jojy Alphonso](https://www.drupal.org/u/jojyja) at [Red Crackle](http://redcrackle.com), and [Joe Shindelar](https://www.drupal.org/u/eojthebrave) at [Drupalize.Me](https://drupalize.me).

This page is generated from [AsciiDoc](http://asciidoc.org/) source from the [User Guide](/project/user_guide). To propose a change, edit the source and attach the file to a [new issue in the User Guide project](/node/add/project-issue/user_guide). PDF and e-book formats are available on the [User Guide project page](/project/user_guide).

Source file: install-dev-sites.asciidoc

## Help improve this page

Page status: No known problems

You can:

- Log in, click [Edit](/node/2827367/edit), and edit this page
- Log in, click [Discuss](/node/2827367/discuss), update the Page status value, and suggest an improvement
- Log in and [create a Documentation issue](/node/add/project-issue/documentation?title=Suggestion%20for%3A%20%282827367%29%2011.7.%20Concept%3A%20Development%20Sites) with your suggestion