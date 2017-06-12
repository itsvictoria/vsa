# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

variable_name = random.randint (1,9)
print(variable_name)
user_num = raw_input("What number am I thinking of? ")

if str(user_num) == "exit":
    print("Okay, have a great day!")

user_num = int(user_num)

    if int(user_num) == variable_name:
        print("Good job, you  got it right!")

else:
    user_num = int(user_num)

    if user_num == variable_name:
        print("Good job, you  got it right!")

    while user_num != variable_name:
        user_num = int(user_num)
        print("Sorry, you didn't get it.")
        if user_num > variable_name:
            print("Here's a hint: it's too high.  Guess again! ")
        if user_num < variable_name:
            print("Here's a hint: it's too low.  Guess again! ")
        user_num = raw_input("What number am I thinking of? ")
        if user_num == "exit":
            print("Okay, have a great day!")
            break

    if user_num == variable_name:
        print("Good job, you  got it right!")
