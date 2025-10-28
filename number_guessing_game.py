# Number Guessing Game.The program chooses a secret random number between 1 and 100.
# The user has a limited number of attempts to guess it. After each guess,
# the program tells the user if their guess was "too high," "too low," or "correct."
import random

randon_number = random.randrange(0,100)
# number guessing function
# print (randon_number)
print("Hi welcome to number guessing game! You have a 3 attempt")


for access in range (0,3):
# here for for 3 in range to repeat 
    user_number = float(input("write here your number: "))
    if randon_number == user_number:
        print("you are right! the randon number is %d" % (randon_number))
        break
    elif randon_number < user_number:
        print("Too high")

    elif randon_number > user_number:
        print("Too low")

    else:
        print("404")
else:
    print("You are not correct")



