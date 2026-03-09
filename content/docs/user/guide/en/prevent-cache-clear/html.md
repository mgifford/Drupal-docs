---
page:
  description: This page provides instructions on how to clear and rebuild caches
    in a Drupal site using Drush, the rebuild script, or through the Drush command
    line interface.
  sections:
  - content: The goal of this page is to provide clear and concise instructions on
      how to clear and rebuild caches in a Drupal site using various methods.
    title: Goal
  - content: Before proceeding with the instructions, ensure that you have Drush installed
      and that you have administrative access to your Drupal site.
    title: Prerequisites
  - content:
    - content:
      - content: Run the command `drush cache:rebuild`. This will clear and rebuild
          all cached data for the site.
        title: 'Command 1: Clear and Rebuild All Cached Data'
      - content: Run the command `drush cache:clear`. This will display a list of
          individual caches, and you can choose the specific cache to clear.
        title: 'Command 2: Clear Individual Caches'
      - content: You can specify a specific cache type in the `drush cache:clear`
          command. For example, to clear the render cache, use the command `drush
          cache:clear render`.
        title: Clearing a Specific Cache Type
      title: Using Drush
    - content:
      - content: Open `settings.php` and add the line `$settings['rebuild_access']
          = TRUE;` to the end of the file.
        title: Adding the Rebuild Access Setting
      - content: Visit `http://www.example.com/core/rebuild.php` in your browser to
          clear the cache and rebuild the site.
        title: Running the Rebuild Script
      - content: After the rebuild is complete, remove the line `$settings['rebuild_access']
          = TRUE;` from `settings.php`.
        title: Removing the Rebuild Access Setting
      title: Using the Rebuild Script
    title: Instructions
  - content:
    - content: 'Video URL: https://www.youtube-nocookie.com/embed/-evRieC6Y3U'
      title: Video Title
    title: Videos
  - content:
    - content: https://www.drupal.org/docs/7/administering-drupal-7-site/clearing-or-rebuilding-drupals-cache
      title: Drupal.org Documentation
    title: Additional Resources
  title: 12.2. Clearing the Cache
readability_score: 67.19
suggested_reviewers:
- Log in
- Create account
---

# Clearing the Cache

Clearing the cache is a common task when managing a Drupal site, as it ensures that your site displays the most up-to-date content and functionality. This guide will walk you through different methods to clear and rebuild the cache using both the Drupal administrative interface and the command line tool, Drush.

## Goal
By the end of this guide, you will be able to:
- Clear and rebuild the cache using the Drupal administrative interface.
- Use the rebuild script to clear and rebuild the cache.
- Use Drush to clear and rebuild the cache.

## Prerequisites
- A Drupal site up and running.
- Access to the server where the Drupal site is hosted.
- Administrative privileges for the Drupal site.

## Clearing and Rebuilding Cache

### Using the Drupal Administrative Interface
1. **Log in to your Drupal site as an administrator.**
2. **Navigate to the `Performance` section.**
   - Click on `Configuration` in the main menu.
   - Select `Development` and then `Performance`.
3. **Clear the cache.**
   - Click on the `Clear all caches` button at the top of the page.
   - Confirm the action by clicking `Yes`.

### Using the Rebuild Script
The rebuild script provides a quick way to clear and rebuild the cache programmatically.

1. **Edit the `settings.php` file.**
   - Locate the `settings.php` file in your Drupal installation, typically located at `/sites/default/settings.php`.
   - Open the file in a plain text editor.
   - Add the following line to the end of the file and save the changes:
     ```php
     $settings['rebuild_access'] = TRUE;
     ```
2. **Run the rebuild script.**
   - Open your web browser and navigate to `http://www.example.com/core/rebuild.php` (replace `www.example.com` with your actual domain).
   - After a short pause, you should be redirected to the home page of your site, and the cache should be rebuilt.
3. **Remove the line from `settings.php`.**
   - Open the `settings.php` file again.
   - Find the line you added with `$settings['rebuild_access']`.
   - Remove this line and save the file.

### Using Drush
Drush is a command-line shell and scripting interface for Drupal. It provides a wide range of commands to manage your Drupal site.

1. **Install Drush if it is not already installed.**
   - Follow the instructions on the [Drush installation page](https://www.drupal.org/project/drush) to install Drush.
2. **Clear the cache using Drush.**
   - Open your terminal or command prompt.
   - Run the following command to clear all caches:
     ```bash
     drush cache:rebuild
     ```
   - You should see the output message "Cache rebuild complete."
3. **Clear a specific cache type using Drush.**
   - Run the following command to clear a specific cache type, for example, the render cache:
     ```bash
     drush cache:clear render
     ```

## Videos
- [Clearing the Cache](https://www.youtube-nocookie.com/embed/-evRieC6Y3U)

## Additional Resources
- [Drupal.org Community Documentation Page: Clearing or Rebuilding Drupal's Cache](https://www.drupal.org/docs/7/administering-drupal-7-site/clearing-or-rebuilding-drupals-cache)

## Attributions
This guide is adapted and edited by Joe Shindelar and Jack Haas from [Clearing or Rebuilding Drupal’s Cache](https://www.drupal.org/docs/7/administering-drupal-7-site/clearing-or-rebuilding-drupals-cache), copyright 2000-2025 by the individual contributors to the Drupal Community Documentation.

---

**Note:** Always ensure you have backups of your site before performing cache operations, especially if you are not familiar with the process.