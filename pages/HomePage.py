from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import string



class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # XPaths for elements on the page
        self.search_field_xpath =  "//input[@name='search']"
        self.search_button_xpath = "//button[contains(@class,'btn-default')]"
        self.my_account_dropdown_xpath = "//span[text()='My Account']"
        self.login_link_xpath = "//a[text()='Login']"
        self.login_email_id = "//input[@id='input-email']"
        self.login_password_id = "//input[@id='input-password']"
        self.login_button_xpath = "//input[@value='Login']"
        self.validate_warning_text_css_selector = "div.alert.alert-danger"


    def enter_product_into_search_box_field(self,product):
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_field_xpath)))
        search.clear()
        search.send_keys(product)

    def click_search_button(self):
        wait = WebDriverWait(self.driver, 10)
        search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath)))
        search_btn.click()
        
        
    def click_on_my_account_drop_menu(self):
        wait = WebDriverWait(self.driver, 10)
        my_account = wait.until(EC.element_to_be_clickable((By.XPATH, self.my_account_dropdown_xpath)))
        my_account.click()
        
    def click_login_option(self):
        wait = WebDriverWait(self.driver, 10)
        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_link_xpath)))
        login_link.click()
        
    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        email_id = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_email_id)))
        email_id.clear()
        email_id.send_keys(email)

    def enter_random_email(self):
        wait = WebDriverWait(self.driver, 10)
        email_id = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_email_id)))
        email_id.clear()
        email_id.send_keys(self.generate_email_with_timestamp())
    
        
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_id = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_password_id)))
        password_id.clear()
        password_id.send_keys(password)
        
    def click_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        login_button.click()

    def validate_warning_message(self):
        wait = WebDriverWait(self.driver, 10)
        warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validate_warning_text_css_selector)))
        assert "Warning" in warning.text


    def generate_email_with_timestamp(self):
        timestamp = int(time.time())  # Current timestamp in seconds
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        email = f"user{random_str}{timestamp}@example.com"
        return email

   


    