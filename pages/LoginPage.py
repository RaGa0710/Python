from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self,driver):
        self.driver=driver



    login_successful_message_xpath = "//h2[text()='My Account']"

    def is_login_successful(self):
        """Wait for the 'My Account' heading to appear after login."""
        try:
            wait = WebDriverWait(self.driver, 10)
            heading = wait.until(EC.visibility_of_element_located((By.XPATH, self.login_successful_message_xpath)))
            return heading.is_displayed()
        except TimeoutException:
            return False



