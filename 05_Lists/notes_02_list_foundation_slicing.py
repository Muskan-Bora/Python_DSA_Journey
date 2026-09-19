# ==========================================================

# List Problems

"""
🟢 List Problem 1 — Creating a List

Create a Python list called fruits containing these three values:

Apple
Banana
Mango

Then print the list.
"""
print()

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

"""
Output:
['Apple', 'Banana', 'Mango']
"""

# ================================

"""
🟢 List Problem 2 — Creating Different Lists

Create three lists:

numbers containing 10, 20, 30, 40
names containing "Muskan", "Rahul", "Priya"
empty_list containing nothing

Then print all three lists.
"""

print()

numbers = [10, 20, 30, 40]
names = ["Muskan", "Rahul", "Priya"]
empty_list = []

print(numbers)
print(names)
print(empty_list)

"""
Output:
[10, 20, 30, 40]
['Muskan', 'Rahul', 'Priya']
[]
"""

# =======================================

"""
🟢 List Problem 3 — Different Data Types

Now let's check an important List property.

Create a list called data containing:

"Python" → string
24 → integer
5.5 → float
True → boolean

Then print:

The complete list
The type of the list using type()
"""

print()

diff_data = ["Python", 24, 5.5, True]

print(diff_data, type(diff_data))   

"""
Output:
['Python', 24, 5.5, True] <class 'list'>
"""

# =======================================

"""
🟢 List Problem 4 — len()

Now we're moving to the next foundation concept: finding how many elements are in a list.

Create:

numbers = [10, 20, 30, 40, 50]

Then print the number of elements in the list using len().

Expected output
5
"""
print()

numbers = [10, 20, 30, 40, 50]

print(f"The length is {len(numbers)}")  # Output: The length is 5

# =======================