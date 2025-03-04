Overview

This is a practice automation project for OrangeHRM, built using Selenium WebDriver with the Page Object Model (POM) design pattern. The goal is to enhance test automation skills and understand best practices in organizing automation frameworks.

Technologies Used

Python

Selenium WebDriver

Pytest (for test execution)

pytest-html (for generating reports)

Project Structure

OrangeHRM_Automation/
│-- tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│-- pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│-- utils/
│   ├── config.py
│-- reports/
│-- screenshots/
│-- conftest.py
│-- requirements.txt
│-- README.md

Setup & Installation

Prerequisites:

Install Python (>= 3.x)

Install Google Chrome / Firefox

Install the required dependencies:

pip install -r requirements.txt

Running Tests

Run the tests using pytest:

pytest --html=reports/report.html --self-contained-html

Features Covered

Login functionality

Dashboard validation

UI verification using Selenium

Future Enhancements

Add more test cases (user management, leave module, etc.)

Implement parallel test execution

Integrate with CI/CD pipelines

Author

This project is created as part of Selenium Python practice for learning automation testing with POM.

