from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


def before_scenario(context, scenario):
    """
    Hook executed before each scenario.  
    Initializes the Appium driver and launches the application.
    """
    print(f"Setting up for scenario: {scenario.name}")

    # Desired Capabilities
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5556",
        "automationName": "UiAutomator2",
        "app": "./apps/monefy.apk",
        "appWaitActivity": "com.monefy.activities.buy.BuyMonefySpecialOfferActivity_",
        "platformVersion": "15.0",
        "noReset": True,
        "fullReset": False
    }

    # Initialize the driver
    try:
        context.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        print("App launched successfully")

        # Wait for a key element to confirm the app is fully started
        element_id = "com.monefy.app.lite:id/textViewLayover"  # Replace with the ID of a key element
        WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, element_id))
        )
        print(f"App is fully loaded. Element {element_id} is visible.")
    except Exception as e:
        # Capture the exception and print a user-friendly error message
        print(f"Error: Unable to launch the application. Check Appium logs for details.")
        print(f"Exception: {e}")
        # Optionally, fail fast if the application cannot launch
        raise

def after_scenario(context, scenario):
    """
    Hook executed after each scenarios
    Close the application
    """
    print(f"Tearing down after scenario: {scenario.name}")
    if context.driver:
        context.driver.close()
