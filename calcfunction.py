def main():
    x = int(input("What's x? "))
    print("X squared is: ", square(x))

def square(n):
    x= n*n
    return(x)

main() 
#In the way I did it, i created a variable to store
#The result of the square and then return
#But teacher did it differently and actually
#Is quicker 
#return n ** 2
