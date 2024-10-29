names = ["Slim", "Jym", "Ogwa"]
names.append(40)

studentMarks = {
    "Kiswahili": 70
}

studentMarks["Maths"] = 90
studentMarks["English"] = 80

total = 0

for subject in studentMarks:
    total += studentMarks[subject]

average = total / len(studentMarks)
print(average)