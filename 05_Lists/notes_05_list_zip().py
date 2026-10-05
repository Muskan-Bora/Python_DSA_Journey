"""

# 🐍 PYTHON JOURNEY — zip()

Topic:
zip()

Purpose:
zip() is used to combine corresponding elements from
two or more iterables.

In simple words:

```
zip() = pair corresponding values together
```

============================================================

1. BASIC SYNTAX
   ============================================================

Syntax:

```
zip(iterable1, iterable2)
```

Example:

```
names = ["Muskan", "Aarav", "Riya"]
marks = [85, 72, 90]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```
Muskan 85
Aarav 72
Riya 90
```

zip() pairs:

```
names[0] → marks[0]
names[1] → marks[1]
names[2] → marks[2]
```

Conceptually:

```
("Muskan", 85)
("Aarav", 72)
("Riya", 90)
```

============================================================
2. WHY USE zip()?
=================

Suppose we have two related lists:

```
students = ["Muskan", "Aarav", "Riya"]
marks = [85, 72, 90]
```

We want to work with each student's corresponding marks.

Without zip():

```
for i in range(len(students)):
    print(students[i], marks[i])
```

With zip():

```
for student, mark in zip(students, marks):
    print(student, mark)
```

zip() makes the relationship between the values
much easier to understand.

============================================================
3. zip() WITH f-STRINGS
=======================

Example:

```
students = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]

for student, mark in zip(students, marks):
    print(f"{student}: {mark}")
```

Output:

```
Muskan: 85
Aarav: 42
Riya: 76
```

============================================================
4. zip() WITH CONDITIONS
========================

We can use conditions while processing zipped values.

Example:

```
students = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]

for student, mark in zip(students, marks):
    if mark >= 50:
        print(f"{student}: Pass")
```

Output:

```
Muskan: Pass
Riya: Pass
```

Here:

```
student → corresponding name
mark    → corresponding marks
```

============================================================
5. zip() WITH THREE LISTS
=========================

zip() can combine more than two iterables.

Example:

```
students = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]
cities = ["Mumbai", "Pune", "Delhi"]

for student, mark, city in zip(students, marks, cities):
    print(f"{student}: {mark}, {city}")
```

Output:

```
Muskan: 85, Mumbai
Aarav: 42, Pune
Riya: 76, Delhi
```

The corresponding positions are combined:

```
Muskan → 85 → Mumbai
Aarav  → 42 → Pune
Riya   → 76 → Delhi
```

============================================================
6. IMPORTANT: zip() WORKS POSITION BY POSITION
==============================================

Example:

```
names = ["Muskan", "Doraemon", "Python"]
ages = [24, 100, 3]

for name, age in zip(names, ages):
    print(name, age)
```

Pairs:

```
Muskan   → 24
Doraemon → 100
Python   → 3
```

The first item is paired with the first item,
the second with the second, and so on.

============================================================
7. WHAT IF THE LISTS HAVE DIFFERENT LENGTHS?
============================================

Example:

```
names = ["Muskan", "Aarav", "Riya"]
marks = [85, 72]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```
Muskan 85
Aarav 72
```

The extra "Riya" is not included.

By default, zip() stops when the shortest iterable
is exhausted.

IMPORTANT:

```
zip() → stops at the shortest iterable
```

============================================================
8. CONVERTING zip() TO A LIST
=============================

zip() returns a zip object.

Example:

```
names = ["Muskan", "Aarav", "Riya"]
marks = [85, 72, 90]

result = zip(names, marks)

print(result)
```

This displays a zip object representation.

To see the paired values directly:

```
result = list(zip(names, marks))

print(result)
```

Output:

```
[('Muskan', 85), ('Aarav', 72), ('Riya', 90)]
```

So:

```
zip(names, marks)
```

creates the pairing.

```
list(zip(names, marks))
```

converts those pairs into a list.

============================================================
9. zip() WITH LIST COMPREHENSION
================================

zip() can also be used inside a list comprehension.

Example:

```
names = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]

result = [
    f"{name}: Pass" if mark >= 50 else f"{name}: Fail"
    for name, mark in zip(names, marks)
]

print(result)
```

Output:

```
['Muskan: Pass', 'Aarav: Fail', 'Riya: Pass']
```

This is a very useful combination:

```
zip()
    +
list comprehension
```

============================================================
10. zip() VS enumerate()
========================

enumerate():

```
Gives us:

    index + value
```

Example:

```
names = ["Muskan", "Aarav"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```
0 Muskan
1 Aarav
```

zip():

```
Gives us:

    corresponding values from multiple iterables
```

Example:

```
names = ["Muskan", "Aarav"]
marks = [85, 72]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```
Muskan 85
Aarav 72
```

Remember:

```
enumerate() → INDEX + VALUE

zip()       → VALUE + VALUE
               from different iterables
```

============================================================
11. COMMON REAL-WORLD USE
=========================

Example:

```
products = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 1000, 2000]

for product, price in zip(products, prices):
    print(f"{product}: ₹{price}")
```

Output:

```
Laptop: ₹50000
Mouse: ₹1000
Keyboard: ₹2000
```

This is useful when two lists contain related information.

============================================================
12. IMPORTANT RULE TO REMEMBER
==============================

The lists should normally represent corresponding data.

For example:

```
students = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]
```

This makes sense because:

```
student ↔ mark
```

But unrelated lists may produce meaningless pairings.

============================================================
🧠 QUICK SUMMARY
================

zip() combines corresponding values from multiple
iterables.

Basic pattern:

```
for value1, value2 in zip(list1, list2):
    ...
```

Three iterables:

```
for value1, value2, value3 in zip(list1, list2, list3):
    ...
```

Different lengths:

```
zip() stops at the shortest iterable.
```

Remember:

```
enumerate() → index + value

zip()       → value + value
```

Simple memory trick:

```
enumerate() = "Where is it?"

zip()       = "What belongs together?"

"""

