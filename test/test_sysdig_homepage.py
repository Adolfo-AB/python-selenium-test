"""
Tests to verify that sysdig homepage/login page works as expected.
"""
from pages.password_recovery import SysdigPasswordRecoveryPage
from pages.login import SysdigLoginPage

# Scenario 1: Verify that all the elements of the page are present.
# This test case could also be split into different scenarios,
# one for each assert.
def test_login_elements(browser):

    login_page = SysdigLoginPage(browser)

    # When the sysdig login page is loaded
    login_page.load()

    # Then the sysdig logo is displayed
    login_page.find_logo()

    # And the email address field is displayed
    login_page.find_email_input()

    # And the password field is displayed
    login_page.find_password_input()

    # And the "Forgot your password?" field is displayed
    login_page.find_forgot_password_link()

    # And the Login button login is displayed
    login_page.find_login_button()

    # And the Google login button is displayed
    login_page.find_login_google_button()

    # And the SAML login button is displayed
    login_page.find_login_saml_button()

    # And the OpenID login button is displayed
    login_page.find_login_openid_button()

    # And the "Sign up for a free trial!" field is displayed
    login_page.find_free_trial_link()

    # And the region selector is displayed
    login_page.find_region_selector()

    
# Scenario 2: Verify that when the user tries to log with invalid credentials an error message appears
def test_login_incorrect_user(browser):

    login_page = SysdigLoginPage(browser)

    # Given the sysdig login page is loaded
    login_page.load()

    # When the user sets an email
    login_page.set_email("adolfo-aguirrezabal@sysdig.com")

    # And the user sets a password
    login_page.set_password("password123")

    # And the user clicks the log in button
    login_page.click_login_button()

    # Then an error message appears stating that the credentials are not valid
    login_page.find_invalid_credentials_error()


# Scenario 3: Verify that when the user clicks on the "Forgot your password?" link 
# he is redirected to the password recovery page
def test_forgot_password_redirect(browser):
    login_page = SysdigLoginPage(browser)
    pwd_recovery_page = SysdigPasswordRecoveryPage(browser)

    # Given the sysdig login page is loaded
    login_page.load()

    # When the user clicks on the "Forgot your password?" link
    login_page.click_forgot_password()

    # Then the user is redirected to the password recovery page
    assert pwd_recovery_page.URL == browser.current_url
