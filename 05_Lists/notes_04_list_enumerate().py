# =============================================

"""

# 🐍 PYTHON JOURNEY — enumerate()

Topic:
enumerate()

Purpose:
enumerate() is used when we want to loop through a
sequence/list and get BOTH:

```
    1. The index
    2. The value
```

Instead of manually working with indexes, enumerate()
provides the index and value together.

============================================================

1. BASIC SYNTAX
   ============================================================

Syntax:

```
for index, value in enumerate(iterable):
    # code
```

Example:

```
names = ["Muskan", "Aarav", "Riya"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```
0 Muskan
1 Aarav
2 Riya
```

============================================================
2. WHAT enumerate() GIVES US
============================

For this list:

```
names = ["Muskan", "Aarav", "Riya"]
```

enumerate(names) conceptually gives:

```
(0, "Muskan")
(1, "Aarav")
(2, "Riya")
```

Therefore:

```
index -> 0, 1, 2
value -> "Muskan", "Aarav", "Riya"
```

We can unpack these two values directly:

```
for index, name in enumerate(names):
```

============================================================
3. WHY USE enumerate()?
=======================

Without enumerate():

```
names = ["Muskan", "Aarav", "Riya"]

for i in range(len(names)):
    print(f"Index: {i}, Name: {names[i]}")
```

With enumerate():

```
names = ["Muskan", "Aarav", "Riya"]

for i, name in enumerate(names):
    print(f"Index: {i}, Name: {name}")
```

The enumerate() version is cleaner and easier to read.

============================================================
4. BASIC EXAMPLE
================

```
students = ["Muskan", "Aarav", "Riya", "Doraemon"]

for index, student in enumerate(students):
    print(f"Index: {index}, Student: {student}")
```

Output:

```
Index: 0, Student: Muskan
Index: 1, Student: Aarav
Index: 2, Student: Riya
Index: 3, Student: Doraemon
```

============================================================
5. enumerate() STARTS FROM 0 BY DEFAULT
=======================================

By default, enumerate() starts the index from 0.

```
names = ["Muskan", "Aarav", "Riya"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```
0 Muskan
1 Aarav
2 Riya
```

============================================================
6. STARTING FROM A DIFFERENT INDEX
==================================

We can provide a start value.

Syntax:

```
enumerate(iterable, start=value)
```

Example:

```
names = ["Muskan", "Aarav", "Riya"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
```

Output:

```
1. Muskan
2. Aarav
3. Riya
```

This is useful when displaying numbered lists to users.

============================================================
7. enumerate() WITH STRINGS
===========================

enumerate() can also be used with strings because strings
are iterable.

Example:

```
word = "Python"

for index, character in enumerate(word):
    print(f"Index: {index}, Character: {character}")
```

Output:

```
Index: 0, Character: P
Index: 1, Character: y
Index: 2, Character: t
Index: 3, Character: h
Index: 4, Character: o
Index: 5, Character: n
```

============================================================
8. enumerate() WITH CONDITIONS
==============================

We can use conditions inside the loop.

Example:

```
numbers = [10, 25, 30, 15, 40]

for index, number in enumerate(numbers):
    if number > 20:
        print(f"Index: {index}, Number: {number}")
```

Output:

```
Index: 1, Number: 25
Index: 2, Number: 30
Index: 4, Number: 40
```

The index tells us WHERE the matching value is located.

============================================================
9. enumerate() WITH LISTS AND MODIFICATION
==========================================

Because lists are mutable, enumerate() can be useful when
we need both the index and value.

Example:

```
numbers = [10, 20, 30, 40]

for index, number in enumerate(numbers):
    if number == 30:
        numbers[index] = 35

print(numbers)
```

Output:

```
[10, 20, 35, 40]
```

Here:

```
index -> tells us where the value is
number -> tells us what the current value is
```

============================================================
10. enumerate() WITH f-STRINGS
==============================

enumerate() works very well with f-strings.

Example:

```
names = ["Muskan", "Doraemon", "Python"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
```

Output:

```
0: Muskan
1: Doraemon
2: Python
```

============================================================
11. enumerate() WITH start=1 AND f-STRINGS
==========================================

Example:

```
tasks = ["Python", "Django", "DSA"]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

Output:

```
1. Python
2. Django
3. DSA
```

This is commonly used for displaying numbered items.

============================================================
12. enumerate() WITH OTHER ITERABLES
====================================

enumerate() is not limited to lists.

It can work with:

```
Lists
Strings
Tuples
Sets (order should not be relied upon)
Other iterable objects
```

Example with a tuple:

```
languages = ("Python", "Java", "C++")

for index, language in enumerate(languages):
    print(index, language)
```

Output:

```
0 Python
1 Java
2 C++
```

============================================================
13. IMPORTANT: enumerate() RETURNS AN ENUMERATE OBJECT
======================================================

Example:

```
names = ["Muskan", "Aarav"]

result = enumerate(names)

print(result)
```

The output will be something similar to:

```
<enumerate object at ...>
```

It is an enumerate object, which is an iterator.

We normally use it directly inside a loop:

```
for index, name in enumerate(names):
    print(index, name)
```

We usually do not need to manually create the
enumerate object.

============================================================
14. CONVERTING enumerate() TO A LIST
====================================

We can convert it into a list if we want to see the
index-value pairs directly.

Example:

```
names = ["Muskan", "Aarav", "Riya"]

result = list(enumerate(names))

print(result)
```

Output:

```
[(0, 'Muskan'), (1, 'Aarav'), (2, 'Riya')]
```

With start=1:

```
result = list(enumerate(names, start=1))
```

Output:

```
[(1, 'Muskan'), (2, 'Aarav'), (3, 'Riya')]
```

============================================================
15. enumerate() VS range(len())
===============================

Traditional approach:

```
names = ["Muskan", "Aarav", "Riya"]

for i in range(len(names)):
    print(i, names[i])
```

Using enumerate():

```
for i, name in enumerate(names):
    print(i, name)
```

Both can produce the same result.

However, enumerate() directly gives us the index and
value together, making the code cleaner.

============================================================
16. IMPORTANT DIFFERENCE
========================

range(len(list)):

```
Gives us indexes.
```

enumerate(list):

```
Gives us index + value together.
```

Example:

```
for i in range(len(names)):
    # i is the index
    # names[i] is the value
```

With enumerate():

```
for i, name in enumerate(names):
    # i is the index
    # name is the value
```

============================================================
17. COMMON MISTAKE
==================

Wrong:

```
for index, name in enumerate(names):
    print(names[index])
```

This is not necessarily wrong, but if we already have
the value in 'name', accessing names[index] again is
unnecessary.

Better:

```
for index, name in enumerate(names):
    print(name)
```

============================================================
18. ANOTHER COMMON MISTAKE
==========================

Wrong:

```
for name, index in enumerate(names):
```

The order is:

```
index, value
```

Correct:

```
for index, name in enumerate(names):
```

============================================================
19. enumerate() WITH NESTED LISTS
=================================

Example:

```
students = [
    ["Muskan", 85],
    ["Aarav", 42],
    ["Riya", 76]
]

for index, student in enumerate(students):
    print(f"Index: {index}, Student: {student}")
```

Output:

```
Index: 0, Student: ['Muskan', 85]
Index: 1, Student: ['Aarav', 42]
Index: 2, Student: ['Riya', 76]
```

The value returned by enumerate() can itself be another
list or complex object.

============================================================
20. KEY PATTERN TO REMEMBER
===========================

The most important pattern:

```
for index, value in enumerate(items):
    # use index
    # use value
```

With a custom starting number:

```
for index, value in enumerate(items, start=1):
    # use index
    # use value
```

============================================================
🧠 QUICK SUMMARY
================

enumerate() is used when we need:

```
INDEX + VALUE
```

Default:

```
enumerate(items)
```

starts at:

```
0
```

Custom starting index:

```
enumerate(items, start=1)
```

Basic pattern:

```
for index, value in enumerate(items):
    ...
```

Think of it as:

```
enumerate() = "Give me the position AND the item."
```

============================================================
🐍 PYTHON JOURNEY REMINDER
==========================

Do not memorize enumerate() as a complicated function.

Remember the simple idea:

```
LIST → enumerate() → INDEX + VALUE
```

Example:

```
names = ["Muskan", "Doraemon", "Python"]

for index, name in enumerate(names):
    print(index, name)
```

# That is the core of enumerate().

"""

# ---------------------------------------------------