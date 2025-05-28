import time
import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):        
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.register_an_account("Ramu","Gande","auto","1234567890","123456","123456","no","select")               
        register_page.close_any_popup()
        register_page.registration_success()
        # Logout after successful registration to reset state for next tests
        register_page.logout()

    def test_register_with_all_fields(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.register_an_account("Ramu","Gande","auto","1234567890","123456","123456","yes","select")  
        register_page.close_any_popup()
        register_page.registration_success()
        # Logout after successful registration to reset state for next tests
        register_page.logout()

    def test_register_with_duplicate_email(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.register_an_account("Ramu","Gande","coolramuus@yahoo.com","1234567890","123456","123456","yes","select")        
        register_page.warning_message_duplicate()

    def test_register_with_no_details(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_page()      
        print("[INFO] Filling registration form with mandatory fields")
        register_page.register_an_account("","","","","","","no","no")     
        register_page.warning_message_privacy_policy()
        register_page.warning_message_first_name()
        register_page.warning_message_last_name()
        register_page.warning_message_email()
        register_page.warning_message_telephone()
        register_page.warning_message_password()


    

        
           