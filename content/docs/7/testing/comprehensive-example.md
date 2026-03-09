---
author: ''
drupal_version: '7'
last_updated: 1 December 2016
readability_score: 59.96
source_url: http://www.example.com/docs/7/testing/comprehensive-example
suggested_reviewers:
- Log in
- Create account
summary: This article provides a comprehensive example of how to write a browser test
  for Drupal 7 using SimpleTest.
tags:
- Drupal 7
- Automated Testing
- Browser Testing
themes: []
title: Comprehensive example
---

# Comprehensive example

**Last updated on 1 December 2016**

**Deprecated**: Drupal 7 will no longer be supported after January 5, 2025. [Learn more and find resources for Drupal 7 sites](/about/drupal-7/d7eol/partners)

Now it's time to try a browser test. We don't have to change too much in our class, because `DrupalWebTestCase` class contains tools for both tests.

We would like to check Drupal's response when specifying an invalid email address in the registration form (user/register). Let's look into the source:

```php
<div class="form-item">
 <label for="edit-name">Username:</label><span class="form-required">*</span><br>
 <input maxlength="64" class="form-text required" name="edit[name]" id="edit-name" size="30" value="" type="text">
 <div class="description">Your full name or your preferred username; only letters, numbers and spaces are allowed.</div>
</div>
<div class="form-item">
 <label for="edit-mail">E-mail address:</label><span class="form-required">*</span><br>
 <input maxlength="64" class="form-text required" name="edit[mail]" id="edit-mail" size="30" value="" type="text">
 <div class="description">A password and instructions will be sent to this e-mail address, so make sure it is accurate.</div>
</div>
```

It is important to notice the name of fields in which we want to put data. There are two of them: edit[name] and edit[mail].

We begin with the same thing everytime:

```php
class OurSecondTest extends DrupalTestCase {
 // we need this function to notify the world about our great test 
 function getInfo() {
    // Note: getInfo() strings are not translated.
    return array(
      'name' => 'Be a browser',
      'desc' => "This tests the browser's response on invalid mail input in the registration process.",
      'group' => 'Example tests',
    );
  }
```

Then we write our test function:

```php
function testBrowserResponse() {
    // let's create a random name and email
    $name = $this->randomName(10);
    $mail = $this->randomName(10);
    // Try to register
    $edit = array('name' => $name, 'mail' => $mail);
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $expectation = t('The e-mail address %mail is not valid.', array('%mail' => $mail));
    // Note: Assertion messages are not translated.
    $this->assertText($expectation, 'The response to an invalid e-mail address was correct');
}
```

Let's look at each line individually:

```php
$name = $this->randomName(10); 
```

This line creates a 10 character random string, which is by default prefixed with 'simpletest_'.

Example: `simpletest_XK3sKW5lFx`

```php
$edit = array('name' => $name, 'mail' => $mail);
$this->drupalPost('user/register', $edit, t('Create new account'));
```

In these two lines, we prepare and send data to our form.

We run `drupalPost` with the following parameters:

1. The path to our form (e.g. 'user/register'). We don't use ?q=, or the whole address `http://www.example.com/?q=user/register`, because this function creates the proper address for us.
2. Array of sent data. Look at the special construction of this array ( => ). We just use the form field names in brackets from above: 'name' and 'mail'. The rest is done by this function.
3. The name of the button which we have to click to send our form. In our example it is: `t('Create new account')`.

```php
$expectation = t('The e-mail address %mail is not valid.', array('%mail' => $mail));
```

We prepare our expectation using `t()` function. We took this from `user.module`.

```php
$this->assertText($expectation, 'The response to an invalid e-mail address was correct');
```

At last we check if our expectation appears on the content page. Note that the second argument to `assertText()` is the message that will appear on the test page, and this should not be translated.

When we run this test we should receive the following output:

```php
Example tests
1/1 test cases complete: 5 passes, 0 fails and 0 exceptions
```

If you look closely, you notice that we have 5 passes in the result, but in the test code we only have one check (using `assertWantedText`). Where is the rest hidden?

The answer is: `$this->drupalPost('user/register', $edit, t('Create new account'));`

If we don't specify the 4th parameter in the `drupalPost` function we will have additional checking. In our example it is:

1. checking if url is valid
2. checking if data was inserted in form's fields
3. checking if we clicked our button

And that's why we have 1 + 4 = 5 passes. If you need to avoid this, give the 4th parameter the value 0.