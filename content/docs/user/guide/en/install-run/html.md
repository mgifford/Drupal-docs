---
error: Failed to parse metadata
raw: "The text you provided is a detailed guide on how to install Drupal using the\
  \ interactive installer. Here's a summary of the key points:\n\n1. **Objective**:\
  \ The guide aims to help users understand and complete the process of installing\
  \ Drupal using the interactive installer.\n\n2. **Prerequisites**: Before starting\
  \ the installation, it's recommended to have administrative access to the server\
  \ where Drupal will be installed. Additionally, having a database set up for Drupal\
  \ is necessary.\n\n3. **Installation Process**:\n   - **Database Setup**: Ensure\
  \ that a database is created and accessible.\n   - **Download Drupal**: Obtain the\
  \ Drupal installation package from the official Drupal website or through Composer.\n\
  \   - **Upload Files**: Transfer the downloaded Drupal files to the server's web\
  \ root directory.\n   - **Run the Installer**: Navigate to the Drupal installation\
  \ URL in a web browser and follow the on-screen instructions to complete the installation.\n\
  \   - **Configure Settings**: During the installation, you will be prompted to configure\
  \ settings such as site name, email, and database credentials.\n   - **Final Steps**:\
  \ After completing the installation, verify that the installation was successful\
  \ and address any warnings or errors.\n\n4. **Alternative Method**: The guide also\
  \ provides an alternative method to install Drupal using Drush, a command-line shell\
  \ and scripting interface for Drupal.\n\n5. **Additional Resources**: The guide\
  \ includes links to additional resources and documentation for further learning\
  \ and troubleshooting.\n\n6. **Attributions**: The content is attributed to Joe\
  \ Shindelar and Jojy Alphonso, and it's part of the Drupal community documentation.\n\
  \nThis guide is comprehensive and serves as a step-by-step manual for users looking\
  \ to set up a new Drupal site either through the web-based installer or using Drush."
readability_score: 51.28
suggested_reviewers:
- Log in
- Create account
---

### 3.7. Running the Interactive Installer

Running the Interactive Installer is a straightforward process that guides you through the steps necessary to install Drupal on your server. Below is a detailed step-by-step guide to help you through the process using both the User Interface (UI) and Drush.

#### Using the User Interface (UI)

1. **Download the Drupal Software**:
   - Download the latest version of Drupal from the official Drupal website.
   - Extract the downloaded archive to a directory on your server where you want to install Drupal.

2. **Create a Database**:
   - Log in to your database management system (e.g., phpMyAdmin, MySQL Workbench).
   - Create a new database for Drupal.

3. **Configure File Permissions**:
   - Ensure that the `sites/default` directory and the `sites/default/settings.php` file have the correct permissions. Typically, these should be set to 755 (read and execute for the owner, read for the group and others) and 644 (read and write for the owner, read for the group and others).

4. **Run the Installer**:
   - Navigate to the root directory of your Drupal installation in your web browser.
   - You should see a page that prompts you to run the installer.
   - Follow the on-screen instructions to complete the installation. This includes:
     - **Database Configuration**: Enter your database name, username, and password.
     - **Site Information**: Provide details about your site, such as the site name and email address.
     - **Account Information**: Create an account for the Drupal administrative user.

5. **Verify Installation**:
   - After completing the installation, you should be redirected to the front page of your new Drupal site.
   - You should see a message indicating that Drupal has been successfully installed.

6. **Resolve File Permissions Warning**:
   - If you encounter a warning about file permissions, ensure that the `sites/default` directory and the `sites/default/settings.php` file are set to 755 and 644, respectively.

#### Using Drush

If you prefer to use Drush for the installation, follow these steps:

1. **Install Drush**:
   - Ensure Drush is installed on your server. You can install it globally using Composer:
     ```sh
     composer global require drush/drush
     ```

2. **Navigate to Drupal Directory**:
   - Open a terminal and navigate to the directory where you downloaded the Drupal software.

3. **Run the Installation Command**:
   - Use the following Drush command to install Drupal:
     ```sh
     drush site:install standard --db-url='mysql://DB_USER:DB_PASS@localhost/DB_NAME' --site-name=example
     ```
   - Replace `DB_USER`, `DB_PASS`, and `DB_NAME` with your database credentials and the desired site name.

4. **Verify Installation**:
   - After running the command, check the output for any errors.
   - If there are no errors, your Drupal installation should be complete.

5. **Access the Front Page**:
   - Open your web browser and navigate to the front page of your new Drupal site.
   - Verify that the site is running correctly.

### Expand Your Understanding

- **Development Sites**: Learn about setting up development environments for Drupal.
- **Additional Tools**: Explore other tools and resources that can enhance your Drupal development workflow.

### Videos

- **Running the Installer**: Watch a video tutorial on how to run the Interactive Installer.

### Additional Resources

- **Drupal.org Community Documentation**:
  - [Create a Database](https://www.drupal.org/docs/installing-drupal/step-3-create-a-database)
  - [Webhosting Issues](https://www.drupal.org/server-permissions)

Feel free to reach out if you have any questions or need further assistance!