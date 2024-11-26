from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import extract_value


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_income(self, amount, category):
        # here ajouter les step pour ajouter un amount
        self.click_income_button()

    def click_income_button(self):
        add_income_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/income_button"))
        )
        add_income_button.click()

    def get_total_balance(self):
        """
        Retrieve the total balance value displayed on the main screen.
        """
        total_balance_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/balance_amount"))
        )

        raw_total = total_balance_field.text
        total_balance = extract_value(raw_total)
        return total_balance

    def get_total_income_balance(self):
        """
        Retrieve the total income balance value displayed on the main screen.
        """
        total_income_balance_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/income_amount_text"))
        )
        
        raw_total = total_income_balance_field.text
        total_income_balance = extract_value(raw_total)
        return total_income_balance