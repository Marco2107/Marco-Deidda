from appium import webdriver
from behave import given
from appium.webdriver.common.appiumby import AppiumBy

@given('the first page is displayed')
def step_impl(context):

    # Vérification de l'existence du driver
    assert hasattr(context, 'driver'), "Driver not found in context! Check if environment.py properly initialized it"
    assert context.driver is not None, "Driver is None! Check environment.py initialization"

    # Localise le bouton par son ID
    gift_button = context.driver.find_element(AppiumBy.ID, "com.monefy.app.lite:id/textViewLayover")

    # Fait un assert pour vérifier qu'il est affiché
    assert gift_button.is_displayed(), "Gift button is not displayed!"