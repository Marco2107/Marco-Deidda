# Exploratory Testing Session - Monefy App

# Table of Contents
1. [Charter 1: Explore income addition to verify balance updates with positive values](#charter-1-explore-income-addition-to-verify-balance-updates-with-positive-values)
2. [Charter 2: Explore income addition with invalid values](#charter-2-explore-income-addition-with-invalid-values)
3. [Charter 3: Explore expense addition to verify balance updates with positive values](#charter-3-explore-expense-addition-to-verify-balance-updates-with-positive-values)
4. [Charter 4: Explore the modification of a transaction](#charter-4-explore-the-modification-of-a-transaction)
5. [Charter 5: Explore expense addition from a category in the main screen to verify the balance and category update](#charter-5-explore-expense-addition-from-a-category-in-the-main-screen-to-verify-the-balance-and-category-update)
6. [Charter 6: Explore the update of expense percentages by category on the main screen](#charter-6-explore-the-update-of-expense-percentages-by-category-on-the-main-screen)
7. [Charter 7: Explore the deletion of a transaction](#charter-7-explore-the-deletion-of-a-transaction)
8. [Charter 8: Explore the transaction history](#charter-8-explore-the-transaction-history)
9. [Charter 9: Explore the app's behavior when sent to the background from different screens](#charter-9-explore-the-apps-behavior-when-sent-to-the-background-from-different-screens)
10. [Prioritisation of Charters with Reasons](#prioritisation-of-charters-with-reasons)
11. [Risks to Mitigate for this type of application](#risks-to-mitigate-for-this-type-of-application)

# Charter 1: Explore income addition to verify balance updates with positive values

- **Target:** Income addition functionality on the main screen.  
- **Resources:** Various positive values (small, large, with decimals).  
- **Information Sought:** Verify that the balance updates correctly and handles edge cases (large values, decimals).  

## Testing Notes
- Add an income of "125" euros when the balance is 0.
- Add an income of "40" euros when the balance is "125".
- Add an income with a large positive number, "123456789".
- Add an income of "999999999" to test how the total balance is displayed.
- Add an income with a decimal value, "150.67".
- Add an income while the history screen is open.

## Findings
- The added amounts are displayed correctly.
- Decimal values are handled correctly.
- When an income is added, a persistent toast appears on the main screen, covering the **Expense** and **Income** buttons. If the user is performing rapid entries, they might unintentionally click **Undo**, deleting the last entry. The display of the toast should be revised. Additionally, when the **Undo** action is performed, a confirmation pop-up could be displayed to validate the user’s choice and avoid accidental actions.  
- In the value input window, the white line can be mistaken for the cursor in an input field.

# Charter 2: Explore income addition with invalid values

- **Target:** Validation of income inputs for negative or invalid cases.
- **Resources:** Negative values, zero, and invalid inputs.
- **Information Sought:** Ensure invalid inputs are blocked.

## Testing Notes
- Add an income with a negative number, "-500".
- Add an income with a large negative number, "-1111111111".
- Add an income with a value of "0".

## Findings
- - **Bug:** The app crashes after entering a large negative value (https://github.com/Marco2107/Marco-Deidda/issues/1)
- When trying to add a transaction with a negative number, a proper error message should be displayed to guide the user in their input.  

# Charter 3: Explore expense addition to verify balance updates with positive values

- **Target:** Expense addition functionality on the main screen.
- **Resources:** Various positive values (small, large, with decimals).
- **Information Sought:** Verify that the balance updates correctly and handles edge cases (large values, decimals).  

## Testing Notes
- Add an expense of "125" euros when the balance is 0.
- Add an expense of "40" euros when the balance is "-125".
- Add an expense with a large positive number, "123456789".
- Add an expense of "999999999" to test how the total balance is displayed.
- Add an expense with a decimal value, "150.67".
- Add an expense while the history screen is open.

## Findings
- The added amounts are displayed correctly.
- A persistent toast is displayed after validating an expense on the main screen, hiding the **Income** and **Expense** buttons (same as mentioned in Charter 1).  

# Charter 4: Explore the modification of a transaction

- **Target:** The modification of an expense and an income.  
- **Resources:** Positive values and invalid values.
- **Information Sought:** Ensure the data is correctly modified and updates are accurately reflected.  

## Testing Notes
- Modification of the amount.  
- Modification of the note.  
- Modify the category for an expense from **"clothes"** to **"food"**.  
- Modify the category for an income from **"deposit"** to **"salary"**.  
- Applying the modification through the **"choose category"** button.  
- Applying the modification through the **"done"** button.  

## Findings
- The balance, category percentages, and history are updated correctly after a transaction modification.  
- When opening an existing expense or income, the category field displays **"choose category"**. It should instead be pre-filled with the current category to clearly present all the information to the user.  
- A persistent toast is displayed after validating a modification on the main screen, hiding the **Income** and **Expense** buttons (same as mentioned in Charter 1).  
- **Bug:** [Note] Amount Buttons Active While Keyboard is Open (https://github.com/Marco2107/Marco-Deidda/issues/4)

# Charter 5: Explore expense addition from a category in the main screen to verify the balance and category update

- **Target:** Expense addition from category functionality on the main screen.
- **Resources:** Positive values.  
- **Information Sought:** Verify that the balance and the category are updated correctly.

## Testing Notes
- Add an expense from a category on the main screen.  

## Findings
- The balance is updated correctly.
- The category percentage is updated correctly on the main screen.
- The expense and its category are visible in the history.

# Charter 6: Explore the update of expense percentages by category on the main screen

- **Target:** Categories section on the main screen and their percentages.
- **Resources:** Positive values.
- **Information Sought:** Verify the accuracy and updates of category percentages.

## Testing Notes
- Given a single expense in one category showing 100%, when I add another expense of the same amount in a different category, then both categories should display 50% for their respective expenses.  
- Add an identical expense to each category present on the main screen.  
- Add an expense to the “Bill” category, which is not initially displayed on the main screen.  

## Findings
- A category **“Other”** appears to group smaller amounts, even when all categories have the same value.   
- When adding different values to each category, the lines connecting them to the graph can overlap.  
- The time required to activate the **'hold to display'** function on a category is too long, leading to unintended navigation to the expense entry page. Reducing this delay would make the interaction more intuitive.  
- **Bug:** [Main page] Superposed values in the center of the graph (https://github.com/Marco2107/Marco-Deidda/issues/2)

# Charter 7: Explore the deletion of a transaction

- **Target:** The deletion of an expense and an income.
- **Information Sought:** Ensure the data is correctly deleted and updates are accurately reflected.

## Testing Notes
- Delete an expense.
- Delete an income.

## Findings
- The balance, category percentages, and history are correctly updated after a transaction deletion.  
- A persistent toast is displayed after validating a deletion on the main screen, hiding the **Income** and **Expense** buttons (same as mentioned in Charter 1).  

# Charter 8: Explore the transaction history

- **Target:** The history page.  
- **Information Sought:** Verify the display of different data in the transaction history.  

## Testing Notes
- Analyze the behavior of the history when there are multiple data entries.
- Verify the display of comments in the transaction view by category.
- Verify the display of comments in the transaction view by date.

## Findings
- When switching views, the display is correct, and the entries are clearly presented.  
- When a transaction note is long, it spans two lines in the history, which reduces consistency in the design. If a note is too long, it could be truncated with “…” for better readability.  
- **Bug:** [History] the focus on the date is lost after reopening the list (https://github.com/Marco2107/Marco-Deidda/issues/3)

# Charter 9: Explore the app's behavior when sent to the background from different screens

- **Target:** Display of different pages after being sent to the background.  
- **Information Sought:** Verify that a page is correctly displayed (no crash or freeze) after being sent to the background.  

## Testing Notes
- Send the app to the background from the main page and then bring it back to the foreground.  
- Send the app to the background from the income entry screen with an amount entered.  
- Send the app to the background from the expense entry screen with an amount entered.  
- Send the app to the background from the history page.  

## Findings
- No crash or freeze found.

## Prioritisation of Charters with Reasons

The prioritisation of these charters is based on three main criteria:
1. **Impact on core functionality:** How essential the feature is to the app’s primary purpose (managing transactions).
2. **Frequency of use:** How often users interact with the feature in normal usage.
3. **Potential risks:** The severity of the issue if the functionality is broken or not working as expected.

Charters addressing critical features or high-risk issues have been assigned higher priority, while less frequently used or non-critical features are ranked lower.

| Priority      | Charter                                                                 | Reason                                                                                   |
|---------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| High          | Charter 1: Explore income addition to verify balance updates            | Core functionality; ensures balance accuracy.                                            |
| High          | Charter 3: Explore expense addition to verify balance updates           | Complementary to income addition; critical for balance accuracy.                         |
| High          | Charter 2: Explore income addition with invalid values                  | Prevents crashes and ensures correct inputs.                                             |
| Medium        | Charter 5: Explore expense addition from a category                     | Ensures accurate category updates and balance consistency.                               |
| Medium        | Charter 7: Explore the deletion of a transaction                        | Ensures data integrity and preserves user confidence.                                    |
| Medium        | Charter 6: Explore the update of expense percentages by category        | Improves user understanding of expense distribution.                                     |
| Low           | Charter 8: Explore the transaction history                              | Less critical than core operations like income/expense addition.                         |
| Low           | Charter 4: Explore the modification of a transaction                    | Less frequent action compared to adding or deleting transactions.                        |
| Low           | Charter 9: Explore the app's behavior when sent to the background       | No crashes or freezes detected; low impact on core functionality.                        |

### Risks to Mitigate for this type of application

1. **Data security:**  
   User data must be protected from breaches, and the app should allow users to delete their personal data completely if needed.

2. **Accuracy of displayed results:**  
   The app must ensure all financial calculations and displayed data are accurate to maintain trust.

3. **Cross-platform functionality:**  
   The app should work smoothly on Android and iOS devices to reach a broader audience.

4. **Performance and stability:**  
   It’s essential for the app to work well on older or less powerful devices and to handle edge cases without crashing.

5. **Error handling:**  
   Error messages need to be clear and help users quickly resolve issues without confusion.

6. **Data validation:**  
   Input fields should block incorrect or malicious data that might corrupt financial records. For instance, negative income values or improperly formatted numbers should not be accepted.

7. **Backup and recovery:**  
   Reliable backups are essential to avoid data loss and to help users recover their data in case of device failure.

8. **Compliance and regulations:**  
   The app must follow standards like GDPR or CCPA and ensure sensitive data is handled securely.

9. **Synchronization risks:**  
   If the app uses cloud or multi-device functionality, we need to ensure consistent and accurate data across all devices.

10. **User interface consistency:**  
    The UI should be intuitive and free of visual bugs that could confuse users, like overlapping elements or misaligned text.
