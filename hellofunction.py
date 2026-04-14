def hello():
    name = input("What's your name? ").title().strip()
    print("Hello",name, "!")

hello()

#This is the way the teacher did it 
def hello(to ="World"):
    print("hello", to)
hello() #If theres nothing inside, it'll say hello world
name = input("What's your name?")
hello(name)

#In my version, the "name" only lives inside the 
#function, while teacher's version is declared in 
#the body of the function and also the function
#will work always doesn't matter where it resides


#Using "main" is a convention in python
#It is used for storing the entry point

def main():
    name = input("What's your name? ")
    hello(name)

def hello (to="world"):
    print("hello", to)
    
main()