Author: Ricardo Williams
Date Created: April 4, 2026
Course: ITT103
GitHub Public URL to Code: https://github.com/r1cky876/TechTitans/blob/main/Tech.Titans-POS-ITT103-SP2026.py


PURPOSE OF THE PROGRAM:

This program is a simple point-of-sale system designed for Best Buy Variety Store. It allows a cashier to manage customer purchases by selecting items, adding them to a cart, and completing transactions.

This POS system performs the following tasks:

	- Displays a list of regular household items with prices and stock levels
	- Allows users to add and remove items from a shopping cart
	- Calculates subtotal, discount, tax, and total cost
	- Processes customer payment and calculates change
	- Generates a formatted receipt
	- Alerts the user when stock levels are low
	- Supports multiple customer transactions

HOW TO RUN THE PROGRAM:

Step 1. Ensure Python is installed on your computer.
Step 2. Open the Python file using PyCharm.
Step 3. Run the program.
Step 4. Follow the menu displayed on the screen:
	- Enter numbers (1–7) to select options from the menu
	- Add items by typing the exact product name
	- Enter numeric values for quantities and payments
Step 5. Complete a transaction by selecting the checkout option.
Step 6. After checkout, you can choose to start a new transaction or exit the program.

REQUIRED MODIFICATIONS:

The program was modified and customized to meet project requirements:
	- A dictionary was used to store product details (price and stock)
	- Functions were created to handle different parts of the program:
		- Display products
		- Add/remove items
		- View cart
		- Calculate totals
		- Checkout and receipt generation
	- A 10% tax is applied to all purchases
	- A 5% discount is applied if the subtotal exceeds $5000
	- Input validation ensures that:
		- Quantities must be numbers
		- Payments must be numeric
		- Stock limits are enforced
	- Low-stock alerts are shown for items with less than 5 units
	- The program uses loops to allow multiple transactions

ASSUMPTIONS:

	- Users will enter product names exactly as shown in the displayed menu
	- The system is used by a cashier who understands basic menu navigation
	- Prices are fixed and do not change during runtime
	- All payments are made in full (no partial payments or payments less than the total)


LIMITATIONS:

	- The program does not save data permanently
	- Stock resets when the program is restarted
	- Product names must be typed exactly
	- Only basic error handling is implemented


