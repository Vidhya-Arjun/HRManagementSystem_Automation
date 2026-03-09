

HR Management Web Automation (OrangeHRM) – Selenium + Pytest
**Overview**

This project is an end-to-end UI automation framework built using Python, Selenium WebDriver, and Pytest to automate the OrangeHRM demo application.

The framework follows the Page Object Model (POM) design pattern to ensure maintainability, scalability, and reusability of automation code.

It validates major HR workflows such as:

User authentication

User management

Leave assignment

Claim initiation

Profile navigation

Data-driven login validation

The project also supports Excel-based data driven testing and modular page object architecture.

Application Under Test

OrangeHRM Demo

URL used:
https://opensource-demo.orangehrmlive.com


Framework Features
1. Page Object Model (POM)

Each page functionality is encapsulated inside dedicated page classes.

2. Data Driven Testing

Login scenarios are executed using Excel based test data.

Example:

@pytest.mark.parametrize("row, username, password, expected", read_data())

This enables:

Multiple test cases

Valid / invalid credential validation

Easy data maintenance

3. Modular Page Objects

Page modules included:

LoginPage

Handles authentication and dashboard navigation.

LeavePage

Handles employee leave assignment.

ClaimPage

Handles claim creation and expense submission.

UserProfilePage

Handles profile menu validation.

