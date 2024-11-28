from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import json
import re

def load_config():
    """
    Load the config.json for the desired capabilities
    """
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def skip_onboarding(context):
    while True:
        try:
            #Check if the button "Continue" is present and clickable
            continue_button = WebDriverWait(context.driver, 5).until(
                EC.element_to_be_clickable((AppiumBy.ID, "com.monefy.app.lite:id/buttonContinue"))
            )
            continue_button.click()
        except StaleElementReferenceException:
            continue
        except Exception:
            # If the button was not found check if the onboarding is finished
            try:
                WebDriverWait(context.driver, 3).until(
                    EC.presence_of_element_located((AppiumBy.ID, "com.monefy.app.lite:id/textViewLayover"))
                )
                print("Onboarding completed.")
                break
            except Exception as e:
                print(f"Failed to confirm onboarding completion: {e}")
                raise

def extract_value(amount):
    """
    Extract the amount value to match the format 0.00
    """
    match = re.search(r"\$\s?([\d.,]+)", amount)

    return match.group(1) if match else None

def format_amount(amount):
    """
    Format amount string
    """
    if '.' in amount:
        return f"${amount}"
    return f"${amount}.00"

def bypass_user_tutorial(context):
    """
    skip the user tutorial
    """
    try:
        for i in range(4):
            try:
                click_pop_up_tutorial = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.FrameLayout").instance(10)'))
                )
                click_pop_up_tutorial.click()
            except Exception:
                print(f"error while clicking on the pop up")
                raise
        
        context.settings_page.click_settings_menu()
    except Exception as e:
        print(f"Error while skipping the user tutorial: {e}")
        raise

    print("user tutorial skipped")