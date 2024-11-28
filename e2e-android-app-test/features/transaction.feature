Feature: transaction
  As a user
  I want to manage my incomes and expenses
  So that I can keep track of my financial activity
  
  Background: the balance should be empty
    Given the balance is empty
  
  Scenario: The user should be able to add an income
    When the user navigates to the income screen
    When the user enters the amount of "100"
    And the user chooses an income category "salary"
    Then the total balance should be "100"
    And the total income balance should be "100"

  Scenario: The user adds a single expense
    Given the user has a positive balance of "250"
    When the user navigates to the expense screen
    And the user enters the amount of "50"
    And the user chooses an expense category "clothes"
    Then the total balance should be "200"
    And the total expense balance should be "50"

  Scenario: Verify expense totals by category
    Given the user has a positive balance of "500"
    When the user adds the following expenses 
      | category       | amount |
      | entertainment  | 50     |
      | house          | 25     |
    Then the total balance should be "425"
    When the user opens the transaction history
    Then the transaction history should include the following transactions
      | category       | total |
      | entertainment  | 50    |
      | house          | 25    |