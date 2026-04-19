students = ["Hermione", "Harry", "Ron"]

for student in students: #I'm not using range because its a list of integer
    print(student)

#ANOTHER WAY
for i in range(len(students)):
    print(i +1, students[i])

