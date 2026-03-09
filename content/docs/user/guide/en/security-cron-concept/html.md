---
author:
- "Di\xE1na Lakatos"
- Dave Hansen-Lange
- Boris Doesborg
drupal_version: '7'
last_updated: 14 April 2025
readability_score: 60.79
source_url: /docs/user_guide/en/security-cron-concept.html
suggested_reviewers:
- Log in
- Create account
summary: 'To ensure that your site and its modules continue to function well, a group
  of administrative operations should be run periodically. These operations are called
  cron tasks. Examples of cron tasks are: checking for module and theme updates, indexing
  content for search, or cleaning up temporary files.'
tags:
- Cron
- Security
- Maintenance
- Drupal
themes:
- Pronovix
- Advomatic
title: '13.1. Concept: Cron'
---

# 13.1. Concept: Cron

To ensure that your site and its modules continue to function well, a group of administrative operations should be run periodically. These operations are called **cron** tasks. Examples of cron tasks are: checking for module and theme updates, indexing content for search, or cleaning up temporary files.

## What is the relationship between the site’s cron tasks and Unix cron?

Linux/Unix-based operating systems have a cron scheduler that can be used to run periodic tasks. You can use the server’s cron scheduler to schedule runs of the site’s cron tasks. Alternatively, you can use the core Automated Cron module to run tasks. You can check the site’s cron tasks' status in the status report.

## Related topics

* [Section 13.2, “Configuring Cron Maintenance Tasks”](/docs/user_guide/en/security-cron.html)
* [Section 12.5, “Concept: Status Report”](/docs/user_guide/en/prevent-status.html)

## Additional resources

* [Drupal.org community documentation page "Setting up cron"] https://www.drupal.org/docs/7/setting-up-cron/overview
* **Attributions**
  * Written and edited by
    * [Diána Lakatos](https://www.drupal.org/u/dianalakatos) at [Pronovix](https://pronovix.com/)
    * [Dave Hansen-Lange](https://www.drupal.org/u/dalin) at [Advomatic](https://www.advomatic.com/)
    * [Boris Doesborg](https://www.drupal.org/u/batigolix)