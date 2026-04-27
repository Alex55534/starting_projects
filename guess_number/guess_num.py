import random
print("Good afternoon")
start_playing = input("You want to play this game? Yes/No?")
while True:
    if start_playing == "No":
        print("Best wishes")
        break
    else:
        print("Fine, Let's go")
        print("I give you a number from 1 to 10, and you need to guess it.")
    randomat = random.randint(1, 10)
    num = 0
    while num < 3:
        try:
            answer = int(input(f"You have left {3 - num} attemps"))
        except ValueError:
            print("You can't enter this letters")
            continue
        if answer == randomat:
            ans = ["Yes, we won", "You are so great, this is the right answer.", "You clearly have the gift of clairvoyance."]
            random_number = random.choice(ans) 
            print(random_number)
            break
        else:
            num += 1
    if num == 3:
        print("Ohh, sorry, but you lose")
    more_one = input("Do you want playing again?Yes/No")
    if more_one =="No":
        print("Good wishes")
        break


    
    


    