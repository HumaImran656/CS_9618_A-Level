# Write a Python program that asks the user to input 10 numbers.
# The program should:
        # Count how many of the entered numbers are positive
        # Calculate the total (sum) of all positive numbers
        # Display a message "Enter Number again" whenever a negative or zero value is entered
# After all inputs, display:
        # The number of positive values entered
        # The total sum of positive numbers
        # The average of the numbers entered
# -------------------------------------------------------------------------------------------
num=0
Total=0
x=0
count=0
for x in range(10):
     num=int(input("enter number:"))
     if num > 0 :
         count=count+1
         Total=Total + num
         avg=Total/10
     else:
         print("Enter Number again")
print("the pos numbers are:",count)
print("the total is",Total)
print("the avg is",avg)