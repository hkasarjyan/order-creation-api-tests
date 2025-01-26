# API Test Automation Framework For Order Creation

## Description
This framework is designed to test the **Order Creation API** using Python, Requests, and Pytest, with additional support for **Allure Reporting**.

---

## Prerequisites
1. Ensure **Python 3.7+** is installed on your system.
2. Install **pip**, the Python package manager, if not already installed.

---

## Setup Instructions

### Step 1: Clone the Repository
```
git clone git@github.com:hkasarjyan/order-creation-api-tests.git
cd api_test_framework
```
### Step 2: Install Dependencies
Install all required Python libraries using the requirements.txt file:

```
pip install -r requirements.txt
```

### Step 3: Set the API Token
The API requires a valid token for authentication. You can set the token securely as an environment variable:

For Linux/Mac:
```
export API_TOKEN=huw515Aue5eU
```
For Windows (Command Prompt):
```
set API_TOKEN=huw515Aue5eU
```
Alternatively, you can directly set the token in the config/config.py file (not recommended for security reasons).

## Running Tests
### Run All Tests
To run all test files in the framework:
```
pytest
```

### Run a Specific Test File
To run tests for positive cases:

```
pytest tests/test_positive_cases.py
```
To run tests for negative cases:
```
pytest tests/test_negative_cases.py
```

To run tests for edge cases:
```
pytest tests/test_edge_cases.py
```
Run a Specific Test Case

To run a single test case, provide the test file and the specific test function:
```
pytest tests/test_positive_cases.py::test_valid_order_creation
```

## Allure Reporting
### Step 1: Install Allure
Install Allure for detailed reporting:
Linux/Mac:
```
brew install allure
```
### Step 2: Run Tests with Allure
Generate test results for Allure:
```
pytest --alluredir=reports/allure-results
```
### Step 3: Serve Allure Report
View the report in your browser:
```
allure serve reports/allure-results
```