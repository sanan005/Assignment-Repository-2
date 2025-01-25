 #Vending Machine Application

# Defining the items available in the vending machine with categories and stock count
items = {
    'A': {'name': 'Coke', 'category': 'Drink', 'price': 2.50, 'stock': 10},
    'B': {'name': 'Tea', 'category': 'Drink', 'price': 2.50, 'stock': 5},
    'C': {'name': 'Chips', 'category': 'Snack', 'price': 4.00, 'stock': 8},
    'D': {'name': 'Chocolate', 'category': 'Snack', 'price': 6.25, 'stock': 12},
    'E': {'name': 'Coffee', 'category': 'Drink', 'price': 5.00, 'stock': 5},
    'F': {'name': 'Cake', 'category': 'Snack', 'price': 4.50, 'stock': 5},
}

# Defining suggested items for complementary purchases
suggested_items = {
    "coffee": "chips",
    "tea": "cake",
    "chips": "coke",
}

# Function to display all available items
def display_items():
    print("Welcome to the vending machine! Here are the available items:")
    print("Item Code | Name      | Category  | Price | Stock")
    for item_code, item in items.items():
        print(f"{item_code}        | {item['name']}  | {item['category']} | {item['price']} | {item['stock']}")

# Function to check if the item is in stock
def check_stock(item_code):
    if item_code in items:
        return items[item_code]['stock'] > 0
    return False

# Function to check if the user has enough money to buy an item
def check_price(item_code, amount):
    if item_code in items:
        if items[item_code]['price'] <= amount:
            return True
    return False

# Function to update the stock after a successful purchase
def update_stock(item_code):
    if item_code in items and items[item_code]['stock'] > 0:
        items[item_code]['stock'] -= 1
        print(f"{items[item_code]['name']} has been dispensed!")
    else:
        print("Sorry, the item is out of stock.")

# Function to suggest a complementary item based on the current selection
def suggest_item(item_code):
    if item_code in suggested_items:
        suggestion = suggested_items[item_code]
        print(f"Since you bought {items[item_code]['name']}, we suggest you try {suggestion}!")

# Main function to handle the user interaction
def main():
    while True:
        # Displaying the available items
        display_items()
        
        # Asking for user input (item code and money)
        item_code = input("Please enter the item code to buy or 'quit' to exit: ").upper()
        if item_code == 'QUIT':
            break
        
        if item_code not in items:
            print("Invalid item code. Please try again.")
            continue
        
        # Check if the item is in stock
        if not check_stock(item_code):
            print(f"Sorry, {items[item_code]['name']} is out of stock.")
            continue
        
        # Asking user for money
        try:
            money = float(input(f"The price of {items[item_code]['name']} is {items[item_code]['price']}. Please enter your money: $"))
        except ValueError:
            print("Invalid input! Please enter a valid amount of money.")
            continue
        
        # Check if the user has enough money
        if not check_price(item_code, money):
            print(f"Insufficient funds. The price of {items[item_code]['name']} is {items[item_code]['price']}, but you entered only ${money}.")
            # Give the user another chance to input money
            continue
        
        # Calculate the change
        change = money - items[item_code]['price']
        print(f"Thank you for your purchase! You paid ${money}. Your change is ${change:.2f}.")
        
        # Dispense the item and update stock
        update_stock(item_code)
        
        # Suggest a complementary item
        suggest_item(item_code)
        
        # Ask if the user wants to buy another item
        continue_choice = input("Do you want to buy another item? (yes/no): ").lower()
        if continue_choice != 'yes':
            break
        
    print("Thank you for using the vending machine!")

# Run the vending machine program
if __name__ == "__main__":
    main()