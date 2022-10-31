def box_in_cm(values):
    box_in_cm = True
    while True:
        try:
            dimensions = int(input(values))


            height_width_depth = values
            if height_width_depth < 5:
                print("The dimensions of the box must be more than 5. Currently, it is {}.".format(height_width_depth))
            elif height_width_depth > 100:
                print("The dimensions of the box must be under 100. Currently, it is {}.".format(height_width_depth))
            else:
                break

        except ValueError:
            print("Please enter a number.")



height = box_in_cm("What is the height of the box in cm's?")
width = box_in_cm("What is the width of the box in cm's?")
depth = box_in_cm("What is the depth of the box in cm's?")
