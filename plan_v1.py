#This is an overview of the main plan for this assessment.

#1: Welcome the user to the online shopping.
print("Welcome to Onlinz Online Shopping!")

#2: Ask the user for their name. This can be added into step one if desired.
users_name = input("What is your name?").title()

#3: Say hello to the user, ask if they would like to return item.
return_item = input("Hello, {}! Would you like to return an item? Y/N.".format(users_name)).lower()

#4: If the user says yes, ask them for the size of their box. NEEDS TO BE A FUNCTION.
if return_item == "y":
    height = int(input("What is the height of the box in cm's?"))
    width = int(input("What is the width of the box in cm's?"))
    depth = int(input("What is the depth of the box in cm's?"))
else:
    print("Please go to the Onlinz Online Website for more information.")

#5: Calculate th


