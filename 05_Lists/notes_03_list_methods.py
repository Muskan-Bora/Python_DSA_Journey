## ================================== ##

# List - Methods

"""
🐍 PYTHON LIST METHODS

A list method is a function that belongs to a list object.

We call a list method using dot notation:

    list_name.method()

Example:

    numbers.append(40)


Main List Methods:

1. Adding Elements
   - append()  → adds one element at the end
   - insert()  → adds one element at a specific index
   - extend()  → adds multiple elements

2. Removing Elements
   - remove()  → removes an element by value
   - pop()     → removes an element by index
   - clear()   → removes all elements

3. Searching / Counting
   - index()   → finds the index of a value
   - count()   → counts how many times a value appears

4. Ordering
   - sort()    → sorts the original list
   - reverse() → reverses the original list

Important:
We will learn each method through:
    What → How → When to use → Difference → Practice
"""

# ======================================

"""
🟢 List Problem 17 — append()
First understand the purpose

append() is used when you want to:

Add ONE new element to the end of a list.

For example, conceptually:

[10, 20, 30]
       ↓ append 40
[10, 20, 30, 40]
Your task

Create:

numbers = [10, 20, 30]

Add 40 to the end of the list using the appropriate list method.

Then print the list.
"""

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)   

"""
Output:
[10, 20, 30, 40]
"""

"""
🧠 What you've learned

append():

Adds one element ✅
Adds it to the end of the list ✅
Changes the original list ✅
Increases the list length by 1 ✅

So:

Before → [10, 20, 30]
After  → [10, 20, 30, 40]
"""

# ====================================

"""
🟢 List Problem 18 — append() with Different Data Types

Now let's make sure you understand that append() can add different types of values, not just numbers.

Create:

items = ["Python", 24, True]

Then use append() to add:

5.5

Print the updated list.

Expected output
["Python", 24, True, 5.5]
"""

print()

items = ["Python", 24, True]

items.append(5.5)

print(items)

"""
Output:
['Python', 24, True, 5.5]
"""

# =============================================

"""
🟢 List Problem 19 — append() and List Length

Now let's connect append() with something you already learned: len().

Create:

numbers = [10, 20, 30]

Then:

Print the length of the list.
Use append() to add 40.
Print the length again.
Print the final list.
Expected output
3
4
[10, 20, 30, 40]
"""

print()

numbers = [10, 20, 30]

print(numbers)           # Output of original list elements [10, 20, 30]

print(len(numbers))      # Length is 3 before append 

numbers.append(40)       # Added the new element in the list

print(len(numbers))      # Length is 4 after new element got added

print(numbers)           # Output after new element added - [10, 20, 30, 40]

# ===============================

"""
🟢 List Problem 20 — append() vs Adding Multiple Values

Now we're going to learn something very important about append().

Create:

numbers = [10, 20, 30]

Use one append() call to add these two values:

40, 50

Then print the list.

Expected output
[10, 20, 30, [40, 50]]
"""

print()

numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)

"""
Output:
[10, 20, 30, [40, 50]]
"""

# ==============================