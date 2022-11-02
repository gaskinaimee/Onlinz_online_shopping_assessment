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
                return height, width, depth
                break

        except ValueError:
            print("Please enter a number.")


def box_volume(height, width, depth):
    box_volume = height * width * depth
    print("The volume of the box is {}.".format(box_volume))

height = 0
width = 0
depth = 0
var1 = box_in_cm()

box_volume(var1[0],var1[1],var1[2])


