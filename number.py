def main():
    x= get_int()
    print()
    print("x is", x)


def get_int():
    while True:
        try:
            x = int(input("What's x?: "))
        except ValueError:
            print(" x is meant to be a number.")
        else:
            break
    return x
    
main() 
