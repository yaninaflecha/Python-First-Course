#sys.argv is a list, recheck later
import sys

#Check for errors
if len(sys.argv) <2:
    sys.exit("Too few arguments") #sys.exit works to prevent the program to continue when we get in the exception

for arg in sys.argv[1:]: #Doing this I can have a slice from a list of elements to prevent printing "name.py"
    print("Hello, my name is", arg)
#elif len(sys.argv)>2:
    #sys.exit("Too many arguments")

#Print name tags
#print("hello, my name is", sys.argv[1])

#You can have multiple elif but not multiple else statements