# Mist API  Checker

This repository contains a small Python utility used to validate authentication and connectivity to the Mist API.

# Overview

The tool performs a simple request to the /self endpoint to confirm that API access is functioning and to identify the account associated with the API token.

A successful response verifies that the token is valid, permissions are sufficient, and the API is reachable.

# Functionality

Sends an authenticated request to the Mist API

Queries the /self endpoint

Returns basic identity information for the authenticated account

# Use Case

Intended as a quick validation step before performing additional API operations or automation.
