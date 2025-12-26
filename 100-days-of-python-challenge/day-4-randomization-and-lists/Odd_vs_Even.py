print("Odd or Even Check")
userdata = int(input("Please enter a number: "))
#all evens can be cleanly divided by 2, so even % 2 = 0
modulo = (userdata % 2)
if modulo == 0:
    print("Even")
else:
    print("Odd")
