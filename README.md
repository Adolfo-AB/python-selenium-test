# Sysdig Technical Interview (Adolfo Aguirrezabal)
This project has the code related to sysdig technical interview regarding the Software Development Engineer in Test position.
It uses Python's Selenium framework to test different aspects of sysdig homepage/login page.

# Setup Requierements
- Python 3 (I used Python 3.9.6)
- Pytest library (pip install pytest)
- Selenium library (pip install selenium)
- Latest Chrome version and its respective webdriver downloaded and added to the Path environment variable
(https://sites.google.com/a/chromium.org/chromedriver/)

# Project structure
## Pages
Package that contains the page objects corresponding to the homepage/login (login.py) and the password recovery page (password_recovery.py). Each of these page objects contain its URL, locators and different methods to interact with the page.

## Test
Folder that contains the sample tests developed for this interview (test_sysdig_homepage.py) and the test configuration file (conftest.py).

# Testing proposal
For this exercise, limited to ~2h, I've developed 3 tests:
- A test that verifies that all the elements of the page are present when loading the page (buttons, input fields, links, selectors...).
- A test that verifies that when the user with invalid credentials tries to login an error message appears.
- A test that verifies that when the user clicks on the "Forgot your password?" button he is redirected to the password recovery page.

However, a more extensive testing of this page should include more tests:
- Verify that when accessing the homepage ('https://app.sysdigcloud.com/') the user is redirected to the login page automatically.
- Verify that a user with valid credentials can log in successfuly.
- Verify that the email and password cannot have invalid characters or exceed the maximum number of characters.
- Verify that the third-party log in buttons work.
- Verify that the free trial link redirects the user to the corresponding page.
- Verify that the region selector works and redirects the user to the corresponding pages.
- Execute automated tests with the different browsers.
- Ensure that authentication security works and there is no way to bypass it.

Other improvements could include exception management and loggers.

# Running the tests
To run the tests, clone the repository, open cmd inside the sysdig folder and execute the following command: python -m pytest


