fnum = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
snum = float(input("Enter second number: "))

def calculator(fnum, snum, operator):
    if operator == '+':
        return fnum + snum
    elif operator == '-':
        return fnum - snum
    elif operator == '*':
        return fnum * snum
    elif operator == '/':
        return fnum / snum
    else:
        return "Invalid operator"   

result = calculator(fnum, snum, operator)
print(f"The result is: {result}")

cont = input("Do you want to perform another calculation? Type 'yes' or 'no': ").lower()
while cont == 'yes':
    fnum = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    snum = float(input("Enter second number: "))
    result = calculator(fnum, snum, operator)
    print(f"The result is: {result}")
    cont = input("Do you want to perform another calculation? Type 'yes' or 'no': ").lower()