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

"""
7. Adding Elements
append()

Adds one item at the end.
"""

fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)

"""
Output:

['apple', 'banana', 'mango']
"""

"""
insert()

Adds an item at a specific index.
"""

fruits = ["apple", "mango"]

fruits.insert(1, "banana")

print(fruits)

"""
Output:

['apple', 'banana', 'mango']
"""

"""
extend()

Adds multiple elements from another collection.
"""

fruits = ["apple", "banana"]

fruits.extend(["mango", "orange"])

print(fruits)

"""
Output:

['apple', 'banana', 'mango', 'orange']
"""

# ================================

"""
8. Removing Elements
remove()

Removes a specific value.
"""

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

"""
Result:

['apple', 'mango']
"""

"""
pop()

Removes an element using its index and returns the removed value.
"""

fruits = ["apple", "banana", "mango"]

removed = fruits.pop(1)

print(removed)
print(fruits)

"""
Output:
banana
['apple', 'mango']
"""

# Without an index:

# fruits.pop()

# removes the last element.

"""
clear()

Removes everything.
"""

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

"""
Output:

[]
"""

# ===========================

"""
9. Useful List Methods
count()

Counts how many times a value appears.
"""

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

"""
Output:

3
"""

"""
index()

Finds the first position of a value.
"""

fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))

"""
Output:

1
"""

"""
sort()

Sorts the original list.
"""

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

"""
Output:

[10, 20, 30, 40]
"""

"""
Descending:
"""

# numbers.sort(reverse=True)

"""
reverse()

Reverses the original list.
"""

numbers = [10, 20, 30]

numbers.reverse()

print(numbers)

"""
Output:

[30, 20, 10]
"""

# ========================

"""
10. Traversing a List

You can loop through every element.
"""

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

"""
Output:

apple
banana
mango
"""

# You can also use indexes:

for i in range(len(fruits)):
    print(fruits[i])

# =======================

"""
11. len() with Lists
"""

fruits = ["apple", "banana", "mango"]

print(len(fruits))

"""
Output:

3

len() tells you how many elements are in the list.
"""

# ========================


"""
12. Checking Membership

Use in and not in.
"""

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)

"""
Output:

True
"""

print("orange" not in fruits)
"""
Output:

True
"""

# ======================================

"""
🧠 Most Important Mental Model

Remember Lists like this:

LIST
 │
 ├── Ordered
 ├── Indexed
 ├── Sliceable
 ├── Mutable ⭐
 ├── Allows duplicates
 ├── Iterable
 │
 ├── Add
 │    ├── append()
 │    ├── insert()
 │    └── extend()
 │
 ├── Remove
 │    ├── remove()
 │    ├── pop()
 │    └── clear()
 │
 └── Useful
      ├── count()
      ├── index()
      ├── sort()
      └── reverse()
"""