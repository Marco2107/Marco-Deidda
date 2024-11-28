from behave import given, when, then


@given('the balance is empty')
def the_balance_is_empty(context):
    actual_total_balance = context.main_page.get_total_balance()
    assert actual_total_balance == "0.00", f"the total balance is {actual_total_balance}, should be 0.00"

@given('The user has a positive balance of "{amount}"')
def the_user_has_a_positive_balance_of(context, amount):
    context.transaction_page.add_income(amount, "deposits")

@when('the user navigates to the income screen')
def the_user_navigates_to_the_income_screen(context):
    context.main_page.click_income_button()

@when('the user navigates to the expense screen')
def the_user_navigates_to_the_income_screen(context):
    context.main_page.click_expense_button_bypass_toast()

@when('the user enters the amount of "{amount}"')
def the_user_enters_the_amount_of(context, amount):
    context.transaction_page.enter_amount(amount)

@when('the user chooses an income category "{category}"')
def the_user_chooses_an_income_category(context, category):
    context.transaction_page.select_income_category(category)

@when('the user chooses an expense category "{category}"')
def the_user_chooses_an_expense_category(context, category):
    context.transaction_page.select_expense_category(category)

@when('the user opens the transaction history')
def the_user_opens_the_transaction_history(context):
    context.main_page.open_transaction_history()

@when('the user adds the following expenses')
def the_user_adds_expenses_with_different_categories(context):
    for row in context.table:
        amount = row['amount']
        category = row['category']

        context.transaction_page.add_expense(amount, category)

@then('the transaction history should include the following transactions')
def the_transaction_history_should_show_this_expenses(context):
    for row in context.table:
        total = row['total']
        category = row['category']

        context.transaction_history_page.validate_transaction_history(category, total)

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

@then('the total expense balance should be "{expected_expense}"')
def the_total_income_balance_should_be(context, expected_expense):
    actual_expense_total = context.main_page.get_total_expense_balance()

    if "." not in expected_expense:
        expected_expense = f"{expected_expense}.00"

    assert actual_expense_total == expected_expense, f"the total income is {actual_expense_total}, should be {expected_expense}"
