menu = {
    "Pizza": 900,
    "Burger": 500,
    "Pasta": 700,
    "Sandwich": 400,
    "Salad": 300,
    "Juice": 200,
    "Coffee": 150,
}

print("Welcome to the Restaurant!")
print("Menu:\n Pizza: 900\n Burger: 500\n" \
" Pasta: 700\n Sandwich: 400\n Salad: 300\n " \
"Juice: 200\n Coffee: 150")

total_bill = 0
item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    total_bill = total_bill + menu[item_1]
    print(f"{item_1} Has been added to your order")
else:
    print("Sorry, we don't have that item on the menu.")

item_2 = input("Enter the second item you want to order: ")
if item_2 in menu:
    total_bill = total_bill + menu[item_2]
    print(f"{item_2} Has been added to your order")
else:
    print("Sorry, we don't have that item on the menu.")
print(f"Your total bill is: {total_bill}")