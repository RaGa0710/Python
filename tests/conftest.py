import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utilities import ReadConfigurations
import allure
from allure_commons.types import AttachmentType

@pytest.fixture()
def log_on_failure(request):
    yield 
    item = request.node
    if item.rep_call.failed:
       allure.attach(driver.get_screenshot_as_png(),name="search_without_product",
                                                       attachment_type=AttachmentType.PNG) 
      

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def setup_browser(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver=None
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