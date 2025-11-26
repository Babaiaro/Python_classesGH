# Dice Rolling Simulator. Use the random module to create a function that
# simulates rolling two six-sided dice and returns their sum.
# Then, create a program that asks the user how many times to roll the dice
# and uses a dictionary to track and display the frequency of each sum.

from definitions import dice_roll

dice_roll()

while True:
            a = input("\nWould you like to roll dice again? (y/n)")
            if a == "y":
                dice_roll()

            elif a == "n":
                break
            else 
                 print("OLA")
                        











