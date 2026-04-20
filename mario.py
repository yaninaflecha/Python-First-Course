def main():

    print_row(4)
    print_column(3)
    print_square(3)

def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?"*width)

def print_square(size):
    #For each row in square
    for i in range(size):

    #For each brick in the row
        for j in range(size):

            #Print brick
            print("#", end="")

        print()

    #CAN BE DONE ALSO LIKE:
    #for i in range(size)
    #   print("#" * size)
main()


