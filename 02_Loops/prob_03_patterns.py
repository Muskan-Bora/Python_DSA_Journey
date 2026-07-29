# ===================================================

# Python Patterns

"""
Pattern 1 — Half Pyramid of Stars
"""
for i in range(1, 6):
    print("*" * i)    # Shortcut pythonic way


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

"""
Output:
*
**
***
****
*****

Explanation:
i = Row Number

The number of stars printed = i

So the execution becomes:

i = 1
↓
Print "*" x 1
↓

*

-------------------

i = 2
↓
Print "*" x 2
↓

**

-------------------

i = 3
↓
Print "*" x 3
↓

***

-------------------

i = 4
↓

****

-------------------

i = 5
↓

*****

Notice here i is doing two jobs:

It tells us which row we're on.
It also tells us how many stars to print.

That's why:

print("*" * i)

works so beautifully.
"""

# ==================================================

"""
Pattern 2 — Inverted Half Pyramid of Stars
"""
print() # Adds a blank line before this pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

"""
Output:
*****
****
***
**
*
"""

# =======================================

"""
Pattern 3 — Half Pyramid of Numbers
"""

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

"""
Output:
1
12
123
1234
12345
"""

# ===========================================

"""
Pattern 4 — Inverted Half Pyramid of Numbers
"""
print()

for i in range(6, 1, -1):
    for j in range(1, i): 
        print(j, end="") 
    print()

"""
Output:
12345
1234
123
12
1
"""

# ===============================================