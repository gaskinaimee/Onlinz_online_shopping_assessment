#Functions

#Variables
customers_name = input("What is your name?").title()

#The box_in_cm function is a function made to calculate the altogether height, width and depth of the box.
def box_in_cm():
    height_width_depth = []
    box_in_cm = True
    while True:
        try:
            height = int(input("What is the height of the box in cm's?"))
            if height < 5:
                print("Sorry, the height of the box must be more than 5 cm's. Currently, it is {}.".format(height))
            else:
                height_width_depth.append(height)
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            width = int(input("What is the width of the box in cm's?"))
            if width < 5:
                print("Sorry, the width of the box must be more than 5 cm's. Currently, it is {}.".format(width))
            else:
                height_width_depth.append(width)
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            depth = int(input("What is the depth of the box in cm's?"))
            if depth < 5:
                print("Sorry, the depth of the box must be more than 5 cm's. Currently, it is {}.".format(depth))
            else:
                height_width_depth.append(depth)
                break
        except ValueError:
            print("Please enter a valid number.")

def box_volume():
    box_volume = height * width * depth

def base_rates():
    volume = input(question)

    if volume <= 6000:
        print("The bass rate for your package is $8.00.")

    elif volume > 6000 and volume < 100000:
        print("The base rate for your package is $12.00.")

    elif volume >= 100000:
        print("The base rate for your package is $15.00.")

#Main program
box_in_cm()

box_volume()
