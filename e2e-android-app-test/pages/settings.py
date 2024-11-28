from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_settings_menu(self):
        settings_menu_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Settings"))
        )
        settings_menu_button.click()
