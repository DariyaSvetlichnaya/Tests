from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage
from page_objects.scanners_page import ScannersPage
from selenium.webdriver.common.by import By

def test_export_scanners_page(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    login_page = LoginPage(driver)
    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()



