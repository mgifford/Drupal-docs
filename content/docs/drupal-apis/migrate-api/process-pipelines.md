---
error: Failed to parse metadata
raw: 'The provided text is a detailed guide on how to use process plugins in Drupal''s
  Migrate and Migrate Plus modules. It covers a wide range of scenarios and provides
  examples on how to achieve specific tasks such as:


  1. Handling null values and defaulting to fallback values.

  2. Creating readable labels for stubbed entities.

  3. Skipping processes or rows based on conditions.

  4. Using custom callback functions.

  5. Concatenating and manipulating data.

  6. Using static maps for value transformations.

  7. Handling multi-value fields.

  8. Dealing with date and time conversions.

  9. Using external data sources.

  10. Creating complex process pipelines.


  The guide is organized into sections, each focusing on a specific aspect of Migrate
  process plugins. It includes detailed explanations, code examples, and use cases,
  making it a comprehensive resource for developers working with Drupal migrations.


  The text also mentions related content and encourages users to contribute to improve
  the documentation. This approach ensures that the guide remains up-to-date and relevant
  to the Drupal community.'
readability_score: 41.05
suggested_reviewers:
- Log in
- Create account
---

Based on the provided content, here are some key points about Migrate process plugins:

1. Core Migrate provides several built-in process plugins like:
   - get
   - concat
   - null_coalesce
   - skip_on_empty
   - migrate_lookup
   - migration_lookup
   - migration_group_lookup
   - static_map
   - callback
   - entity_lookup
   - entity_generate

2. Migrate Plus provides additional plugins like:
   - entity_autopopulate
   - entity_transform
   - entity_count
   - entity_subform
   - entity_subform_element
   - entity_subform_group
   - entity_subform_item
   - entity_subform_property
   - entity_subform_widget
   - entity_subform_wrapper

3. Contributed modules like Migrate Conditions provide:
   - skip_on_condition
   - skip_on_value
   - skip_on_length
   - skip_on_type
   - skip_on_not_empty

4. Key features of Migrate process plugins:
   - Transforming and manipulating data during migration
   - Handling complex data structures and relationships
   - Providing fallback values and default behavior
   - Enabling conditional logic and skipping processes

5. Common use cases include:
   - Converting data formats
   - Joining related data
   - Generating fallback values
   - Applying conditional transformations

6. Plugins can be chained together to create complex data processing pipelines.

7. Documentation and examples are available for each plugin type to help with implementation.

Overall, Migrate process plugins provide powerful tools for customizing data migration processes in Drupal, allowing for flexible and complex data handling during migration.