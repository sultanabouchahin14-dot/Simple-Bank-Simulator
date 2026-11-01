
1. Project Overview

The program is a micro-banking system that operates via a Command Line Interface (CLI). It allows users to manage a virtual bank account initialized with a starting balance. Users can perform basic financial operations: checking their balance, making deposits, and withdrawing funds. The code also includes basic logic to handle invalid choices and prevent overdrafts.

2. Code Structure & Analysis

The program utilizes fundamental programming concepts:
• Variables: balance stores the current funds, choice captures the user's menu selection, and money holds the transaction amounts.
• Conditional Statements (if-elif-else): Controls the application flow based on the user's input.
• Built-in Functions: print() displays messages and options, while input() captures user interaction.

Operational Workflow:

• Option "1" (Check Balance): Directly prints the current value of the balance variable.
• Option "2" (Deposit): Prompts for an amount, converts it to an integer using int(), adds it to the existing balance, and displays the update.
• Option "3" (Withdraw): Implements a guard clause; it verifies if the requested amount is less than or equal to the available balance. If true, it deducts the money; otherwise, it rejects the transaction with "Not enough money".
• Option "4" (Exit): Prints a farewell message and terminates.
• Fallback (else): Catches any inputs outside of "1" to "4" and outputs "Wrong choice".

3. Pros and Cons of the Current Implementation


Pros	Cons & Limitations
Simple and Readable: The logic is straightforward and highly suitable for beginners learning control flow.	Single-Execution Limit: The program terminates immediately after completing a single action instead of remaining open.
Basic Financial Safety: It successfully prevents users from withdrawing more money than they actually have.	Crash Vulnerability: The application will crash (ValueError) if a user types letters instead of numbers during a deposit or withdrawal.
Clear User Interface: The printed menu is simple and easy to navigate.	Data Volatility: State is stored purely in volatile memory. Restarting the script resets the balance back to 500.


4. Recommended Enhancements

To transform this script into a more robust and professional application, consider the following upgrades:
1. Implement a while loop: Keeps the program running indefinitely until the user explicitly chooses the exit option (4).
2. Add Exception Handling (try-except): Prevents crashes by gracefully catching non-numeric inputs.
3. Use Floating-Point Numbers: Switches from int() to float() to support realistic currency values with decimals (e.g., $50.50).
