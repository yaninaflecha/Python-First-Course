def main():

    
    meow(get_number()) #this is what i did
    #this is how the teacher did it
    #Teacher's way is safer and easier to read
    number= get_number()
    meow(number)

def get_number():

    while True:
        counter= int(input("What's the value of the counter?"))
        if counter >0:
            return counter

def meow(n):
    for _ in range(n):
        print("Meow")
main()