from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage
import time, random, string


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.popup_css = (By.CSS_SELECTOR, ".modal-close, .popup-close, .close")
        self.my_account_dropdown = (By.CSS_SELECTOR, "a.dropdown-toggle[title='My Account']")
        self.register_link = (By.LINK_TEXT, "Register")
        self.logout_link = (By.LINK_TEXT, "Logout")
        self.login_link = (By.LINK_TEXT, "Login")
        self.first_name_field = (By.ID, "input-firstname")
        self.last_name_field = (By.ID, "input-lastname")
        self.email_field = (By.ID, "input-email")
        self.telephone_field = (By.ID, "input-telephone")
        self.password_field = (By.ID, "input-password")
        self.confirm_password_field = (By.ID, "input-confirm")
        self.newsletter_radio = (By.XPATH, "//input[@name='newsletter'][@value='1']")
        self.privacy_policy_checkbox = (By.NAME, "agree")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")
        self.success_header = (By.XPATH, "//div[@id='content']/h1")
        self.duplicate_email_warning = (By.XPATH, "//div[@id='account-register']/div[1]")
        self.privacy_policy_warning = (By.XPATH, "//div[contains(@class, 'alert-danger') and contains(text(), 'Privacy Policy')]")
        self.first_name_error = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
        self.last_name_error = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
        self.email_error = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
        self.telephone_error = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
        self.password_error = (By.XPATH, "//input[@id='input-password']/following-sibling::div")

    def close_any_popup(self):
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable(self.popup_css))
            close_btn.click()
            print("[INFO] Popup closed")
        except (TimeoutException, NoSuchElementException):
            print("[INFO] No popup to close")

    def open_register_page(self):
        self.close_any_popup()
        print("[INFO] Opening registration page")
        self.wait.until(EC.element_to_be_clickable(self.my_account_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.register_link)).click()

    def logout(self):
        print("[INFO] Attempting logout")
        try:
            self.wait.until(EC.element_to_be_clickable(self.my_account_dropdown)).click()
            self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
            self.wait.until(EC.visibility_of_element_located(self.login_link))
            print("[INFO] Successfully logged out")
        except TimeoutException:
            print("[INFO] Already logged out or logout button not found")

    def generate_email_with_timestamp(self):
        timestamp = int(time.time())
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"user{random_str}{timestamp}@example.com"

    def fill_input(self, locator, value):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)

    def enter_first_name(self, fname):
        self.fill_input(self.first_name_field, fname)

    def enter_last_name(self, lname):
        self.fill_input(self.last_name_field, lname)

    def enter_email(self, email):
        self.fill_input(self.email_field, email)

    def enter_auto_email(self):
        email = self.generate_email_with_timestamp()
        self.enter_email(email)

    def enter_telephone(self, telephone):
        self.fill_input(self.telephone_field, telephone)

    def enter_password(self, password):
        self.fill_input(self.password_field, password)

    def confirm_password(self, cpassword):
        self.fill_input(self.confirm_password_field, cpassword)

    def check_newsletter_box(self):
        self.wait.until(EC.element_to_be_clickable(self.newsletter_radio)).click()

    def check_privacy_box(self):
        self.wait.until(EC.element_to_be_clickable(self.privacy_policy_checkbox)).click()

    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def register_an_account(self, fname, lname, email, telephone, password, cpassword, yes_or_no, privacy_policy):
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        if email == "auto":
            self.enter_auto_email()
        else:
            self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.confirm_password(cpassword)
        if yes_or_no.lower() == "yes":
            self.check_newsletter_box()
        if privacy_policy.lower() == "select":
            self.check_privacy_box()
        self.click_continue_button()

    def registration_success(self):
        actual_text = self.wait.until(EC.visibility_of_element_located(self.success_header)).text.strip()
        expected_text = "Your Account Has Been Created!"
        print(f"[INFO] Confirmation: '{actual_text}'")
        assert actual_text == expected_text, f"[ERROR] Expected '{expected_text}', but got '{actual_text}'"

    def _assert_warning_message(self, locator, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(locator)).text.strip()
        print(f"[INFO] Warning: '{actual_text}'")
        assert expected_text in actual_text, f"[ERROR] Expected '{expected_text}' in '{actual_text}'"

    def warning_message_duplicate(self):
        self._assert_warning_message(self.duplicate_email_warning, "Warning: E-Mail Address is already registered!")

    def warning_message_privacy_policy(self):
        self._assert_warning_message(self.duplicate_email_warning, "Warning: You must agree to the Privacy Policy!")

    def warning_message_first_name(self):
        self._assert_warning_message(self.first_name_error, "First Name must be between 1 and 32 characters!")

    def warning_message_last_name(self):
        self._assert_warning_message(self.last_name_error, "Last Name must be between 1 and 32 characters!")

    def warning_message_email(self):
        self._assert_warning_message(self.email_error, "E-Mail Address does not appear to be valid!")

    def warning_message_telephone(self):
        self._assert_warning_message(self.telephone_error, "Telephone must be between 3 and 32 characters!")

    def warning_message_password(self):
        self._assert_warning_message(self.password_error, "Password must be between 4 and 20 characters!")
