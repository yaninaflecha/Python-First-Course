#This is intended to ask the users name 
#Then remove whitespace from str andCapitalize user's name

name =input("What's your name?: ").strip().title()


#Split user's name into first name and last name
first, last = name.split(" ")

#And hen say them hello

print("hello", first)

#I can also solve it this way
#print(f"hello {name}")
#Style depends a lot on what you like
#BUt also what the company you work for expects

