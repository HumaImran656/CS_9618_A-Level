ClassSize = 3
SubjectNo = 3

Distinction = 0
Merit = 0
Pass = 0
Fail = 0

StudentName = ["" for _ in range(ClassSize)]
StudentMarks = [[0 for _ in range(SubjectNo)] for _ in range(ClassSize)]

for Row in range(ClassSize):

    StudentName[Row] = input(f"Enter the name of student {Row+1}: ")

    total = 0

    for Column in range(SubjectNo):
        mark = int(input(f"Enter mark of Subject {Column+1}: "))
        StudentMarks[Row][Column] = mark
        total += mark

    average = total / SubjectNo

    print(f"\n{StudentName[Row]} has TOTAL MARKS: {total} AVERAGE: {average}")

    if average >= 70:
        Distinction += 1
        print("Grade: Distinction")

    elif average >= 55:
        Merit += 1
        print("Grade: Merit")

    elif average >= 40:
        Pass += 1
        print("Grade: Pass")

    else:
        Fail += 1
        print("Grade: Fail")

print("\nTotal Distinctions:", Distinction)
print("Merit:", Merit)
print("Pass:", Pass)
print("Fail:", Fail)
