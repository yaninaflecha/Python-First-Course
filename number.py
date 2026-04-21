while True:
    try:
        x = int(input("What's x?: "))
    except ValueError:
        print(" x is meant to be a number.")
    else:
        break
print("x is", x)
    
