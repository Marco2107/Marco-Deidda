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

    def select_expense_category(self, category):
        CATEGORY_MAPPING = {
            "bills": 4,
            "car": 5,
            "clothes": 6,
            "communications": 7,
            "eating_out": 8,
            "entertainment": 9,
            "food": 10,
            "gifts": 11,
            "health": 12,
            "house": 13,
            "pets": 13,
            "sport": 15,
            "taxi": 16,
            "toiletry": 17,
            "transport": 18
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
        Enter the amount through the keyboard
        """
        print(f"enter_amount - Amount value: {amount}, Type: {type(amount)}")
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
        Add an income transaction
        """
        self.main_page.click_income_button()
        self.enter_amount(amount)
        self.select_income_category(category)

    def add_expense(self, amount, category):
        """
        Add an expense transaction
        """
        self.main_page.click_expense_button_bypass_toast()
        self.enter_amount(amount)
        self.select_expense_category(category)



        