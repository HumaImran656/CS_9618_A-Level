import random

print("random.randint:", random.randint(1,10))
# Generates one random integer between a and b (both included)
# ✔ Includes both 1 and 10
# ✔ Returns only ONE number
# ✔ Can repeat if used again

print("random.choice:", random.choice(range(0,101)))
names = ["Ali", "Ahmed", "Sara"]
print("random.choice with a string list:", random.choice(names))
print("random.choice with the string value-HELLO:",random.choice("HELLO"))
# Selects one random element from a list, tuple, or string.
# ✔ Picks only ONE element
# ✔ Can repeat
# ✔ Works with lists, strings, tuples
print("random.sample between 1-10:", random.sample(range(1,11), 3))
# Selects k unique random elements (no repetition).
# ✔ Selects multiple values
# ✔ No duplicates
# ✔ Does NOT change original list
# Very useful for:
    # # Lottery numbers
    # # Random student selection
    # # Unique random data
numbers = [1,2,3,4,5]
print("Before Shuffle:", numbers)
random.shuffle(numbers)
print("After Shuffle", numbers)
# Shuffles (mixes) the list randomly.
# It changes the original list.
# ✔ Rearranges the list
# ✔ Returns nothing (None)
# ✔ Modifies original list
# SUMMARY
# | Function    | Returns                  | Repetition     | Changes Original? |
# | ----------- | ------------------------ | -------------- | ----------------- |
# | `randint()` | One number               | Can repeat     | No                |
# | `choice()`  | One element              | Can repeat     | No                |
# | `sample()`  | Multiple unique elements | No repeat      | No                |
# | `shuffle()` | Nothing                  | Not applicable | YES               |





