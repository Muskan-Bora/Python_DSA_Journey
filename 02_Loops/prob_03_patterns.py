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

"""
Pattern 5 — Repeated Row Numbers
"""

print()

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

"""
Output:
1
22
333
4444
55555
"""

# =========================

"""
Pattern 6 — Continuous Numbers
"""
print()

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end="")
        num += 1
    print()

"""
Output:
1
23
456
78910
1112131415
"""

# =======================================

"""
Pattern 7 — Right-Aligned Half Pyramid
"""

print()

for i in range(1, 6):  # Outer Loop
    for k in range(5-i):   # For Space.. How many space needed
        print(" ", end="")
    for j in range(i):   # For star loop
        print("*", end="")
    print()

"""
Output:
    *
   **
  ***
 ****
*****
"""

# =====================================

"""
Pattern 8 — Right-Aligned Inverted Half Pyramid
"""
print()
for i in range(1, 6):    # Outer Loop
    for k in range(1, i):   # For space Loop
        print(" ", end="")
    for j in range(6, i, -1):  # For star Loop
        print("*", end="")
    print()

"""
*****
 ****
  ***
   **
    *
"""

# ===================================

"""
Pattern 9 — Full Pyramid of Stars
"""
# Method 1
print()
for i in range(1, 10, 2):
    for k in range(9 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# Method 2 common

print()

for i in range(1, 6):
    for k in range(5-i):
        print(" ", end="")
    for j in range(i * 2 - 1) :
        print("*", end="")
    print()

"""
Method 1: 

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

Method 2:
    *
   ***
  *****
 *******
*********
"""

# =================================

"""
Pattern 10 — Inverted Full Pyramid
"""
print()
for i in range(1, 6):
    for k in range(1, i):
        print(" ", end="")
    for j in range(10, i * 2 - 1, -1):
        print("*", end="")
    print("")

"""
Output:

*********
 *******
  *****
   ***
    *
"""
# ==========================================

"""
Pattern 11 — Diamond (Upper + Lower Pyramid)

This pattern combines two patterns you've already mastered.

Write a Python program using nested for loops to print:
"""
print()
for i in range(1, 6):
    for k in range(5 - i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

for i in range(2, 6):
    for l in range(1, i):
        print(" ", end="")
    for m in range(10, i*2-1, -1):
        print("*", end="")
    print()

"""
Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

# =================================================

"""
Pattern 12 — Half Diamond Star Pattern
Problem Statement

Write a Python program using nested for loops to print the following pattern:

*
**
***
****
*****
****
***
**
*
"""

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
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
****
***
**
*
"""

# =====================================================

"""
Pattern 13 [Challenge]
Without changing the logic much, how would you print this in Numbers instead?
"""
print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

"""
Output:
1
22
333
4444
55555
4444
333
22
1
"""

# =============================================

"""
Pattern 14 — Hollow Half Pyramid
"""
print()

for i in range(1, 6):

    # Row 1, Row 2 and Last Row
    if i == 1 or i == 2 or i == 5:
        for j in range(i):
            print("*", end="")

    # Hollow Rows (Row 3 and Row 4)
    else:
        print("*", end="")          # First star

        for k in range(i - 2):      # Middle spaces
            print(" ", end="")

        print("*", end="")          # Last star

    print()

"""
Output:
*
**
* *
*  *
*****
"""

# ============================================