---
author: null
drupal_version: null
last_updated: 25 April 2025
readability_score: 49.63
source_url: /docs/extending-drupal/uninstalling-modules
suggested_reviewers:
- Log in
- Create account
summary: 'In order to uninstall the module, be sure that the module is not being used
  on your site so that it does not impact any functionality. The full process will
  require 2 steps: uninstall and remove your module folder. You can use either the
  Drush or the Administrative Interface to uninstall modules.'
tags:
- uninstalling
- modules
- drush
- administrative interface
- composer
themes: null
title: Uninstalling Modules
---

# Uninstalling Modules

In order to uninstall the module, be sure that the module is not being used on your site so that it does not impact any functionality. The full process will require 2 steps: uninstall and remove your module folder. You can use either the Drush or the Administrative Interface to uninstall modules.

## Using Drush

Pre-requisite: Drush should be installed on your machine. To install Drush check [How to install Drush](https://www.drupal.org/node/1791676).

Run the following Drush command to uninstall the module:
```php
drush pm-uninstall module_name
```

Or use the Drush alias:
```php
drush pmu module_name
```

Next, clear cache using the Drush command:
```php
drush cr
```

That's it. The uninstalled module will no longer show as checked in the module list and the functionality of the module will have been removed from the site.

## Using the Administrative Interface

1. In the **Manage** administrative menu, navigate to **Extend** > **Uninstall** tab (`admin/modules/uninstall`) where you will find the list of enabled modules that are ready to be uninstalled.
2. You can search or filter for the module to be uninstalled by typing the module name in the search field.
3. Check the box/boxes of modules that you want to uninstall.
4. Click the **Uninstall button** at the bottom of the page.
5. Step 4 will prompt you to confirm the module uninstall request.
6. Click **Uninstall**.
7. Go to the link `manage>configuration>development>performance` click on `clear all cache.`

The functionality of the uninstalled module will now have been removed from the site. If you are sure you won't need the module any more you can remove the module folder from your server. This can be done on different ways depending on your set up. Most commonly can be done with composer or manually; make sure you don't have composer manager and look for your hosting provider instructions for manually removing files.

## Using composer

Having uninstalled the module, you can then remove the module code from your server using composer. Be sure to uninstall via the admin interface or by using Drush before removing the codebase.

Run `composer remove drupal/module`

References to this module in composer.json and composer.lock should be removed, as well as the folder in the directory path (e.g. in /modules/contrib/)

Verify in /admin/modules/ module had been removed (it should not show the module available for install.)

If for some reason, module folder gets retained in the /modules/contrib directory, you may now safely delete it now, e.g. running `rm -rf module_name` from that directory

Run the usual `update.php`, `drush updb`, `drush cache:rebuild`, etc. to clean-up and flush system

In case you are working on a workflow with more than one environment (including you local) you should consider uninstall your module in production before you remove it from composer. Otherwise you may not be able to uninstall and you will end up with errors on your database. [Refer to Managing your site’s configuration](https://www.drupal.org/docs/administering-a-drupal-site/configuration-management/managing-your-sites-configuration)

Refer also to [https://www.drupal.org/forum/support/post-installation/2022-03-04/uninstall-modules-that-were-installed-with-composer](https://www.drupal.org/forum/support/post-installation/2022-03-04/uninstall-modules-that-were-installed-with-composer)

## Related Content

- [4.4. Uninstalling Unused Modules](/docs/user_guide/en/config-uninstall.html)

**Help improve this page**

Page status: Needs work

You can:
- Log in, click **Edit**, and edit this page
- Log in, click **Discuss**, update the Page status value, and suggest an improvement
- Log in and [create a Documentation issue](/node/add/project-issue/documentation?title=Suggestion%20for%3A%20%282845604%29%20Uninstalling%20Modules) with your suggestion