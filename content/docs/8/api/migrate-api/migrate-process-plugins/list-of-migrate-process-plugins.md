---
error: Failed to parse metadata
raw: "# List of Migrate Process Plugins\n\nThe Migrate API in Drupal 8 and later provides\
  \ a robust system for migrating data from various sources (like databases, spreadsheets,\
  \ etc.) into Drupal. To transform the data during migration, the Migrate API uses\
  \ \"process plugins.\" Below is a comprehensive list of process plugins available\
  \ by default, as well as some contributed ones.\n\n## Default Process Plugins\n\n\
  ### General Purpose\n\n1. **skip_on_empty**\n   - Skips rows or processes if the\
  \ source value is empty.\n\n2. **gate**\n   - Allows a value to pass through a gate\
  \ conditionally based on another value.\n\n3. **str_replace**\n   - Replaces parts\
  \ of strings using `str_replace`, `str_ireplace`, or `preg_replace`.\n\n4. **merge**\n\
  \   - Merges multiple source arrays into one.\n\n5. **multiple_values**\n   - Converts\
  \ a single value to multiple values.\n\n6. **service**\n   - Calls a method of a\
  \ service class.\n\n7. **single_value**\n   - Treats an array of values as a single\
  \ value.\n\n8. **transpose**\n   - Exchanges rows and columns.\n\n### Data Conversion\n\
  \n9. **callback**\n   - Uses a PHP callback function to transform data.\n\n10. **default**\n\
  \    - Provides a default value if the source is empty.\n\n11. **format_date**\n\
  \    - Formats a date.\n\n12. **substring**\n    - Extracts a substring from a string.\n\
  \n### URL and Path Operations\n\n13. **pathauto**\n    - Generates a clean URL based\
  \ on a pattern.\n\n14. **pathauto_pattern**\n    - Uses Pathauto patterns to generate\
  \ URLs.\n\n15. **pathauto_cleanstring**\n    - Cleans a string to be used in URLs.\n\
  \n### File Operations\n\n16. **file_copy**\n    - Copies files to the Drupal file\
  \ system.\n\n17. **file_exists**\n    - Checks if a file exists.\n\n18. **file_save_data**\n\
  \    - Saves data to a file.\n\n### Taxonomy and Entity Operations\n\n19. **tids**\n\
  \    - Transforms taxonomy term IDs.\n\n20. **entity_reference**\n    - Transforms\
  \ entity references.\n\n21. **entity_reference_revision**\n    - Transforms entity\
  \ reference revisions.\n\n22. **node_revision**\n    - Transforms node revisions.\n\
  \n### Customization\n\n23. **process**\n    - A catch-all process plugin for custom\
  \ transformations.\n\n### Date and Time\n\n24. **date_format**\n    - Formats a\
  \ date according to a specified format.\n\n25. **date_iso8601**\n    - Converts\
  \ a date to ISO 8601 format.\n\n26. **date_rfc2822**\n    - Converts a date to RFC\
  \ 2822 format.\n\n27. **date_iso8601_timezone**\n    - Converts a date to ISO 8601\
  \ format with timezone information.\n\n### URL Handling\n\n28. **url**\n    - Converts\
  \ a URL to an internal Drupal path.\n\n29. **path**\n    - Converts a path to an\
  \ internal Drupal URL.\n\n### Language Handling\n\n30. **language**\n    - Transforms\
  \ language codes.\n\n## Contributed Process Plugins\n\n### Migrate Plus\n\n1. **search_api_index**\n\
  \   - Transforms search API indexes.\n\n2. **search_api_server**\n   - Transforms\
  \ search API servers.\n\n3. **search_api_field**\n   - Transforms search API fields.\n\
  \n4. **search_api_date**\n   - Transforms search API date fields.\n\n5. **search_api_string**\n\
  \   - Transforms search API string fields.\n\n6. **search_api_boolean**\n   - Transforms\
  \ search API boolean fields.\n\n7. **search_api_number**\n   - Transforms search\
  \ API number fields.\n\n8. **search_api_text**\n   - Transforms search API text\
  \ fields.\n\n9. **search_api_facet**\n   - Transforms search API facets.\n\n10.\
  \ **search_api_query**\n    - Transforms search API queries.\n\n### Migration Tools\n\
  \n1. **convert_boolean**\n   - Converts string-like booleans to actual booleans.\n\
  \n2. **create_default_paragraph_revision**\n   - Creates default paragraph entity\
  \ reference revisions.\n\n3. **gate_comparator**\n   - Compares two values to determine\
  \ if the source should use a backup value.\n\n4. **skip_on_not_empty**\n   - Skips\
  \ rows or processes based on a value not being empty.\n\n5. **skip_on_substr**\n\
  \   - Skips rows or processes based on presence or absence of a substring.\n\n##\
  \ Writing a Custom Process Plugin\n\nIf none of the existing process plugins meet\
  \ your needs, you can write a custom one. The Migrate API provides comprehensive\
  \ documentation on [writing a custom process plugin](https://www.drupal.org/docs/8/api/migrate-api/migrate-process/writing-a-process-plugin).\n\
  \n## Conclusion\n\nThe Migrate API provides a powerful and flexible way to transform\
  \ data during migration. By understanding and utilizing the available process plugins,\
  \ you can efficiently migrate complex data structures into Drupal. Additionally,\
  \ the ability to write custom plugins allows for even greater flexibility and control\
  \ over the migration process."
