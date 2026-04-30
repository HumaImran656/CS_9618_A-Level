password = "123"
x = input("Enter Password: ")
attempts = 3
inputs = 1
while x != password:
    print("Try again")
    x = input("Enter password:")
    inputs += 1 
    if inputs == attempts:
        print("No turns left")
        break
if x == password:
    print("Valid password ")
