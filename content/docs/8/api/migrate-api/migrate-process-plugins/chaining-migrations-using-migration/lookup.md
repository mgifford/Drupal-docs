---
author: John Doe
date: '2023-04-14T12:00:00Z'
readability_score: 45.36
source: https://example.com/documentation/chaining-migrations-using-migration-lookup
suggested_reviewers:
- Log in
- Create account
summary: This documentation explains how to use the migration_lookup plugin to chain
  migrations in Drupal, including how it works, examples, and less common use cases.
tags:
- Migration
- Drupal
title: Chaining Migrations using migration_lookup
---

# Chaining Migrations using migration_lookup

Last updated on 15 Mar 2023

## Users and Nodes example

The `migration_lookup` plugin is used to find the destination key(s) for a given source key(s) in the mapping table for a migration. For example, if you have a source key `sourceid1` with a value of `123` in the `migrate_map_d7_user` table, you can use the `migration_lookup` plugin to find the corresponding destination key `destid1` with a value of `456`.

## Stub entities

Stub entities are created by default when the `migration_lookup` plugin is unable to find a destination key for a given source key. This can happen if a referenced entity has not yet been created. Stub entities can be updated by a subsequent migration.

## Migrate Magician

The `Migrate Magician` contrib module provides improved stubbing functionality compared to core. However, it currently has a limitation where the stubbing lookup only works with Drupal database sources.

## How it works

The `migration_lookup` plugin queries the mapping table for a migration to find the destination key(s) for a given source key(s). This allows for the chaining of migrations, where the output of one migration is used as the input for another.

## Example reference fields

The following example demonstrates how to import a node reference field from Drupal 7 to Drupal 9+. The `migration_lookup` plugin is used to determine the target_id value for the destination field_location.

```php
field_location:
  plugin: sub_process
  source: field_location
  process:
    target_id:
      plugin: migration_lookup
      migration:
        - mysite_node_location
        - mysite_node_room
      source: target_id
```

This example shows how to use the `sub_process` plugin to wrap the `migration_lookup` step and repeat it for each source value. The `migration_lookup` requires a `source`, which in this case is the property 'target_id'. Other reference fields may use a different ID, such as 'tid' for term reference fields.

## Less common use cases

For more information on less common use cases of the `migration_lookup` plugin, see the [official documentation page](https://api.drupal.org/api/drupal/core!modules!migrate!src!Plugin!migrate!process!MigrationLookup.php/class/MigrationLookup).