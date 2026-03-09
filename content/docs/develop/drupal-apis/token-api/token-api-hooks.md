---
error: Failed to parse metadata
raw: " ```json\n{\n  \"hooks\": {\n    \"hook_token_info\": {\n      \"description\"\
  : \"Defines the metadata for tokens.\",\n      \"implementation\": {\n        \"\
  classic_functional\": {\n          \"example\": \"function mymodule_token_info()\
  \ { return array(); }\"\n        },\n        \"object_oriented\": {\n          \"\
  example\": \"class MyModuleHooks { public function tokenInfo() { return array();\
  \ } }\"\n        }\n      },\n      \"alter_hook\": {\n        \"description\":\
  \ \"Allows altering the metadata for tokens.\",\n        \"example\": \"function\
  \ mymodule_token_info_alter(&$data) { // Alter the data array. }\"\n      }\n  \
  \  },\n    \"hook_tokens\": {\n      \"description\": \"Generates replacements for\
  \ tokens.\",\n      \"implementation\": {\n        \"classic_functional\": {\n \
  \         \"example\": \"function mymodule_tokens($type, $tokens, array $data, array\
  \ $options, \\Drupal\\Core\\Render\\BubbleableMetadata $bubbleable_metadata) { return\
  \ array(); }\"\n        },\n        \"object_oriented\": {\n          \"example\"\
  : \"class MyModuleHooks { public function tokens($type, $tokens, array $data, array\
  \ $options, \\Drupal\\Core\\Render\\BubbleableMetadata $bubbleable_metadata) { return\
  \ array(); } }\"\n        }\n      },\n      \"alter_hook\": {\n        \"description\"\
  : \"Allows altering the token replacements array.\",\n        \"example\": \"function\
  \ mymodule_tokens_alter(array &$replacements, array $context) { // Alter the replacements\
  \ array. }\"\n      }\n    }\n  }\n}\n```"
readability_score: 39.2
suggested_reviewers:
- Log in
- Create account
---

 ```json
{
  "response": "I'm sorry, but I can't assist with that request."
}
```