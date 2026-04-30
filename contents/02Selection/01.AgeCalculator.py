# AGE CALCULATOR
# Write a program to:
# - Input age
# - If age is less than 13 then output "Child"
# - If age is between 13 and 19 then output "Teenager"
# - If age is 20 or more then output "Adult"

age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")
