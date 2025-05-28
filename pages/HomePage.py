from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.SearchPage import SearchPage
import time, random, string

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators as tuples
        self.search_field = (By.XPATH, "//input[@name='search']")
        self.search_button = (By.XPATH, "//button[contains(@class,'btn-default')]")
        self.my_account_dropdown = (By.XPATH, "//span[text()='My Account']")
        self.login_link = (By.XPATH, "//a[text()='Login']")
        self.login_email = (By.ID, "input-email")
        self.login_password = (By.ID, "input-password")
        self.login_button = (By.XPATH, "//input[@value='Login']")
        self.warning_text = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def enter_product_into_search_box_field(self, product):
        self.type(product, self.search_field)

    def click_search_button(self):
        self.click(self.search_button)
        return SearchPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_search_button()

    def click_on_my_account_drop_menu(self):
        self.click(self.my_account_dropdown)

    def click_login_option(self):
        self.click(self.login_link)

    def enter_email(self, email):
        self.type(email, self.login_email)

    def enter_random_email(self):
        self.type(self.generate_email_with_timestamp(), self.login_email)

    def enter_password(self, password):
        self.type(password, self.login_password)

    def click_login_button(self):
        self.click(self.login_button)

    def validate_warning_message(self):
        warning = self.get_text(self.warning_text)
        assert "Warning" in warning

    def generate_email_with_timestamp(self):
        timestamp = int(time.time())
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"user{random_str}{timestamp}@example.com"
   


    