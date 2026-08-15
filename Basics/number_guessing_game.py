import random

num = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess the number: "))
    
    if(guess == num):
        tries += 1
        print(f"You guess the right number which is {num}\nYou guessed the number in {tries} try\n")
        break
    elif(guess > num):
        tries += 1
        print("The guess was wrong...\nThe number is little lower\n")
    else:
        tries += 1
        print("The guess was wrong...\nThe number is little higher\n")