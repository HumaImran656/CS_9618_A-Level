CHOICE = str(input("What do you want to convert to?(C/F) "))
TEMPINPUT = int(input("Enter The Temperature --> "))
if CHOICE == "C":
    print("Temperature in Fahrenheit",(TEMPINPUT*(9/5))+32)
elif CHOICE == "F":
    print("Temperature in Celsius",(5/9)*(TEMPINPUT-32))
else:
        print("Sorry, Something went wrong. Please try again."
          "(Maybe try writing Celsius or Fahrenheit properly)")
