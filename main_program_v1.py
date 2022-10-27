

#Variables

#Functions
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    print(statement)


    return ""


#The box_in_cm function is a function made to calculate the altogether height, width and depth of the box.
def box_in_cm():
    box_in_cm = True
    while True:
        try:

            height = int(input("Hello! What is the height of the box in cm's?"))

            width = int(input("What is the width of the box in cm's?"))

            depth = int(input("What is the depth of the box in cm's?"))

            height_width_depth = height + width + depth

            if height_width_depth < 5:
                print("The dimensions of the box must be more than 5. Currently, it is {}.".format(height_width_depth))
            elif height_width_depth > 100:
                print("The dimensions of the box must be under 100. Currently, it is {}.".format(height_width_depth))
            else:
                print("The dimensions of the box is {}.".format(height_width_depth))
                break


            height_width_depth = height + width + depth

        except ValueError:
            print("Please enter a number.")



def base_rates():
    volume = input(question)

    if volume <= 6000:
        print("The bass rate for your package is $8.00.")

    elif volume > 6000 and volume < 100000:
        print("The base rate for your package is $12.00.")

    elif volume >= 100000:
        print("The base rate for your package is $15.00.")






#Main program
statement_generator("Welcome to Onlinz Online Shopping!", "*")
customers_name = input("What is your name?").title()
print("Hello, {}!")
box_in_cm()
