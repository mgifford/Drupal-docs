---
error: Failed to parse metadata
raw: "### Updating Entities and Fields in Drupal 8\n\n#### Overview\nUpdating entities\
  \ and fields in Drupal 8 involves creating update functions to handle schema changes\
  \ and migrations. This ensures that your data remains consistent and your site functions\
  \ correctly after updates. This guide will cover various scenarios, including changing\
  \ field types, deleting fields, and handling revisions.\n\n#### Creating Update\
  \ Functions\nUpdate functions are defined in your module's `.install` file and are\
  \ named according to a convention. For example, if your module is named `my_module`,\
  \ and you are adding an update function for version 8001, the function should be\
  \ named `my_module_update_8001`.\n\n#### Example: Changing Field Type\nTo change\
  \ the type of a field, you need to store the existing values, clear out the old\
  \ field, uninstall the old field, create a new field, install the new field, and\
  \ then restore the values.\n\n```php\nfunction my_module_update_8001() {\n    $database\
  \ = \\Drupal::database();\n    $transaction = $database->startTransaction();\n\n\
  \    $entity_type_manager = \\Drupal::entityTypeManager();\n    $bundle_of = 'node';\n\
  \n    $storage = $entity_type_manager->getStorage($bundle_of);\n    $bundle_definition\
  \ = $entity_type_manager->getDefinition($bundle_of);\n    $id_key = $bundle_definition->getKey('id');\n\
  \    $table_name = $storage->getDataTable() ?: $storage->getBaseTable();\n    $definition_manager\
  \ = \\Drupal::entityDefinitionUpdateManager();\n\n    // Store existing values.\n\
  \    $status_values = $database->select($table_name)\n        ->fields($table_name,\
  \ [$id_key, 'status_field'])\n        ->execute()\n        ->fetchAllKeyed();\n\n\
  \    // Clear out the values.\n    $database->update($table_name)\n        ->fields(['status_field'\
  \ => NULL])\n        ->execute();\n\n    // Uninstall the field.\n    $field_storage_definition\
  \ = $definition_manager->getFieldStorageDefinition('status_field', $bundle_of);\n\
  \    $definition_manager->uninstallFieldStorageDefinition($field_storage_definition);\n\
  \n    // Create a new field definition.\n    $new_status_field = BaseFieldDefinition::create('string')\n\
  \        ->setLabel(t('Status field'))\n        ->setDescription(t('The status -\
  \ either no, yes or skip.'))\n        ->setDefaultValue('no')\n        ->setRevisionable(FALSE)\n\
  \        ->setTranslatable(FALSE);\n\n    // Install the new definition.\n    $definition_manager->installFieldStorageDefinition('status_field',\
  \ $bundle_of, $bundle_of, $new_status_field);\n\n    // Restore the values.\n  \
  \  $value_map = [\n        '1' => 'yes',\n        '0' => 'no',\n    ];\n    foreach\
  \ ($status_values as $id => $value) {\n        $database->update($table_name)\n\
  \            ->fields(['status_field' => $value_map[$value]])\n            ->condition($id_key,\
  \ $id)\n            ->execute();\n    }\n\n    // Commit transaction.\n    unset($transaction);\n\
  }\n```\n\n#### Example: Deleting a Field\nTo delete a field, remove the field code\
  \ from the entity class, delete the field from `entity_keys` in the entity definition,\
  \ uninstall the field, and run cron.\n\n```php\nfunction my_module_update_8002()\
  \ {\n    $update_manager = \\Drupal::entityDefinitionUpdateManager();\n    $definition\
  \ = $update_manager->getFieldStorageDefinition('name_of_old_field_to_delete', 'entity_type');\n\
  \    $update_manager->uninstallFieldStorageDefinition($definition);\n}\n```\n\n\
  #### Useful Drush Commands\nDrush commands can help you check and manipulate the\
  \ schema version of your module.\n\n- **Checking the current schema version of a\
  \ module:**\n\n  ```php\n  drush php-eval \"echo drupal_get_installed_schema_version('my_module');\"\
  \n  ```\n\n  For Drupal 9+:\n\n  ```php\n  drush php-eval \"echo \\Drupal::service('update.update_hook_registry')->getInstalledVersion('my_module');\"\
  \n  ```\n\n- **Manually setting the current schema version of a module:**\n\n  ```php\n\
  \  drush php-eval \"echo drupal_set_installed_schema_version('my_module', '8000');\"\
  \n  ```\n\n  For Drupal 9+:\n\n  ```php\n  drush php-eval \"\\Drupal::service('update.update_hook_registry')->setInstalledVersion('my_module',\
  \ '9000');\"\n  ```\n\n#### Conclusion\nUpdating entities and fields in Drupal 8\
  \ requires careful planning and execution. By using update functions and understanding\
  \ the lifecycle of fields, you can ensure that your site remains functional and\
  \ your data remains consistent."
