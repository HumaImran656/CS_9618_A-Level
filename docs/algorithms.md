---

# 🟠 6. `algorithms.md`

```markdown
# 🟠 Algorithms

## 📘 Concept: Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

**Practice**

Write a program to search for a number in a list.
