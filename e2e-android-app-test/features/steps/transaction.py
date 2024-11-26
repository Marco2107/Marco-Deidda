from appium import webdriver
from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from pages.main import MainPage
from pages.transaction import TransactionPage



@given('the balance is empty')
def the_balance_is_empty(context):
    actual_total_balance = context.main_page.get_total_balance()
    assert actual_total_balance == "0.00", f"the total balance is {actual_total_balance}, should be 0.00"

@given('The user has a positive balance of {amount}')
def the_user_has_a_positive_balance_of(context, amount):
    context.transaction_page.add_income(amount, "deposit")

@when('the user navigates to the income screen')
def the_user_navigates_to_the_income_screen(context):
    context.main_page.click_income_button()

@when('the user enters the amount of "{amount}"')
def the_user_enters_the_amount_of(context, amount):
    context.transaction_page.enter_amount(amount)

@when('the user choose an income category "{category}"')
def the_user_choose_an_income_category(context, category):
    context.transaction_page.select_income_category(category)
    
@then('the total balance should be "{expected_total}"')
def the_total_balance_should_be(context, expected_total):

    actual_total_balance = context.main_page.get_total_balance()

    if "." not in expected_total:
        expected_total = f"{expected_total}.00"

    assert actual_total_balance == expected_total, f"the total balance is {actual_total_balance}, should be {expected_total}"

@then('the total income balance should be "{expected_income}"')
def the_total_income_balance_should_be(context, expected_income):
    actual_income_total = context.main_page.get_total_income_balance()

    if "." not in expected_income:
        expected_income = f"{expected_income}.00"

    assert actual_income_total == expected_income, f"the total income is {actual_income_total}, should be {expected_income}"