readability_score: 5.32
suggested_reviewers:
- Log in
- Create account
---

This is a comprehensive guide on how to update entities and fields in Drupal 8 and later versions. It covers various scenarios such as changing a field type, deleting a field, and updating field storage definitions. Here's a summary of key points:

### General Steps to Update Entities and Fields

1. **Backup**: Always back up your database before making any schema changes.

2. **Create Update Functions**: Use `hook_update_N` in your module to define the update logic.

3. **Schema Version**: Use `drupal_get_installed_schema_version` to check the current schema version of your module.

4. **Set Schema Version**: Use `drupal_set_installed_schema_version` to manually set the schema version if needed.

### Updating a Field Type

1. **Store Existing Values**: Fetch the existing values of the field.
2. **Clear Field Values**: Set the field values to `NULL`.
3. **Uninstall Field Storage**: Uninstall the old field storage.
4. **Create New Field Definition**: Define the new field with the updated type.
5. **Install New Field Storage**: Install the new field storage.
6. **Restore Values**: Restore the original values.

### Deleting a Field

1. **Delete Field Definition**: Remove the field definition from the entity class.
2. **Update Entity Keys**: Remove the field from `entity_keys` in the entity definition if defined.
3. **Uninstall Field Storage**: Uninstall the field storage.
4. **Run Cron**: Run cron to clear the field widget from entity edit pages.

### Example of Changing a Field Type

```php
$database = \Drupal::database();
$transaction = $database->startTransaction();

$entity_type_manager = \Drupal::entityTypeManager();
$bundle_of = 'node';

$storage = $entity_type_manager->getStorage($bundle_of);
$bundle_definition = $entity_type_manager->getDefinition($bundle_of);
$id_key = $bundle_definition->getKey('id');
$table_name = $storage->getDataTable() ?: $storage->getBaseTable();
$definition_manager = \Drupal::entityDefinitionUpdateManager();

// Store the existing values.
$status_values = $database->select($table_name)
  ->fields($table_name, [$id_key, 'status_field'])
  ->execute()
  ->fetchAllKeyed();

// Clear out the values.
$database->update($table_name)
  ->fields(['status_field' => NULL])
  ->execute();

// Uninstall the field.
$field_storage_definition = $definition_manager->getFieldStorageDefinition('status_field', $bundle_of);
$definition_manager->uninstallFieldStorageDefinition($field_storage_definition);

// Create a new field definition.
$new_status_field = BaseFieldDefinition::create('string')
  ->setLabel(t('Status field'))
  ->setDescription(t('The status - either no, yes or skip.'))
  ->setDefaultValue('no')
  ->setRevisionable(FALSE)
  ->setTranslatable(FALSE);

// Install the new definition.
$definition_manager->installFieldStorageDefinition('status_field', $bundle_of, $bundle_of, $new_status_field);

// Restore the values.
$value_map = [
  '1' => 'yes',
  '0' => 'no',
];
foreach ($status_values as $id => $value) {
  $database->update($table_name)
    ->fields(['status_field' => $value_map[$value]])
    ->condition($id_key, $id)
    ->execute();
}

// Commit transaction.
unset($transaction);
```

### Example of Deleting a Field

```php
$update_manager = \Drupal::entityDefinitionUpdateManager();
$definition = $update_manager->getFieldStorageDefinition('name_of_old_field_to_delete', 'entity_type');
$update_manager->uninstallFieldStorageDefinition($definition);
```

### Useful Drush Commands

- **Check Current Schema Version**:
  ```bash
  drush php-eval "echo drupal_get_installed_schema_version('my_module');"
  ```
  For Drupal 9+:
  ```bash
  drush php-eval "echo \Drupal::service('update.update_hook_registry')->getInstalledVersion('my_module');"
  ```

- **Set Schema Version**:
  ```bash
  drush php-eval "echo drupal_set_installed_schema_version('my_module', '8000');"
  ```
  For Drupal 9+:
  ```bash
  drush php-eval "\Drupal::service('update.update_hook_registry')->setInstalledVersion('my_module', '9000');"
  ```

These steps and examples should help you effectively update entities and fields in Drupal 8 and later versions.