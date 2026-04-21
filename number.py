def main():
    x= get_int("What's x?: ") #I can ask here instead so my code is reusable
    print("x is", x)


def get_int(prompt):#Less hard coded this way
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            pass #I can use pass instead of putting a message here to keep looping the question
    
    
main() 
