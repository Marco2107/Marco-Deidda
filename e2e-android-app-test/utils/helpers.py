from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def skip_onboarding(context):
        for _ in range(3):
            try:
                continue_button = WebDriverWait(context.driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "com.monefy.app.lite:id/buttonContinue"))
                )
                continue_button.click()
            except StaleElementReferenceException:
                print("onboarding: Retrying to locate the 'Continue' button.")
                continue
            except Exception as e:
                print(f"onboarding: Failed to click 'Continue' button: {e}")
                raise

        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/textViewLayover"))
        )
