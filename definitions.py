import time
import random

def dice_roll_loading():
    lines = [
        ("\n-----------------------",0.05),
    ]
    delays_after_line = [0.5]*len(lines)
    for i, (lines, char_delay) in enumerate(lines):
        for char in lines:
            print(char,end="",flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(delays_after_line[i])
if __name__ == "__main__":
    dice_roll_loading()


def dice_rolling():
    dice_random_number1 = random.randrange(1, 7)
    dice_random_number2 = random.randrange(1, 7)

def dice_roll(total):

        dice_roll_loading()
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        print("Your first dice roll number is " + str(dice1))
        dice_roll_loading()
        print("Your second dice roll number is " + str(dice2))
        total = dice1 + dice2
        dice_roll_loading()
        print("\nYour total dice roll number is " + str(total))