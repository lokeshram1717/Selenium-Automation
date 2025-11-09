**Selenium Automation Framework (Pytest + POM)**

**Overview :-**
This project is a Selenium-based test automation framework built using Python and Pytest.
It follows the Page Object Model (POM) design pattern and supports data-driven testing through CSV and Excel files.
Reports are generated in HTML format, and the suite can be integrated with Jenkins for CI/CD execution.

**Project Structure :-**
SeleniumProject/
│
├── pages/                        # Page Object classes
│   ├── login_page.py
│   ├── home_page.py
│   └── checkout_page.py
│
├── tests/                        # All test cases
│   ├── test_login.py
│   └── test_add_item_to_cart_and_submit.py
│
├── util/                         # Utility functions (Data readers, etc.)
│   ├── data_reader.py
│   └── excel_reader.py
│
├── Data/                         # Test data sources
│   ├── test_data.csv
│   └── test_data.xlsx
│
├── reports/                      # HTML reports generated after test runs
│
├── conftest.py                   # Pytest fixtures (driver setup/teardown)
├── requirements.txt              # Dependencies list
└── README.md                     # Project documentation

**Features :-**
1. Page Object Model (POM) for maintainability
2. Data-driven testing using CSV and Excel
3. Pytest as the core test runner
4. HTML Reports using pytest-html
5. Alert Handling implemented gracefully
6. Jenkins Integration Ready (CI/CD setup)

**Prerequisites :-**
1. Make sure you have the following installed:
  a. Python 3.10 or above
  b. Google Chrome browser
2. ChromeDriver compatible with your Chrome version
  a. Git
  b. Pytest and Selenium libraries
3. Install dependencies:
  a. pip install -r requirements.txt
4. Example requirements.txt:
  a. pytest
  b. selenium
  c. pytest-html
  d. openpyxl

**Running Tests :-**
1. Run all tests: pytest -v
2. Run a specific test file: pytest -v tests/test_login.py
3. Run with HTML report: pytest -v --html=reports/test_report.html --self-contained-html

**Data-Driven Testing :-**
1. Using CSV:
  Data stored in Data/test_data.csv
    "username,password,firstname,lastname,zipcode,product_name
    standard_user,secret_sauce,Lokesh,Ram,142301,Sauce Labs Bike Light"
2. Using Excel:
  Data stored in Data/test_data.xlsx

Note :- The utility reads headers dynamically and maps them to the test parameters.

**Jenkins Integration :-**
1. To integrate with Jenkins:
  a.Create a Jenkins job (Freestyle project).
b.In Source Code Management, choose Git and provide your repo URL.
2. In Build Steps, add:
  cd "C:\Users\saite\OneDrive\Documents\SeleniumProject"
  pytest -v --html=reports/test_report.html --self-contained-html
3. Ensure Python and pytest are added to Jenkins environment variables.
4. Run the build and check the reports folder for results.

**Future Enhancements :-**
1. Add logging using Python’s logging module
2. Capture screenshots on failure
3.Add test reports upload to Jenkins dashboard
4.Include email notifications post test run
