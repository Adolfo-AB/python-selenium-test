"""
Page object model for the sysdig homepage/login page.
"""
from selenium.webdriver.common.by import By

class SysdigLoginPage:

    URL = 'https://app.sysdigcloud.com/#/login'

    # Locators for the elements in the page
    LOGO = (By.CLASS_NAME, 'login__logo')
    EMAIL_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.ID, 'ember1646')
    FORGOT_PWD_LINK = (By.XPATH, '//a[@href="#/forgotPassword"]')
    LOGIN_GOOGLE_BUTTON = (By.XPATH, '//a[@href="/api/oauth/google?redirectRoute=/"]')
    LOGIN_SAML_BUTTON = (By.XPATH, '//a[@href="#/samlAuthentication"]')
    LOGIN_OPENID_BUTTON = (By.XPATH, '//a[@href="#/openIdAuthentication"]')
    FREE_TRIAL_LINK = (By.XPATH, '//a[@href="https://sysdig.com/sign-up/"]')
    REGION_SELECTOR = (By.CLASS_NAME, 'reactsel__control')
    ERROR_INVALID_CREDENTIALS = (By.CLASS_NAME, 'login__error-display')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Methods to interact with the page
    def load(self):
        self.browser.get(self.URL)

    def set_email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

    def set_password(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def click_forgot_password(self):
        forgot_password_link = self.browser.find_element(*self.FORGOT_PWD_LINK)
        forgot_password_link.click()
        
    # Methods to find the different elements of the page
    def find_logo(self):
        self.browser.find_element(*self.LOGO)

    def find_email_input(self):
        self.browser.find_element(*self.EMAIL_INPUT)

    def find_password_input(self):
        self.browser.find_element(*self.PASSWORD_INPUT)

    def find_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON)

    def find_forgot_password_link(self):
        self.browser.find_element(*self.FORGOT_PWD_LINK)

    def find_login_google_button(self):
        self.browser.find_element(*self.LOGIN_GOOGLE_BUTTON)

    def find_login_saml_button(self):
        self.browser.find_element(*self.LOGIN_SAML_BUTTON)

    def find_login_openid_button(self):
        self.browser.find_element(*self.LOGIN_OPENID_BUTTON)

    def find_free_trial_link(self):
        self.browser.find_element(*self.FREE_TRIAL_LINK)

    def find_region_selector(self):
        self.browser.find_element(*self.REGION_SELECTOR)

    def find_invalid_credentials_error(self):
        self.browser.find_element(*self.ERROR_INVALID_CREDENTIALS)