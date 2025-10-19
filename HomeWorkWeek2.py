#total bill amount
# tip percentage
# recipient
print ("Welcome to our restaurant.")

recipient_name  = input("May I know your name for order? ")
menu = input("Which menu would you like to see? \nWe have Kyrgyz, Italian and Turkish cuisines: ")
# list of variables that i use
name_of_menu = ""
cost_of_meal = int( )
order = " "
total = int()
# category of cuisines and menu in.
if menu == "Kyrgyz":
    order = print (input("Beshbarmak \nLagman\nManty \nSamsa\nKuurdak\n:"))
    # for dividing and price each i use if else statement
    if name_of_menu == "Beshbarmak, Kuurdak":
        cost_of_meal = 15
    else:
        cost_of_meal = 10
elif menu == "Turkish":
    order = print (input("Kebab \nİskender \nLahmacun \nPide \nBörek\n:"))
    if name_of_menu == "Kebab,Iskender":
        cost_of_meal = 12
    elif name_of_menu == "Lahmacun, Pide":
        cost_of_meal = 10
    else:
        cost_of_meal = 8
elif menu == "Italian":
    order = print(input("Pizza Margherita \nSpaghetti Carbonara \nLasagna\nRisotto\nRavioli \n:"))
    if name_of_menu == "Pizza Margherita, Lasagna":
        cost_of_meal = 12
    elif name_of_menu == "Spaghetti Carbonara, Risotto":
        cost_of_meal = 10
    else:
        cost_of_meal = 8
else:
    print(" ")

# This is the 4 week task
# i would like to add here if they want to split the payment
# and if they added 20%< tips i will print  "Thank you for your generosity!"
# also there i need to ask their names to receipt
# add show there how much are they gonna pay



if cost_of_meal > 0:
    # here i need to ask if they want to split the payment
    split_payment = input("Would you like to split payment? ")
    if split_payment == "Yes":
        number_to_split = float(input("how many do i need to split? "))
        # print(number_to_split)
        # split_payment.count(number_to_split)
        names_for_receipts = input("May i know names for check? ")
        # print(names_for_receipts)




    # here i use formula of calculation of percentage
    tip_percentage = float(input("Enter the tip percentage \n: "))

    tip_amount= tip_percentage * cost_of_meal/100
    if tip_percentage <= 20: print("Thank you for your generosity!")
    total= cost_of_meal + tip_amount
    total = total / number_to_split
    print(names_for_receipts, "total is", total, "for each")
