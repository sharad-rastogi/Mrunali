
# SauceDemo Playwright Automation Framework

## Project Overview

This project contains UI automation tests for the SauceDemo application using Python, Playwright, and Pytest.

The framework follows the Page Object Model (POM) design pattern and supports parallel execution, test reporting, and failure debugging.

Application: https://www.saucedemo.com

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-xdist
- Pytest-HTML
- JUnit XML

## Project Structure

```text
SauceDemo_Playwright_Automation/
├── pages/
├── tests/
├── reports/
├── sample-reports/
├── test-results/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.ps1
├── azure-pipelines.yml
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd SauceDemo_Playwright_Automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browser

```bash
python -m playwright install chromium
```

## Test Execution

### Run all tests

```bash
pytest tests
```

### Run a single test file

```bash
pytest tests/test_login.py
```

### Run smoke tests

```bash
pytest -m smoke
```

### Run regression tests

```bash
pytest -m regression
```

### Run tests in parallel and generate reports

Windows PowerShell:

```powershell
.\run_tests.ps1
```

## Framework Design

### Page Object Model

Each application page has a separate Python class.

- LoginPage: Login actions and error messages.
- InventoryPage: Product listing, sorting, and cart actions.
- CartPage: Cart operations.
- CheckoutPage: Checkout form and order summary.

### Pytest Fixtures

Page objects are provided through fixtures in `conftest.py`.

### Session Reuse

The framework creates an authenticated browser storage state for tests that do not test login functionality.

Login tests use a fresh unauthenticated browser context.

### Wait Strategy

Playwright auto-waiting and web-first assertions are used instead of hard-coded sleeps.

### Test Data

Application URL and credentials are configurable through pytest configuration and command-line/environment options.

## Reporting and Debugging

- JUnit XML: reports/junit.xml
- HTML report: reports/report.html
- Failure screenshots, traces, and videos: test-results/

Failure artifacts are configured to be retained only when tests fail.

## CI/CD Pipeline

The Azure DevOps pipeline:

1. Sets up Python.
2. Installs dependencies.
3. Installs Playwright Chromium.
4. Executes tests in parallel.
5. Publishes JUnit results.
6. Publishes HTML reports and failure artifacts.

## Assumptions

- The assignment uses the SauceDemo application.
- The default browser is Chromium.
- Tests use the standard_user account except for negative login scenarios.
- The suite focuses on UI automation; API testing is outside the assignment scope.

## Future Improvements

- Add Firefox and WebKit coverage.
- Add cross-browser CI matrix execution.
- Integrate Allure reporting.
- Add Docker support.
- Expand test coverage for additional checkout and inventory scenarios.

## AI Tool Usage

AI assistance was used for learning, troubleshooting, and reviewing implementation ideas. The framework code and test execution were reviewed and validated by the author.
