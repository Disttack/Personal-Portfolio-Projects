choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
drink = False
water = 300
milk = 200
coffee = 100
money = 0

while drink == False:
    if choice == "espresso":
        print("Here is your espresso. ☕️")
        drink = True
    elif choice == "latte":
        print("Here is your latte. ☕️")
        drink = True
    elif choice == "cappuccino":
        print("Here is your cappuccino. ☕️")
        drink = True
    elif choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        drink = True
    else:
        choice = input("Invalid choice. Please choose again (espresso/latte/cappuccino): ").lower()