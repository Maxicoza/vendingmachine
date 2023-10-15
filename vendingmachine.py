# import the modules
import time
import random

# initialize the bank and coins variables
bank = 6
coins = 0

# Define a list of items available in the vending machine
items = [
    # Each item is represented as a dictionary with item_id, item_name, item_price, item_quantity
    {   "item_id": 3,
        "item_name": "Coca-Cola",
        'item_price': 2,
        "quantity": 0,
    },
    {
        "item_id": 1,
        "item_name": "Sprite",
        'item_price': 2,
        "quantity": 2,
    },
    {
        "item_id": 2,
        "item_name": "Fanta",
        'item_price': 2,
        "quantity": 2,
    },
    {
        "item_id": 3,
        "item_name": "Orange Juice",
        'item_price': 1,
        "quantity": 1,
    },
    {
        "item_id": 4,
        "item_name": "Doritos",
        'item_price': 3,
        "quantity": 2,
    },
    {
        "item_id": 5,
        "item_name": "Cheetos",
        'item_price': 3,
        "quantity": 1,
    },
    {
        "item_id": 6,
        "item_name": "Popcorn",
        'item_price': 4,
        "quantity": 3,
    },
    {
        "item_id": 7,
        "item_name": "Sour Patch Kids",
        'item_price': 4,
        "quantity": 2,
    },
    {
        "item_id": 8,
        "item_name": "Bubble Gum",
        'item_price': 1,
        "quantity": 3,
    },
    {
        "item_id": 9,
        "item_name": "Skittles",
        'item_price': 3,
        "quantity": 3,
    },
    {
        "item_id": 10,
        "item_name": "KitKat",
        'item_price': 2,
        "quantity": 4,
    },
    {
        "item_id": 11,
        "item_name": "Aero Bar",
        'item_price': 3,
        "quantity": 4,
    },
    {
        "item_id": 12,
        "item_name": "Snickers Bar",
        'item_price': 2,
        "quantity": 4,
    },
    {
        "item_id": 13,
        "item_name": "Twix Bar",
        'item_price': 2,
        "quantity": 3,
    },
    {
        "item_id": 14,
        "item_name": "Water",
        'item_price': 1,
        "quantity": 6,
    }
]

the_item = [] # Initialize an empty list to store selected items
acceptedchoices = ["yes", "no"] # Define accepted choices for transactions

run = True # Initialize a variable to control the vending machine run state

# Function to display the available items for purchase
def display_menu():
    print("Here's what's available to be purchased:")
    print("")
    for i in items:
        print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
    print("")


# Function to generate a random bonus
def generate_random_bonus():
    return random.randint(1, 10)

# Function to add a bonus to the bank
def add_bonus_to_bank(bank, bonus):
    print(f"You got a bonus of {bonus} dollars!")
    return bank + bonus

# Function to dispense an item to the user
def dispense():
    global items
    global bank
    selected_item = items[buy_item]

    if selected_item["quantity"] > 0:
        print(f"You have selected {selected_item['item_name']}.")
        print("Amount due is:",selected_item['item_price'],"dollars")
        print("You currently have", (bank), "dollars in your pocket")
        transaction = input("Enter 'yes' to proceed and enter 'no' to cancel transaction: ").lower()

        if transaction == acceptedchoices[0]:
            if bank >= selected_item['item_price']:
                items[buy_item]["quantity"] -= 1
                bank -= selected_item['item_price']
                print(f"You now have {selected_item['item_name']}.")
                print(f"Thank you for your purchase!")
                print("Your money in your pocket is", (bank), "dollars")
            else:
                print("Insufficient funds. Transaction canceled.")
                print("Options:")
                print("1. Type 'money' to add money to your pocket")
                print("2. Type 'quit' to exit")

                user_input = input("Enter your choice: ").lower()

                time.sleep(1)
                if user_input == 'money':
                    bonus = generate_random_bonus()

                    bank = add_bonus_to_bank(bank, bonus)
                    print(f"Your money in your pocket is now: {bank} dollars")

                if user_input == 'quit':
                    vendingmachine(items, run, the_item)

        elif transaction == acceptedchoices[1]:
            print("You have cancelled the transaction")
            time.sleep(1)
            display_menu()
            vendingmachine(items, run, the_item)
        else:
            print("Invalid choice.")
    else:
        print("Sorry, this item is out of stock.")


# Function to operate the vending machine
def vendingmachine(items, run, the_item):
    global bank
    acceptableCoins = [1, 2, 3, 4,5]
    while run:
        display_menu()
        global buy_item
        buy_item = int(input(" Enter the item code of the product you want to buy: "))

        if buy_item < len(items):
            the_item.append(items[buy_item])
            dispense()
        else:
            print("Invalid item code. Please try again.")

# Print a welcome message for the vending machine
print("Hello! Welcome to Max's Vending Machine!")

# Start the vending machine
vendingmachine(items, run, the_item)
