""" 
Project fixtures.
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    # Create ChromeDriver instance
    chromedriver = selenium.webdriver.Chrome()

    # Wait 10s so that the elements can appear
    chromedriver.implicitly_wait(10)

    # Return the instance
    yield chromedriver

    # Quit the ChromeDriver instance
    chromedriver.quit()

