
# BEST BUY VARIETY STORE POS SYSTEM

"""
This part stores all the items in the store.
I used a dictionary because it allows me to save the product name, the price and the stock amount in one place.
Each product has two details, its price and how many are in stock.
"""
products = {
    "Dove Dry Spray": {"price": 750, "stock": 10},
    "Ammens Medicated Powder": {"price": 1200, "stock": 8},
    "Lysol Disinfectant Spray": {"price": 1500, "stock": 6},
    "Sophie 24pk Tissue": {"price": 2000, "stock": 20},
    "Irish Spring Soap": {"price": 250, "stock": 15},
    "Colgate Toothpaste": {"price": 350, "stock": 12},
    "Reach Toothbrush 3pk": {"price": 700, "stock": 10},
    "Hair Brush": {"price": 550, "stock": 7},
    "Hair Comb": {"price": 250, "stock": 5},
    "Johnsons Baby Oil": {"price": 700, "stock": 9}
}

# These are constant values used in my program.
# The tax rate is 10%, the discount rate is 5%, and the customer only gets the discount if the subtotal is above 5000.
# For example, if I want to change the tax I only need to change it in one place.

TAX_RATE = 0.10
DISCOUNT_RATE = 0.05
DISCOUNT_LIMIT = 5000



def show_products():
    """
    This function prints the product catalog.
    It loops through the products dictionary and shows the name of each item, its price, and how many are left in stock.
    I used a for loop and read from the product dictionary.
    """
    print("\n========= PRODUCT CATALOG =========")
    for name, details in products.items():
        print(f"{name} - Price: ${details['price']:.2f} | Stock: {details['stock']}")
    print("===================================")


# This is to show low stock alert, if the stock is less than 5, it prints a warning message.
# If none are low, it says there are no low-stock items.
# I used a for loop and I also use an if statement.

def low_stock_alert():
    print("\n------ LOW STOCK ALERT ------")
    low_found = False
    for name, details in products.items():
        if details["stock"] < 5:
            print(f"{name} is low in stock. Only {details['stock']} left.")
            low_found = True
    if not low_found:
        print("No low-stock items at the moment.")
    print("-----------------------------")


# This function first shows the products, then asks the user to enter the product name and then quantity.
# It checks if the item exists, checks if the quantity is there, and checks if there is enough stock.
# It updates the stock after adding
# It validates the product name and also converts quantity to integer.
# It also helps prevent errors by using try and except in case the user enters something that is not a number.

def add_to_cart(cart):
    show_products()
    item = input("Enter the product name to add to cart: ").strip()

    if item not in products:
        print("Sorry, that item is not in the catalog.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    if quantity > products[item]["stock"]:
        print("Not enough stock available.")
        return

    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {
            "price": products[item]["price"],
            "quantity": quantity
        }

    products[item]["stock"] -= quantity
    print(f"{quantity} x {item} added to cart.")


# This is to remove an item from cart.
# If the user removes all the items, it deletes it from the cart completely and if only part is removed, it reduces the quantity.
# It also adds the removed amount back to the stocks.

def remove_from_cart(cart):
    if len(cart) == 0:
        print("Cart is empty.")
        return

    view_cart(cart)
    item = input("Enter the product name to remove from cart: ").strip()

    if item not in cart:
        print("That item is not in the cart.")
        return

    try:
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    if quantity >= cart[item]["quantity"]:
        products[item]["stock"] += cart[item]["quantity"]
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        cart[item]["quantity"] -= quantity
        products[item]["stock"] += quantity
        print(f"{quantity} x {item} removed from cart.")


# This is to print all items currently in the cart.
# It shows the quantity, unit price, and total for each item and it also adds all the items totals together to give the subtotal.

def view_cart(cart):
    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\n============= SHOPPING CART =============")
    total = 0
    for item, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        print(f"{item} | Qty: {details['quantity']} | Unit Price: ${details['price']:.2f} | Total: ${item_total:.2f}")
    print(f"Cart Subtotal: ${total:.2f}")
    print("=========================================")


# This is to calculate totals
# First it adds up all item total to get the subtotal.
# Then it checks whether the subtotal is greater than the discount limit, if yes, it applies a 5% discount.
# After that, it calculates tax on the discounted amount and then adds it to get the final total.

def calculate_bill(cart):
    subtotal = 0
    for item, details in cart.items():
        subtotal += details["price"] * details["quantity"]

    discount = 0
    if subtotal > DISCOUNT_LIMIT:
        discount = subtotal * DISCOUNT_RATE

    subtotal_after_discount = subtotal - discount
    tax = subtotal_after_discount * TAX_RATE
    total = subtotal_after_discount + tax

    return subtotal, discount, tax, total


# This is to print the receipt.
# I used the equal signs and dashes as separators to organize the receipt into sections.

def print_receipt(cart, subtotal, discount, tax, total, amount_paid, change):
    print("\n========================================")
    print("           BEST BUY RETAIL STORE        ")
    print("          Point of Sale Receipt         ")
    print("========================================")

    for item, details in cart.items():
        item_total = details["price"] * details["quantity"]
        print(f"{item}")
        print(f"  Qty: {details['quantity']} x ${details['price']:.2f} = ${item_total:.2f}")

    print("----------------------------------------")
    print(f"Subtotal:            ${subtotal:.2f}")
    print(f"Discount:            ${discount:.2f}")
    print(f"Sales Tax (10%):     ${tax:.2f}")
    print(f"Total Due:           ${total:.2f}")
    print(f"Amount Paid:         ${amount_paid:.2f}")
    print(f"Change:              ${change:.2f}")
    print("========================================")
    print("Thank you for shopping with us!")
    print("========================================")


# This is to checkout when a customer is ready to pay.
# First, it checks whether the cart is empty, if not, it calls the calculate_bill function to get the bill amount.
# Then it asks the user to enter the amount paid.
# If the payment is not enough, it tells the user to enter more.
# If the payment is enough, it calculates the change, prints the receipt, clears the cart, and ends the transaction.
# It uses a while loop

def checkout(cart):
    if len(cart) == 0:
        print("Cart is empty. Nothing to checkout.")
        return False

    subtotal, discount, tax, total = calculate_bill(cart)

    print("\n========== CHECKOUT ==========")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Due: ${total:.2f}")
    print("==============================")

    while True:
        try:
            amount_paid = float(input("Enter amount paid by customer: $"))
            if amount_paid < total:
                print("Payment is not enough. Please enter enough money.")
            else:
                change = amount_paid - total
                print_receipt(cart, subtotal, discount, tax, total, amount_paid, change)
                cart.clear()
                return True
        except ValueError:
            print("Invalid input. Payment must be a number.")


# This is the main function of the program.
# It connects the whole program together.

def main():
    print("Welcome to Best Buy Retail Store POS System")
    print("This system helps the cashier process customer purchases.")

    while True:
        cart = {}

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Show Products")
            print("2. Add Item to Cart")
            print("3. Remove Item from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Low Stock Alert")
            print("7. End Transaction")
            print("================================")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                show_products()
            elif choice == "2":
                add_to_cart(cart)
            elif choice == "3":
                remove_from_cart(cart)
            elif choice == "4":
                view_cart(cart)
            elif choice == "5":
                completed = checkout(cart)
                if completed:
                    break
            elif choice == "6":
                low_stock_alert()
            elif choice == "7":
                print("Transaction ended without checkout.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

        another = input("\nWould you like to start another transaction? (yes/no): ").strip().lower()
        if another != "yes":
            print("System closed. Goodbye!")
            break


# This runs the program by calling the main function.
main()