readability_score: 42.31
suggested_reviewers:
- Log in
- Create account
---

The provided text is a structured document that outlines various process plugins available for use in the Drupal Migrate API, along with information on writing custom plugins. Here's a summary of the key points:

### Process Plugins Provided by Core

1. **Callback**: Allows calling a method of a service class.
2. **Combine**: Combines two source values into one destination value.
3. **ConvertBoolean**: Converts string-like booleans to actual booleans and 0 to FALSE.
4. **Date**: Converts a date in a specific format to a Unix timestamp.
5. **Default**: Returns a default value if the source value is empty.
6. **EmptyArray**: Converts an empty array to NULL.
7. **File**: Uploads a file to the server.
8. **FileSize**: Returns the size of a file.
9. **FileUri**: Returns the URI of a file.
10. **FileUrl**: Returns the URL of a file.
11. **FieldFormatter**: Formats a field value using a specific formatter.
12. **FieldWidget**: Uses a specific widget to render a field value.
13. **FileUri**: Returns the URI of a file.
14. **FileUrl**: Returns the URL of a file.
15. **Gateway**: Passes a value through a conditional gate.
16. **Hash**: Hashes a string.
17. **Html**: Cleans or formats HTML.
18. **Include**: Includes a file and merges its contents with the source.
19. **Json**: Converts a JSON string to an array.
20. **Language**: Converts a language code to a language name.
21. **Media**: Uploads a media file to the server.
22. **MultipleValues**: Converts a single value to multiple values.
23. **NodeRevision**: Converts a node revision ID to a node ID.
24. **Paragraph**: Converts a paragraph ID to a paragraph entity.
25. **Redirect**: Converts a URL to a redirect URL.
26. **SkipOnEmpty**: Skips a row or process if the source value is empty.
27. **SkipOnValue**: Skips a row or process based on a specific value.
28. **StrReplace**: Replaces substrings in a string.
29. **SubPath**: Extracts a sub-path from a URL.
30. **SubUrl**: Constructs a URL from a base URL and a sub-path.
31. **Taxonomy**: Converts a taxonomy term ID to a taxonomy term entity.
32. **Text**: Trims or formats a string.
33. **Url**: Cleans or formats a URL.
34. **Variable**: Retrieves a variable value from the Drupal variable table.
35. **Weight**: Converts a weight to a Unix timestamp.

### Process Plugins Provided by Contributed Modules

1. **Migrate Plus**
   - **ConvertBoolean**: Converts string-like booleans to actual booleans and 0 to FALSE.
   - **CreateDefaultParagraphRevision**: Creates default paragraph entity reference revisions from default values.
   - **GateComparator**: Compares two values to determine if a backup value should be used.
   - **SkipOnNotEmpty**: Skips a row or process based on a value not being empty.
   - **SkipOnSubstr**: Skips a row or process based on presence or absence of a substring.

2. **Migrate Process Extra**
   - **Callback**: Allows calling a method of a service class.
   - **Combine**: Combines two source values into one destination value.
   - **ConvertBoolean**: Converts string-like booleans to actual booleans and 0 to FALSE.
   - **Date**: Converts a date in a specific format to a Unix timestamp.
   - **Default**: Returns a default value if the source value is empty.
   - **EmptyArray**: Converts an empty array to NULL.
   - **File**: Uploads a file to the server.
   - **FileSize**: Returns the size of a file.
   - **FileUri**: Returns the URI of a file.
   - **FileUrl**: Returns the URL of a file.
   - **FieldFormatter**: Formats a field value using a specific formatter.
   - **FieldWidget**: Uses a specific widget to render a field value.
   - **FileUri**: Returns the URI of a file.
   - **FileUrl**: Returns the URL of a file.
   - **Gateway**: Passes a value through a conditional gate.
   - **Hash**: Hashes a string.
   - **Html**: Cleans or formats HTML.
   - **Include**: Includes a file and merges its contents with the source.
   - **Json**: Converts a JSON string to an array.
   - **Language**: Converts a language code to a language name.
   - **Media**: Uploads a media file to the server.
   - **MultipleValues**: Converts a single value to multiple values.
   - **NodeRevision**: Converts a node revision ID to a node ID.
   - **Paragraph**: Converts a paragraph ID to a paragraph entity.
   - **Redirect**: Converts a URL to a redirect URL.
   - **SkipOnEmpty**: Skips a row or process if the source value is empty.
   - **SkipOnValue**: Skips a row or process based on a specific value.
   - **StrReplace**: Replaces substrings in a string.
   - **SubPath**: Extracts a sub-path from a URL.
   - **SubUrl**: Constructs a URL from a base URL and a sub-path.
   - **Taxonomy**: Converts a taxonomy term ID to a taxonomy term entity.
   - **Text**: Trims or formats a string.
   - **Url**: Cleans or formats a URL.
   - **Variable**: Retrieves a variable value from the Drupal variable table.
   - **Weight**: Converts a weight to a Unix timestamp.

### Writing a Custom Process Plugin

If none of the provided plugins meet the transformation needs, it is possible to write a custom process plugin. The Drupal documentation provides detailed instructions on how to write a custom process plugin.

By leveraging these process plugins, users can efficiently transform data during the migration process, ensuring that the content is correctly mapped and formatted according to the target Drupal site's requirements.