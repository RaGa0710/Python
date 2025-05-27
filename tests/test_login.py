from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup_browser")
class TestLogin:

    base_url = "https://tutorialsninja.com/demo/index.php"

    def navigate_to_login_page(self):
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_login_option()

        # Optional: Verify navigation succeeded
        print("Current URL after clicking login:", self.driver.current_url)
        assert "route=account/login" in self.driver.current_url

    def test_login_with_valid_credentials(self):
        self.navigate_to_login_page()

        home_page = HomePage(self.driver)
        home_page.enter_email("coolramuus1@yahoo.com")
        home_page.enter_password("123456")
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.is_login_successful()

    def test_login_with_invalid_email(self):
        self.navigate_to_login_page()

        home_page = HomePage(self.driver)
        home_page.enter_random_email()
        home_page.enter_password("123456")
        home_page.click_login_button()
        home_page.validate_warning_message()      

    def test_login_with_invalid_password(self):
         self.navigate_to_login_page()

         home_page = HomePage(self.driver)
         home_page.enter_email("coolramuus8@yahoo.com")
         home_page.enter_password("1234")
         home_page.click_login_button()
         home_page.validate_warning_message()
        
    def test_login_with_no_credentials(self):
        self.navigate_to_login_page()

        home_page = HomePage(self.driver)
        home_page.click_login_button()
        home_page.validate_warning_message()

       