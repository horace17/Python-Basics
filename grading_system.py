def addMarks():
    subjects = {}
    total_marks = 0
    def recordMarks(noOfSubjects):
        total = 0
        for i in range(1, noOfSubjects + 1):
            name = input(f"Enter name of subject {i}: ")
            while True:
                try:
                    marks = int(input(f"Enter marks of subject {i}: "))
                    if marks >= 0 and marks <= 100:
                        break
                    else:
                        print("The marks should range 0 - 100")
                except ValueError:
                    print("The marks should be an integer")
            subjects[name] = marks
            total += marks
        return total

    try:
        noOfSubjects = int(input("Enter no of subjects: "))
        total_marks = recordMarks(noOfSubjects)
    except ValueError:
        print("The number of subjects must be an integer")
        exit()


    average = total_marks / len(subjects)
    subjects["Total marks"] = total_marks
    subjects["Average"] = int(average)

    print(subjects)