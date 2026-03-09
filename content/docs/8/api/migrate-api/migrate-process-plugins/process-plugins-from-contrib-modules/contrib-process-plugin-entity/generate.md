---
author: null
drupal_version: '8'
last_updated: 25 March 2025
readability_score: 29.48
source_url: /docs/8/api/migrate-api/migrate-process-plugins/process-plugins-from-contrib-modules/contrib-process-plugin-entity_generate
suggested_reviewers:
- Log in
- Create account
summary: The entity_generate plugin, provided by the contributed Migrate Plus module,
  is used to match existing entities and generate entities that don't yet exist. It's
  commonly used for taxonomy term reference fields.
tags:
- Migrate Plus
- entity_generate
- Taxonomy terms
- Migrate process plugins
themes: []
title: 'Contrib process plugin: entity_generate'
---

The `entity_generate` plugin, provided by the contributed [Migrate Plus](https://www.drupal.org/project/migrate_plus) module, is used to match existing entities (by entity type, bundle type, and value_key) and generate entities that don't yet exist. The most common use is for taxonomy term reference fields.

**Taxonomy Terms Example with Documentation**

Here's a taxonomy term example using all of the possible configuration parameters (spacing and commenting only for documentation purposes):

```php
process:
  field_tags:
    plugin: entity_generate
    source: 'Tag'
    value_key: name
    bundle_key: vid
    bundle: tags
    entity_type: taxonomy_term
    ignore_case: true
    default_values:
      status: 1
    values:
      description: 'Tag description'
```

**Example of Generating Multiple Taxonomy Terms**

If you have multiple terms in your source, for example `tags`: `great;helpful;awesome`, you can split them up with the [Migrate plugin Explode](https://api.drupal.org/api/drupal/core%21modules%21migrate%21src%21Plugin%21migrate%21process%21Explode.php/class/Explode) where the data is separated before being piped on to `entity_generate` and get created:

```php
process:
  field_tags:
    - plugin: explode
      source: tags
      delimiter: ';'
    - plugin: entity_generate
      value_key: name
      bundle_key: vid
      bundle: tags
      entity_type: taxonomy_term
```

A single term import can be done like this:

```php
process:
  field_photo_category:
    plugin: entity_generate
    source: photo_category
    value_key: name
    bundle_key: vid
    bundle: image_category
    entity_type: taxonomy_term
```

**Create terms and insert custom field values at the same time**

Vocabulary terms can have extra fields, and it's possible to generate a non-existing term, while at the same time inserting a value into another field. This example shows how to loop over a nested JSON-file, create a non-existing term, and populate a multi-value field.

**JSON source:**

```php
[
  {
    "companies": [
      {
        "company_name": "Company INC.",
        "company_link": "https://example.org/"
      },
      {
        "company_name": "ABC Company",
        "company_link": "https://example.com/"
      }
    ]
  }
]
```

**Combining `sub_process` and `entity_generate`:**

```php
process:
  taxonomy_vocabulary_4:
    plugin: sub_process
    source: companies
    process:
      target_id:
        plugin: entity_generate
        source: company_name
        value_key: name
        bundle_key: vid
        bundle: vocabulary_4
        entity_type: taxonomy_term
        values:
          field_link/value: company_link
```

**Example of Generating/Looking Up Nodes by Title**

Node generation is similar to taxonomy terms, but the `bundle_key` for nodes is `type` (for the content type of the node):

```php
process:
  field_related_articles:
    plugin: entity_generate
    source: 'title'
    entity_type: node
    bundle: article
    value_key: title
    bundle_key: type
    default_values:
      title: 'Title missing'
    values:
      title: 'title'
```

**Example of Generating Users**

The following example was taken from a migration for a comment:

```php
process:
  uid:
    - plugin: skip_on_empty
      method: row
      source: 'Author email'
      message: 'Author email is required but missing.'
    - plugin: entity_generate
      entity_type: user
      value_key: mail
      values:
        name: 'Author email'
```

**Help improve this page**

- Log in, click **Edit**, and edit this page
- Log in, click **Discuss**, update the Page status value, and suggest an improvement
- Log in and [create a Documentation issue](/node/add/project-issue/documentation?title=Suggestion%20for%3A%20%282883987%29%20Contrib%20process%20plugin%3A%20entity_generate) with your suggestion