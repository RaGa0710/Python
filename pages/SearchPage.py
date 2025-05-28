from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.valid_hp_product = (By.LINK_TEXT, "HP LP3065")
        self.no_product_message = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    def display_status_of_valid_product(self):
        """Returns True if the valid product is displayed."""
        try:
            element = self.wait.until(EC.presence_of_element_located(self.valid_hp_product))
            return element.is_displayed()
        except:
            return False

    def display_status_of_invalid_product(self):
        """Returns the trimmed text of the invalid/no product message."""
        try:
            element = self.wait.until(EC.presence_of_element_located(self.no_product_message))
            message = element.text.strip()
            print(f"DEBUG: Invalid product message text: '{message}'")
            return message
        except:
            return ""
    