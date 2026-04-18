def main():

    x = int(input("What's x?: "))
    if is_odd(x):
        print(x, "is odd")
    else:
        print(x, "is even")

def is_odd(n):
        return n%2


main() 
#If i do it this way it works because for ex. 
#2/2= 0 and 0=False for computers


def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print(x, "is even")
    else:
        print(x, "is odd")
   
    
def is_even(n):
        if n%2 ==0:
             return True
        else: 
             return False
        
#Pythonic way: return True if n%2 == 0 else False
#Or return n%2 == 0

main()