from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import re


def skip_onboarding(context):
         while True:
            try:
                #Check if the button "Continue" is present and clickable
                continue_button = WebDriverWait(context.driver, 5).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "com.monefy.app.lite:id/buttonContinue"))
                )
                continue_button.click()
            except StaleElementReferenceException:
                print("Retrying to locate the 'Continue' button due to stale reference.")
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

    # Extract the numerical value A REFACTO
    extracted_value = re.search(r"\$\s?([\d.,]+)", amount)
    extracted_value = extracted_value.group(1) if extracted_value else None

    return extracted_value