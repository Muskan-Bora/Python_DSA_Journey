# =======================================

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

"""