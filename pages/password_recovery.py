"""
Page object model for the sysdig password recovery page.
"""
from selenium.webdriver.common.by import By

class SysdigPasswordRecoveryPage:

    URL = 'https://app.sysdigcloud.com/#/forgotPassword'

    # Locators
    EMAIL_INPUT = (By.NAME, 'username')
    REQUEST_PWD_BUTTON = (By.ID, 'ember1545')

    # Initializer
    def __init__(self, browser):
        self.browser = browser
