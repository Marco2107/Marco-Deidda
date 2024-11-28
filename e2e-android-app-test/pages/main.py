from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from utils.helpers import extract_value


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_income_button(self):
        add_income_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/income_button"))
        )
        add_income_button.click()

    def click_expense_button(self):
        expense_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/expense_button"))
        )
        expense_button.click()

    def open_transaction_history(self):
        expand_history_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/leftLinesImageView"))
        )
        expand_history_button.click()

    def click_category_button(self, category):
        CATEGORY_MAPPING = {
            "bills": 4,
            "car": 1,
            "clothes": 7,
            "communications": 12,
            "eating_out": 6,
            "entertainment": 3,
            "food": 0,
            "gifts": 9,
            "health": 11,
            "house": 4,
            "pets": 13,
            "sport": 10,
            "taxi": 5,
            "toiletry": 8,
            "transport": 2
        }

        category_id = CATEGORY_MAPPING.get(category.lower())
        print(f"category_clicked {category_id}")
        print(f"Attempting to click category: {category} with ID: {category_id}")
        
        if category_id is None:
            raise ValueError(f"Category '{category}' is not defined in the mapping.")

        try:
            category_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().className("android.widget.ImageView").instance({category_id})'
                ))
            )
            print(f"Found button for category {category}")
            
            if category_button.is_displayed():
                print(f"Button for category {category} is visible")
            else:
                print(f"Button for category {category} is not visible")
                
            category_button.click()
            print(f"Successfully clicked category {category}")
            
        except Exception as e:
            print(f"Failed to interact with category {category}: {str(e)}")
            raise
        
    def click_expense_button_bypass_toast(self):
        """
        Temporary method to click expense button by coordinates to bypass toast overlay.
        TODO: Remove this method once toast overlay issue is fixed in the app.
        See: [link to an issue if it exists]
        """
        expense_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/expense_button"))
        )
        
        location = expense_button.location
        size = expense_button.size
        x = location['x'] + (size['width'] / 2)
        y = location['y'] + (size['height'] * 0.95)
        
        actions = ActionBuilder(self.driver)
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.click()
        actions.perform()

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
    
    def get_total_expense_balance(self):
        """
        Retrieve the total expense balance value displayed on the main screen.
        """
        total_expense_balance_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/expense_amount_text"))
        )

        raw_total = total_expense_balance_field.text
        total_expense_balance = extract_value(raw_total)
        return total_expense_balance
    