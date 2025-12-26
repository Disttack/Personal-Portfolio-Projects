print("Welcome to the rollercoaster!")
height = int(input("How tall are you in inches?"))
bill = 0

if height >= 60:
    print("You may ride!")
    age = int(input("How old are you?"))
    if age >= 45 and age <= 55:
        print("Free midlife crisis ticket!")
        bill = 0
    elif age >= 18:
        print("Adult tickets will be 10 dollars")
        bill = 10
    elif age >= 14:
        print("Youth tickets will be 7 dollars")
        bill = 7
    else:
        print("Child tickets will be 5 dollars")
        bill = 5
    
    wants_photo = input("Would you like your photo taken? Type Y for yes and N for no.")
    if wants_photo == "Y":
        bill += 3
        # += is the same as bill = bill + 3
    print(f"Your final bill is ${bill}")
else:
    print("You will need to wait until you are taller!")