---
author: null
drupal_version: '8'
last_updated: null
readability_score: 6.23
source_url: /docs/drupal-apis/update-api
suggested_reviewers:
- Log in
- Create account
summary: This guide is about the Update API, which allows modules to provide code
  that will update their data models between minor versions and releases within one
  major version (that is, between different software/data versions all within Drupal
  8).
tags:
- Drupal APIs
- Update API
- Drupal 8
themes: null
title: Update API
---

# Update API

This guide is about the Update API, which allows modules to provide code that will update their data models between minor versions and releases within one major version (that is, between different software/data versions all within Drupal 8).

## Introduction to the Update API for Drupal 8

Introduction to the Update API for Drupal 8.

## Updating Configuration

If your module is making a data model change related to configuration, then you need to properly update your data model. The three steps are

## Updating Database Schema and/or Data in Drupal

How to update your data model if making changes to the database schema.

## Updating Entities and Fields in Drupal 8

How to write update functions handling field/entity type definition changes affecting schema

## Writing Automated Update Tests for Drupal 8 (or later)

If your module is making a data model change related to configuration, then you need to properly update your data model (as described on