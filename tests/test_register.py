import time
import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.RegisterPage import RegisterPage

@pytest.mark.usefixtures("setup_browser")
class TestRegister:

    def test_register_with_mandatory_fields(self):
        
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()
      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.enter_first_name("Ramu")
        register_page.enter_last_name("Gande")
        register_page.enter_auto_email()
        register_page.enter_telephone("1234567890")
        register_page.enter_password("123456")
        register_page.confirm_password("123456")
        register_page.check_privacy_box()
        register_page.click_continue_button()
        
        register_page.close_any_popup()

        register_page.registration_success()

        # Logout after successful registration to reset state for next tests
        register_page.logout()

    def test_register_with_all_fields(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()
      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.enter_first_name("Ramu")
        register_page.enter_last_name("Gande")
        register_page.enter_auto_email()
        register_page.enter_telephone("1234567890")
        register_page.enter_password("123456")
        register_page.confirm_password("123456")
        register_page.check_newsletter_box()
        register_page.check_privacy_box()
        register_page.click_continue_button()
        
        register_page.close_any_popup()

        register_page.registration_success()

        # Logout after successful registration to reset state for next tests
        register_page.logout()

    def test_register_with_duplicate_email(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()
      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.enter_first_name("Ramu")
        register_page.enter_last_name("Gande")
        register_page.enter_email("coolramuus@yahoo.com")
        register_page.enter_telephone("1234567890")
        register_page.enter_password("123456")
        register_page.confirm_password("123456")
        register_page.check_newsletter_box()
        register_page.check_privacy_box()
        register_page.click_continue_button()
        
        register_page.warning_message_duplicate()

    def test_register_with_no_details(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()
      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.confirm_password("")
        register_page.check_privacy_box()
        register_page.click_continue_button()

        # register_page.warning_message_privacy_policy()
        register_page.warning_message_first_name()
        register_page.warning_message_last_name()
        register_page.warning_message_email()
        register_page.warning_message_telephone()
        register_page.warning_message_password()
       

        

        
        

        

        
           