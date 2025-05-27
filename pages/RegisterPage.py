from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time, random, string

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        self.popup_css_selector = ".modal-close, .popup-close, .close"
        self.my_account_drop_down_css_selector = "a.dropdown-toggle[title='My Account']"
        self.register_button_link_text = "Register"
        self.logout_button_link_text = "Logout"
        self.login_button_link_text = "Login"
        self.first_name_field_id = "input-firstname"
        self.last_name_field_id = "input-lastname"
        self.email_field_id = "input-email"
        self.telephone_field_id = "input-telephone"
        self.password_field_id = "input-password"
        self.confirm_password_field_id = "input-confirm"
        self.newsletter_field_xpath = "//input[@name='newsletter'][@value='1']"
        self.privacy_policy_field_name = "agree"
        self.continue_button_field_xpath = "//input[@value='Continue']"
        self.registration_success_xpath = "//div[@id='content']/h1"
        self.duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
        self.privacy_policy_error_field_xpath = "//div[contains(@class, 'alert-danger') and contains(text(), 'Privacy Policy')]"
        self.first_name_error_field_xpath = "//input[@id='input-firstname']/following-sibling::div"
        self.last_name_error_field_xpath = "//input[@id='input-lastname']/following-sibling::div"
        self.email_error_field_xpath = "//input[@id='input-email']/following-sibling::div"
        self.telephone_error_field_xpath = "//input[@id='input-telephone']/following-sibling::div"
        self.password_error_field_xpath = "//input[@id='input-password']/following-sibling::div"

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def close_any_popup(self):
        try:
            close_btn = self.wait(5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.popup_css_selector))
            )
            close_btn.click()
            print("[INFO] Popup closed")
        except (TimeoutException, NoSuchElementException):
            print("[INFO] No popup to close")

    def open_register_page(self):
        self.close_any_popup()
        print("[INFO] Clicking 'My Account' dropdown")
        self.wait().until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.my_account_drop_down_css_selector))
        ).click()

        print("[INFO] Clicking 'Register' link")
        self.wait().until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.register_button_link_text))
        ).click()

    def logout(self):
        print("[INFO] Logging out if logged in")
        try:
            self.wait().until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.my_account_drop_down_css_selector))
            ).click()
            self.wait().until(
                EC.visibility_of_element_located((By.LINK_TEXT, self.logout_button_link_text))
            ).click()
            self.wait().until(
                EC.visibility_of_element_located((By.LINK_TEXT, self.login_button_link_text))
            )
            print("[INFO] Logged out successfully")
        except TimeoutException:
            print("[INFO] Logout link not found; maybe already logged out")

    def generate_email_with_timestamp(self):
        timestamp = int(time.time())
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"user{random_str}{timestamp}@example.com"

    def enter_first_name(self, fname):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.first_name_field_id)))
        field.clear()
        field.send_keys(fname)

    def enter_last_name(self, lname):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.last_name_field_id)))
        field.clear()
        field.send_keys(lname)

    def enter_auto_email(self):
        email_value = self.generate_email_with_timestamp()
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.email_field_id)))
        field.clear()
        field.send_keys(email_value)

    def enter_email(self,email):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.email_field_id)))
        field.clear()
        field.send_keys(email)

    def enter_telephone(self, telephone):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.telephone_field_id)))
        field.clear()
        field.send_keys(telephone)

    def enter_password(self, password):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.password_field_id)))
        field.clear()
        field.send_keys(password)

    def confirm_password(self, cpassword):
        field = self.wait().until(EC.element_to_be_clickable((By.ID, self.confirm_password_field_id)))
        field.clear()
        field.send_keys(cpassword)


    def check_newsletter_box(self):
        field = self.wait().until(EC.element_to_be_clickable((By.XPATH, self.newsletter_field_xpath)))
        field.click()

    def check_privacy_box(self):
        checkbox = self.wait().until(EC.element_to_be_clickable((By.NAME, self.privacy_policy_field_name)))
        checkbox.click()

    def click_continue_button(self):
        button = self.wait().until(EC.element_to_be_clickable((By.XPATH, self.continue_button_field_xpath)))
        button.click()

    def registration_success(self):
        header = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.registration_success_xpath)))
        actual_text = header.text.strip()
        expected_text = "Your Account Has Been Created!"
        print(f"[INFO] Confirmation text: '{actual_text}'")
        assert actual_text == expected_text, f"[ERROR] Expected '{expected_text}', but got '{actual_text}'"

    def warning_message_duplicate(self):
        warning_element = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.duplicate_email_warning_xpath)))
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        actual_warning_text = warning_element.text
        print(f"[INFO] Warning text: '{actual_warning_text}'")
        assert expected_warning_text in actual_warning_text

    def warning_message_privacy_policy(self):
        warning_element = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.duplicate_email_warning_xpath)))
        expected_warning_text = "Warning: You must agree to the Privacy Policy!"
        actual_warning_text = warning_element.text
        print(f"[INFO] Warning text: '{actual_warning_text}'")
        assert expected_warning_text in actual_warning_text

    
    def warning_message_first_name(self):
        warning_first_name = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.first_name_error_field_xpath)))
        expected_warning_first_name_text = "First Name must be between 1 and 32 characters!"
        actual_first_name_text = warning_first_name.text
        print(f"[INFO] First name warning text: '{actual_first_name_text}'")
        assert expected_warning_first_name_text == actual_first_name_text

    def warning_message_last_name(self):
        warning_last_name = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.last_name_error_field_xpath)))
        expected_warning_last_name_text = "Last Name must be between 1 and 32 characters!"
        actual_last_name_text = warning_last_name.text
        print(f"[INFO] Last name warning text: '{actual_last_name_text}'")
        assert expected_warning_last_name_text == actual_last_name_text

    def warning_message_email(self):
        warning_email = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.email_error_field_xpath)))
        expected_warning_email_text = "E-Mail Address does not appear to be valid!"
        actual_email_text = warning_email.text
        print(f"[INFO] Email warning text: '{actual_email_text}'")
        assert expected_warning_email_text == actual_email_text

    def warning_message_telephone(self):
        warning_telephone = self.wait().until(EC.visibility_of_element_located((By.XPATH, self.telephone_error_field_xpath)))
        expected_warning_telephone_text = "Telephone must be between 3 and 32 characters!"
        actual_telephone_text = warning_telephone.text
        print(f"[INFO] Telephone warning text: '{actual_telephone_text}'")
        assert expected_warning_telephone_text == actual_telephone_text

    def warning_message_password(self):
        warning_password = self.wait().until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-password']/following-sibling::div")))
        expected_warning_password_text = "Password must be between 4 and 20 characters!"
        actual_password_text = warning_password.text
        print(f"[INFO] Password warning text: '{actual_password_text}'")
        assert expected_warning_password_text == actual_password_text
