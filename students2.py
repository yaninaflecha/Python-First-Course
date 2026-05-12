import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students2.csv", "a", newline= "") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])

    if file.tell() == 0:
        writer.writeheader()
    writer.writerow({"name": name, "home": home})