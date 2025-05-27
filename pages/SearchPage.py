from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    valid_hp_product_linktext = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    # Methods
    def display_status_of_valid_product(self):
        """Returns True if the valid product is displayed."""
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_linktext).is_displayed()

    def display_status_of_invalid_product(self):
        """Returns the trimmed text of the invalid/no product message."""
        element = self.driver.find_element(By.XPATH, self.no_product_message_xpath)
        message = element.text.strip()
        print(f"DEBUG: Invalid product message text: '{message}'")
        return message
    