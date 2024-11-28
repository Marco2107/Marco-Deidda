from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import format_amount


class TransactionHistory:
    def __init__(self, driver):
        self.driver = driver

    def validate_transaction_history(self, category, amount):
        """
        Validate that a transaction with specified category and amount exists in the history
        """
        formatted_category = category.capitalize()
        formatted_amount = format_amount(amount)

        # find the containers
        containers = self.driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.monefy.app.lite:id/transaction_group_header")'
        )

        found = False
        for container in containers:
            try:
                category_element = container.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{formatted_category}")'
                )

                expense_element = container.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{formatted_amount}")'
                )

                if category_element and expense_element:
                    found = True
                    print(f"Transaction found: {formatted_category} - {formatted_amount}")
                    break

            except Exception:
                continue

        assert found, f"Transaction not found: {formatted_category} - {formatted_amount}"