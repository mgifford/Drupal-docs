---
author: null
drupal_version: Drupal 8
last_updated: 1 May 2022
readability_score: 37.17
source_url: /docs/8/api/migrate-api/migrate-process-plugins/process-plugins-from-other-contrib-modules/contrib-process-plugin-geofield_latlon
suggested_reviewers:
- Log in
- Create account
summary: The contributed Geofield module provides a field type for storing geographic
  data in Drupal 7 & Drupal 8. The module also provides a Migrate API geofield_latlon
  process plugin.
tags:
- Migrate API
- geofield_latlon
- Geofield
- Drupal 8
themes: null
title: 'Contrib process plugin: geofield_latlon'
---

### Contrib process plugin: geofield_latlon

Last updated on 1 May 2022

This documentation **needs work**. See "Help improve this page" in the sidebar.

The contributed [Geofield](https://www.drupal.org/project/geofield) module provides a field type for storing geographic data in Drupal 7 & Drupal 8. The module also provides a Migrate API `geofield_latlon` process plugin.

#### Migrating latitude and longitude from a custom data source to Drupal 8 Geofield

The `geofield_latlon` plugin can transform latitude and longitude from custom data sources to Drupal 8 Geofield values.

Example migration_plus manifest:

```php
Drupal 8 Target field : field_drupal8_geofield
Custom sources of data :
  lat
  lon
```

```php
field_drupal8_geofield:
  plugin: geofield_latlon
  source:
    - lat
    - lon
```

#### Upgrading Drupal 7 Geofield values to Drupal 8

The upgrade path from Drupal 7 Geofield to Drupal 8 Geofield is now complete. See [https://www.drupal.org/project/geofield/issues/3003822](https://www.drupal.org/project/geofield/issues/3003822).