import random
import string

lowercase_letters = string.ascii_lowercase
cappital_letters = string.ascii_uppercase
all_letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

def all_funck(a,b, c, v):
    return a + b + c + v

def random_generate():   
    while True:
        try:
            lenth = int(input("Enter length"))
            if lenth <= 0:
                continue
            break
        except ValueError:
            print("Numbers only")
            continue
    all =  all_funck(lowercase_letters, cappital_letters, digits, punctuation)
    while True:
        for i in range(lenth):
            generate = random.choice(all)
            print(generate, end= '')            
        print("\n Password Generated")
        now = input("Generated more: yes/no")
        if now == "no":
            print("Exit")
            break

def choise_generate():
    while True:
        try:
            lenth = int(input("Enter length"))
            if lenth <= 0:
                continue
            break
        except ValueError:
            print("Numbers only")
            continue

    while True:
        print()
        print(" letters and numbers - 1, numbers and special characters - 2, special characters and letters - 3, only numbers - 4, only special characters - 5, only letters - 6 ")
        try:
            way = int(input("Select a password creation method"))
        except ValueError:
            print("Only numbers")
            continue
        if way == 1:
            first = all_letters + digits
            for i in range(lenth):
                generate_first = random.choice(first)
                print(generate_first, end = '')
        elif way == 2:
            second = digits + punctuation
            for i in range(lenth):
                generate_first = random.choice(second)
                print(generate_first, end = '')
        elif way == 3:
            thidly = all_letters + punctuation
            for i in range(lenth):
                generate_first = random.choice(thidly)
                print(generate_first, end = '')              
        elif way == 4:
            for i in range(lenth):
                generate_first = random.choice(digits)
                print(generate_first, end = '')             
        elif way == 5:
            for i in range(lenth):
                generate_first = random.choice(punctuation)
                print(generate_first, end = '')
                        
        elif way == 6:
            for i in range(lenth):
                generate_first = random.choice(all_letters)
                print(generate_first, end = '')
        elif way < 1 or way > 6:
            print("Wrong action")
        
        print("\n The password has been generated")
        again = input("Generate more? (yes/no): ").lower()
        if again != "yes":
            print("Exit.")
            break
while True:
    print()
    try:
        call = int(input("Select a password creation method (Custom = 1, All characters together = 2) Press 0 to exit the program "))
    except ValueError:
        print("Only Numbers")
        continue
    if call == 2:
        random_generate()
    elif call == 1:
        choise_generate()
    elif call == 0:
         break



 
