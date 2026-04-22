from random import choice #Using FROM i dont need to keep typing random.choice each time i need it
#but then I must avoid use variables or functions with the same kayword "choice"
from random import randint
from random import shuffle


coin= choice(["heads", "tails"])
print(coin)

number= randint(1,10)
print(number)

cards= ["jack", "queen", "king"]
shuffle(cards) #Shuffle helps mix the items from a list
for card in cards:
    print(card)