# ====================================

"""
🐍 Problem 106 — Your First zip()

Given:

names = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]
🎯 Task

Use zip() to combine the corresponding student names and marks, and print each pair.

Expected output
Muskan: 85
Aarav: 42
Riya: 76
Requirements

✅ Use zip()
✅ Use a for loop
✅ Use an f-string

❌ No range()
❌ No len()
❌ No manual indexing
❌ No list comprehension
"""

names = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]

for name, mark in zip(names, marks):
    print(f"{name}: {mark}")

"""
Output:
Muskan: 85
Aarav: 42
Riya: 76
"""

# ===================================

"""
🐍 Problem 107 — zip() with a Condition
names = ["Muskan", "Aarav", "Riya", "Doraemon"]
marks = [85, 42, 76, 95]

Task:
Use zip() to combine the names and marks, and print only the students who scored 50 or more.

Expected output:

Muskan: 85
Riya: 76
Doraemon: 95
Requirements

✅ Use zip()
✅ Use a for loop
✅ Use an if condition
✅ Use an f-string
"""

print()

names = ["Muskan", "Aarav", "Riya", "Doraemon"]
marks = [85, 42, 76, 95]

for name, mark in zip(names, marks):
    if mark >= 50:
        print(f"{name}: {mark}")

"""
Output:
Muskan: 85
Riya: 76
Doraemon: 95
"""

# =============================================

"""
🐍 Problem 108 — zip() with Three Lists
names = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]
statuses = ["Pass", "Fail", "Pass"]

Task:
Use zip() to combine all three lists and print the result in this format:

Muskan: 85 - Pass
Aarav: 42 - Fail
Riya: 76 - Pass

Requirements:

✅ Use zip()
✅ Use a for loop
✅ Use an f-string
✅ Combine all three lists

❌ No range()
❌ No len()
❌ No manual indexing
❌ No list comprehension
"""

print()

names = ["Muskan", "Aarav", "Riya"]
marks = [85, 42, 76]
statuses = ["Pass", "Fail", "Pass"]

for name, mark, status in zip(names, marks, statuses):
    print(f"{name}: {mark} - {status}")

"""
Output:
Muskan: 85 - Pass
Aarav: 42 - Fail
Riya: 76 - Pass
"""

# ===========================================