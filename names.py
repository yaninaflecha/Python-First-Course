#Method 1.

#names = []
#for _ in range(3):
    #name = input("What's your name? ")
    #names.append(name)

#for name in sorted(names):
    #print(f"Hello, {name}")

#Method 2:
#name = input("What's your name? ")
#with open("names.txt", "a") as file:
    #file.write(f"{name}\n")

#Method 1 to read the file:
with open("names.txt") as file:
    for line in sorted(file, reverse= True):
        print("hello, ", line.rstrip())
#Method 2:
#names = []
#with open("names.txt") as file:
    #for line in file:
        #names.append(line.rstrip())
#for name in sorted(names):
    #print(f"hello, {name}")

