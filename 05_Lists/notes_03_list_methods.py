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

"""
🟢 List Problem 21 — extend()

Create:

numbers = [10, 20, 30]

Use extend() to add:

40, 50

Then print the list.

Expected output
[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)

"""
Output:
[10, 20, 30, 40, 50]
"""

# =======================================

"""
🟢 List Problem 22 — extend() with Different Data Types

Now let's make sure extend() isn't limited to numbers.

Create:

items = ["Python", 24]

Use extend() to add these three elements:

"Java", 5.5, True

Then print the final list.

Expected output
["Python", 24, "Java", 5.5, True]
"""

print()

items = ["Python", 24]

items.extend(["Java", 5.5, True])

print(items)

"""
Output:
['Python', 24, 'Java', 5.5, True]
"""

# =============================================

"""
🟢 List Problem 23 — append() vs extend()

Now we're going to test whether you can choose the correct method, rather than just reproduce syntax.

Start with:

numbers = [10, 20, 30]

You want the final list to be:

[10, 20, 30, 40, 50]
Your task

Add 40 and 50 to the end of the list.

You must use one method call.

The important part: decide yourself whether append() or extend() is appropriate.

Then print the final list.
"""

print()

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)          

"""
Output:
[10, 20, 30, 40, 50]
"""

# ========================================

"""
🟢 List Problem 24 — append() vs extend() — Your Decision

Now let's reverse the situation.

Start with:

items = ["Python", "Java"]

You want the final list to be:

["Python", "Java", ["C++", "JavaScript"]]
Your task

Add ["C++", "JavaScript"] as ONE element at the end of the list.
"""

print()

items = ["Python", "Java"]

items.append(["C++", "JavaScript"])
print(items)

"""
Output:
['Python', 'Java', ['C++', 'JavaScript']]
"""

# ====================================

"""
🟢 List Problem 25 — Basic insert()

Create:

numbers = [10, 20, 40, 50]

Insert 30 at index 2.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)   # Output: [10, 20, 30, 40, 50]

# ==========================================

"""
🟢 Problem 26 — insert() at the Beginning

Create:

numbers = [20, 30, 40, 50]

Insert 10 at the beginning of the list.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [20, 30, 40, 50]

numbers.insert(0, 10)
print(numbers)    # Output: [10, 20, 30, 40, 50]

# ==========================================

"""
List Problem 27 — insert() in the Middle

Create:

numbers = [10, 20, 40, 50]

Insert 30 between 20 and 40.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)      # Output: [10, 20, 30, 40, 50]

# ===================================

"""
🟢 List Problem 28 — append() vs insert()

Start with:

numbers = [10, 20, 30]

You need to add 40 at the end of the list.

Question: Should you use append() or insert()?
"""

print()

numbers = [10, 20, 30]

numbers.append(40)    # used append() because the question said You need to add 40 at the end of the list. so it means at the end 

print(numbers)  # Output: [10, 20, 30, 40]

# ==================================

"""
🟢 List Problem 29 — insert() vs append()

Start with:

items = ["Python", "Java", "C++"]

You need to add "JavaScript" between "Java" and "C++".

Question: Should you use append() or insert()?
"""

print()

items = ["Python", "Java", "C++"]

items.insert(2, "JavaScript")     # Here insert() used becaus ethe requirement was the elemnet should be add between "Java" and "C++" means its specified its position.

print(items)          # output: ['Python', 'Java', 'JavaScript', 'C++']

# ======================================

"""
🟢 List Problem 30 — insert() Understanding

Start with:

numbers = [10, 20, 30, 40]

You want the final list to be:

[10, 20, 25, 30, 40]

Your task: Use insert() to add 25 in the correct position.
"""

print()

numbers = [10, 20, 30, 40]

numbers.insert(2, 25)

print(numbers)      # Output: [10, 20, 25, 30, 40]

# =======================================

"""
🟢 List Problem 31 — remove() Basics

Start with:

numbers = [10, 20, 30, 40, 50]

Remove the value 30 from the list.

Expected output:

[10, 20, 40, 50]
Your task:

Use the appropriate list method to remove 30.
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
print(numbers)    # Output: [10, 20, 40, 50]

# ===============================================

"""
🟢 List Problem 32 — remove() with Duplicate Values

Start with:

numbers = [10, 20, 30, 20, 40]

Remove the value 20 once.

Expected output:

[10, 30, 20, 40]
Your task

Use remove() and think carefully about what happens when a value appears more than once.
"""

print()

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)
print(numbers)       # Output: [10, 30, 20, 40] --> It reove the 1st 20 from the list

# ===============================

"""
🟢 List Problem 33 — remove() and a Missing Value

Start with:

numbers = [10, 20, 30, 40, 50]

Try to remove the value 100.

Your task

Write the code using remove().
"""

print()

# numbers = [10, 20, 30, 40, 50]
# numbers.remove(100)
# print(numbers)

"""
Error will come: 
ValueError: list.remove(x): x not in list
"""

# ===================================================