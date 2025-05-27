import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utilities import ReadConfigurations

@pytest.fixture(scope="class")
def setup_browser(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Provide a valid browser name: chrome/firefox/edge")

    driver.maximize_window()
    base_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(base_url)

    request.cls.driver = driver
    request.cls.base_url = base_url

    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def logout_after_test(request):
    yield  # Let the test run first

    driver = getattr(request.cls, "driver", None)
    if driver:
        try:
            logout_link = driver.find_element(By.LINK_TEXT, "Logout")
            if logout_link.is_displayed():
                logout_link.click()
        except NoSuchElementException:
            pass  # Logout link not found – probably not logged in