ClassSize=3
SubjectNo=2
Distinction=0
Merit=0
Pass=0
Fail=0
# Setting up arrays
StudentName=["Hina", "Ahmed","Asif"]
StudentMarks = [[40,65],[60,45],[63,54]]
total=[0 for Row in range(ClassSize)]
Average=[0.0 for Row in range(ClassSize)]
# Setting up the values in arrrays

for Row in range(ClassSize):
    for column in range(SubjectNo):
        total[Row]=total[Row]+StudentMarks[Row][column]
        Average[Row]=int(total[Row]/SubjectNo)


for Row in range(ClassSize):
    print(f"{StudentName[Row]} has  TOTAL MARKS: {total[Row]} AVERAGE: {Average[Row]}")
    if Average[Row] >= 70:
        Distinction += 1
        print(f" {StudentName[Row]} has Grade: Distinction")

    elif Average[Row] >= 55 and Average[Row] < 70:
        Merit += 1
        print(f" {StudentName[Row]} has Grade: Merit")

    elif Average[Row] >= 40 and Average[Row] < 55:
        Pass += 1
        print(f" {StudentName[Row]} has Grade: Pass")

print("Total Distinctions: ", Distinction)
print("Merit: ", Merit)
print("Pass:", Pass)
print("Fail:", Fail)













