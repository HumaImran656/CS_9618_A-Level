x = 0
while x < 5:
  print("Loop Executed " + str(x))
  x = x + 1
print("Outside the Loop " + str(x))

# Table of 5
# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1.
# The "result" variable is initialized with the value of the
# "multiplier" variable times 5.

multiplier = 1
result = multiplier*5
while result <= 50:
  print(f"5 * {multiplier} = {result}")
  multiplier += 1
  result = multiplier*5
print("Done")
