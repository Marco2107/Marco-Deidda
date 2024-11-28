from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import skip_onboarding, bypass_user_tutorial, load_config
from pages.main import MainPage
from pages.transaction import TransactionPage
from pages.settings import SettingsPage
from pages.transaction_history import TransactionHistory


def before_scenario(context, scenario):
    """
    Perform a full reset of the app before each feature.
    """
    print(f"Resetting app state for feature: {scenario.name}")

    #Load the desired capabilities
    config = load_config()

    # Initialize the driver
    try:
        context.driver = webdriver.Remote("http://127.0.0.1:4723", config)
        context.main_page = MainPage(context.driver)
        context.transaction_page = TransactionPage(context.driver)
        context.settings_page = SettingsPage(context.driver)
        context.transaction_history_page = TransactionHistory(context.driver)
        print("App launched successfully")

        #Wait for a key element to confirm the app is fully started
        element_id = "com.monefy.app.lite:id/textViewHeader"
        WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, element_id))
        )
        print(f"App is fully loaded. Element {element_id} is visible.")

        skip_onboarding(context)

        # Handle special offer
        button_close_special_offer = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/buttonClose"))
        )
        button_close_special_offer.click()
        print("Special offer closed")

        bypass_user_tutorial(context)

    except Exception as e:
        # Capture the exception and print a user-friendly error message
        print(f"Error: Unable to launch the application. Check Appium logs for details.")
        print(f"Exception: {e}")
        # Optionally, fail fast if the application cannot launch
        raise
