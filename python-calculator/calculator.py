import math

def add(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiply(a, b):
    return a * b
def devision(a, b):
    if b == 0:
        return None
    return a / b
def deg(a, b):
    return a ** b
def sqrte(n):
    if n < 0:
        return None
    else:
        return math.sqrt(n)

def function_calculator():
    results = []
    while True:
        while True:
            try:
                number1 = float(input("Request number "))
                break
            except ValueError:
                print("You can't enter anything but numbers.")


        action = input("Select action (+, -, /, *, **, s-Request root: ")

        while True:
            try:
                number2 = float(input("Request number "))
                break
            except ValueError:
                print("You can't enter anything but number")

        if action == "+":
            adding = add(number1, number2)
            results.append(adding)
            print(adding)
        elif action == "-":
            subtraction1 = substraction(number1, number2)
            results.append(subtraction1)
            print(subtraction1)            
        elif action == "s":
            if number1 < 0 or number2 < 0:
                print("You cannot take the root of a negative number.")
            else:
                while True:
                    try:
                        which = int(input("What number should I take the square root of? 1/2?"))
                    except ValueError:
                        print("Only nombers")
                        continue                
                    if which == 1:
                        radix1 = sqrte(number1)
                        results.append(radix1)
                        print(radix1)
                        break
                    if which == 2:
                        radix2 = sqrte(number2)
                        results.append(radix2)
                        print(radix2)
                        break
        elif action =="**":
            degree = deg(number1, number2)
            results.append(degree)
            print(degree)
        elif action == "/":
            if number2 == 0:
                print("You can't divide by zero")
            else:
                division1 = devision(number1, number2)
                results.append(division1)
                print(division1)
        elif action == "*":
            multiplication = multiply(number1, number2)
            results.append(multiplication)
            print(multiplication)
        else:
            print("Unknown action")
        
        choice = input("If you want to continue choice yes/no").lower()
        if choice =="no":
            break
    print("Here are your results", results)

call = input("do you want to use a calculator? yes/no ").lower()
if call == "yes":
    function_calculator()
else:
    print("Good day")




