from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import skip_onboarding
from pages.main import MainPage
from pages.transaction import TransactionPage


def before_scenario(context, scenario):
    """
    Hook executed before each scenario.  
    Initializes the Appium driver and launches the application.
    """
    print(f"Setting up for scenario: {scenario.name}")

    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "app": "./apps/monefy.apk",
        "appWaitActivity": "com.monefy.activities.onboarding.OnboardingActivity_",
        "platformVersion": "15.0",
        "noReset": False,
        "fullReset": False
    }

    # Initialize the driver
    try:
        context.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        context.main_page = MainPage(context.driver)
        context.transaction_page = TransactionPage(context.driver)
        print("App launched successfully")

        #Wait for a key element to confirm the app is fully started
        element_id = "com.monefy.app.lite:id/textViewHeader"
        WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, element_id))
        )
        print(f"App is fully loaded. Element {element_id} is visible.")

        skip_onboarding(context)

        #close the special offer page
        button_close_special_offer = context.driver.find_element(AppiumBy.ID, "com.monefy.app.lite:id/buttonClose")
        button_close_special_offer.click()

    except Exception as e:
        # Capture the exception and print a user-friendly error message
        print(f"Error: Unable to launch the application. Check Appium logs for details.")
        print(f"Exception: {e}")
        # Optionally, fail fast if the application cannot launch
        raise