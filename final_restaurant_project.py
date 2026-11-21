
menu = {
    "pizza": 150,
    "burger": 120,
    "pasta": 100,
    "coke": 50,
    "cold coffee": 80,
    "normal coffee": 50,
    "ice tea": 40
}

print("================================")
print("   WELCOME TO FOOD PARADISE!")
print("================================")

print("\n--------- OUR MENU ---------")

for item, price in menu.items():
    print(f"{item.title():15} : Rs.{price}")

total_amount = 0
order_list = []

while True:

    print("\nPlace your order:")
    item = input("Enter the item name: ").lower()

    if item in menu:

        quantity = int(input("Enter quantity: "))

        amount = menu[item] * quantity
        total_amount += amount

        order_list.append((item, quantity, amount))

        print(f"\n{quantity} {item}(s) added successfully!")

    else:
        print("Sorry! This item is not available.")

    another_order = input("\nDo you want to order more? (yes/no): ").lower()

    if another_order != "yes":
        break

print("\n========== YOUR BILL ==========")

for item, quantity, amount in order_list:
    print(f"{item.title()} x {quantity} = Rs.{amount}")

print("--------------------------------")
print(f"Total Amount: Rs.{total_amount}")
print("================================")
print("Thank you for visiting!")
print("Have a wonderful day!")
