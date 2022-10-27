#The box_in_cm function is a function made to calculate the altogether height, width and depth of the box.
def box_in_cm():
    box_in_cm = True
    while True:
        try:

            height = int(input("What is the height of the box in cm's?"))

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

box_in_cm()
