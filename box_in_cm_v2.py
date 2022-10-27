#The box_in_cm function is a function made to calculate the altogether height, width and depth of the box.
def box_in_cm(height, width, depth):
    height_width_depth = []
    box_in_cm = True
    while True:
        try:
            if height < 5:
                print("Sorry, the measurements of the box must not be lower than 5cm's.")
            else:
                height_width_depth.append(height)
                break

            if width < 5:
                print("Sorry, the measurements of the box must not be lower than 5cm's.")
            else:
                height_width_depth.append(width)
                break

            if depth < 5:
                print("Sorry, the measurements of the box must not be lower than 5cm's.")
            else:
                height_width_depth.append(depth)
                break
        except ValueError:
            print("Please enter a valid number.")
