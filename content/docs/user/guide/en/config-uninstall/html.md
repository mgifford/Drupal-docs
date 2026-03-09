---
error: Failed to parse metadata
raw: '### Key Points from the Provided Text:


  #### Title and Content:

  - The title of the document is "4.4. Uninstalling Unused Modules".

  - The content discusses how to uninstall unused modules in a Drupal site.


  #### Table of Contents:

  - The document covers methods for uninstalling modules using the Drupal administrative
  interface and Drush.


  #### Method 1: Using the Drupal Administrative Interface:

  1. Navigate to `admin/modules/uninstall`.

  2. Check the boxes for the modules you want to uninstall.

  3. Click "Uninstall" at the bottom of the page.

  4. Confirm the uninstallation request.


  #### Method 2: Using Drush:

  1. Navigate to `admin/modules`.

  2. Find the machine name of the module you want to uninstall.

  3. Run the command `drush pm:uninstall <module_machine_name>`.


  #### Notes:

  - A module cannot be uninstalled if it is required by other modules or functionality.

  - The core File module is required by Text Editor, CKEditor, and Image modules and
  cannot be uninstalled unless their dependencies are also removed.


  #### Additional Resources:

  - The document includes a link to a video tutorial on YouTube for further guidance.

  - It also provides suggestions for improving the documentation.


  #### Contact Information:

  - The documentation is maintained by Joe Shindelar, Surendra Mohan, and Jojy Alphonso
  from Drupalize.Me and Red Crackle.


  #### Source Information:

  - The document is based on an AsciiDoc source file and is part of the User Guide
  project. PDF and e-book formats are available on the project page.


  #### Improvements:

  - Users can edit the source, discuss improvements, or create a Documentation issue
  on the project page.


  ### Summary:

  The document provides detailed instructions on how to uninstall unused modules in
  a Drupal site using both the administrative interface and Drush, along with additional
  resources and support for improvement.'
readability_score: 51.47
suggested_reviewers:
- Log in
- Create account
---

The provided text is a detailed guide on how to uninstall unused modules in a Drupal site. It covers both the administrative interface (using the "Extend" page) and the command-line interface (using Drush). The guide includes step-by-step instructions for checking and unchecking modules, confirming the uninstallation, and provides a video tutorial for visual learners. Additionally, it mentions related resources such as how to use additional tools and clear the cache, and suggests expanding knowledge by uninstalling other core modules like the Comment module. The page is structured with navigation links for previous and next sections and includes a feedback section for users to suggest improvements.