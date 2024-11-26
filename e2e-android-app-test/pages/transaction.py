from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main import MainPage


class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver) 

    def select_income_category(self, category):
        CATEGORY_MAPPING = {
            "deposits": 4,
            "salary": 5,
            "savings": 6,
        }

        category_id = CATEGORY_MAPPING.get(category.lower())
        if category_id is None:
            raise ValueError(f"Category '{category}' is not defined in the mapping.")

        open_category_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/keyboard_action_button"))
        )
        open_category_button.click()

        select_category_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().className("android.widget.LinearLayout").instance({category_id})'))
        )
        select_category_button.click()

    def enter_amount(self, amount):
        """
        Enter the amount through the page keyboard
        """
        for digit in amount:
            button_id = f"com.monefy.app.lite:id/buttonKeyboard{digit}"
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, button_id))
                )
                button.click()
                print(f"Clicked button: {digit}")
            except Exception as e:
                print(f"Failed to click button {digit}. Exception: {e}")
                raise

    def add_income(self, amount, category):
        """
        Add an income amount
        """
        self.main_page.click_income_button()
        self.enter_amount(amount)
        self.select_income_category(category)



        