#The box_in_cm function is a function made to calculate the altogether height, width and depth of the box.
def box_in_cm(height, width, depth):
    height_width_depth = []

    box_in_cm = True
    while True:
        try:
            for number in height_width_depth:
                if number < 5:
                    print("Sorry, the box must not be under 5cm's.")
                    break
                elif number > 100:
                    print("Sorry, the box must not exceed 100cm's.")
                else:
                    height_width_depth.append(height)
                    height_width_depth.append(width)
                    height_width_depth.append(depth)
        except ValueError:
            print("Please enter a number.")


#PUT IN LIST?

height = int(input("What is the height of the box in cm's?"))
width = int(input("What is the width of the box in cm's?"))
depth = int(input("What is the depth of the box in cm's?"))

box_in_cm(height, width, depth)
