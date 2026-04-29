DataArray=[0 for Row in range(5)]
total=0
num=0
for count in range(5):
    num = int(input(f"Enter {count} number:"))
    while num <1 or num >50:
        print("invalid number entered")
        num=int(input(f"Enter {count} number:"))

    DataArray[count]=num
    total=total+DataArray[count]
print(f"The total of the numbers:{total}")
#for count in range(5):
print(DataArray)