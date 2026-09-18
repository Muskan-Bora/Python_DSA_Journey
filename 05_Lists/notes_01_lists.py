# ========================================================

# Lists 

"""
🐍 Python Lists — Notes

1. What is a List?

A list is an ordered collection of multiple values stored in a single variable.

fruits = ["apple", "banana", "mango"]

A list can contain different data types:

data = ["Muskan", 24, 5.6, True]
Key points
Ordered ✅
Indexed ✅
Mutable ✅
Allows duplicate values ✅
Can store different data types ✅

# -------------------------------------------
2. Creating a List

Use square brackets [].

numbers = [10, 20, 30, 40]

names = ["Muskan", "Rahul", "Priya"]

empty_list = []

Check type:

print(type(numbers))

Output:

<class 'list'>
"""

"""
3. List Indexing

Lists use zero-based indexing.
"""

fruits = ["apple", "banana", "mango"]

"""
| Index | Value  |
| ----: | ------ |
|     0 | apple  |
|     1 | banana |
|     2 | mango  |
"""

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango

# ======================

"""
4. Negative Indexing

Lists also support negative indexing.
"""

fruits = ["apple", "banana", "mango"]

"""
| Index | Value  |
| ----: | ------ |
|    -1 | mango  |
|    -2 | banana |
|    -3 | apple  |
"""

print(fruits[-1])  # mango
print(fruits[-2])  # banana

# ============================

"""
5. List Slicing

Same slicing concept as Strings:
"""

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

"""
Output: [20, 30, 40]
"""

"""
Remember:

start included, end excluded.

Other examples:


numbers[:3]     # [10, 20, 30]
numbers[2:]     # [30, 40, 50]
numbers[:]      # [10, 20, 30, 40, 50]
numbers[::2]    # [10, 30, 50]
numbers[::-1]   # [50, 40, 30, 20, 10]
"""

# =========================

"""
6. Lists are Mutable ⭐

This is one of the most important differences between Lists and Strings.

You can change an individual list element.
"""

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)

"""
Output:

['apple', 'orange', 'mango']
Remember:

String → immutable ❌

text[0] = "J"   # Error

List → mutable ✅

fruits[0] = "orange"
"""

# =========================