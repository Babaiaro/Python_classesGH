from definitions import dice_roll

time = int(input("How many time would you like to roll up?"))
if time == 1:
        dice_roll()
elif time == 2:
        dice_roll()
        dice_roll()
else:
        print("404")
