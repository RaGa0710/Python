from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.login_successful_message = (By.XPATH, "//h2[text()='My Account']")

    def is_login_successful(self):
        """Use BasePage's is_displayed method to check login success."""
        return self.is_displayed(self.login_successful_message)



