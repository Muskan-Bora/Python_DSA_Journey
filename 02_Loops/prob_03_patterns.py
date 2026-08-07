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

# Revision of the previous concepts:

"""
Pattern 1 — Half Pyramid (Warm-up)
"""

print()
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
"""

# =============================================

"""
Pattern 2 — Right-Aligned Half Pyramid
"""

print()
for i in range(1, 6):
    for k in range(5 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

"""
    *
   **
  ***
 ****
*****
"""

# ============================================

"""
Pattern 3 — Hollow Half Pyramid (Today's Main Revision)
"""
print()

for i in range(1, 6):
    if i == 1 or i == 2 or i == 5:
        for j in range(i):
            print("*", end="")
    else:
        print("*", end="")
        for k in range(i - 2): # 3 - 2 = 1 space and 4 - 2 = 2 space
            print(" ", end="")
        print("*", end="")
    print()

"""
Output:
*
**
* *
*  *
*****
"""
    
# ========================================================

"""
Pattern 4 — Right-Aligned Number Pyramid
"""

print()
for i in range(1, 6):
    for k in range(5 - i):
        print(" ", end="")
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

# ===================================================

"""
Pattern 5 — Left-Aligned Number Triangle
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

# ==================================

"""
(Logic Builder)
Pattern 6 — Hollow Right-Angled Triangle with 6 rows now
"""
print()

for i in range(1, 7):
    if i == 1 or i == 2 or i == 6:
        for j in range(i):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for k in range(i - 2):
            print(" ", end="")
        print("*", end="")
        print()

"""
Output:
*
**
* *
*  *
*   *
******
"""

# ============================================

"""
Revision Pattern 
Pattern R1 — Right-Aligned Number Pyramid

Write a Python program using nested for loops to print:

    1
   22
  333
 4444
55555
"""
print()
for i in range(1, 6):
    for k in range(5 - i):
        print(" ", end="")
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

# ==================================================

"""
New Pattern 1 
Pattern 1 — Floyd's Triangle
Problem Statement

Write a Python program using nested for loops to print:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
num = 1

print()
for i in range(num, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# ===============================================

"""
New Pattern 2 - Reverse Number Triangle

Write a Python program to print:

12345
1234
123
12
1
"""

print()
for i in range(5, 0, -1):
    for j in  range(i):
        print(j + 1, end="")
    print()

"""
Output:
12345
1234
123
12
1
"""

# ===================================

"""
New Pattern 3 — Palindrome Number Triangle
Problem Statement

Write a Python program using nested for loops to print:

1
121
12321
1234321
123454321
"""

print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    for l in range(i-1, 0, -1):
        print(l, end="")
    print()

"""
Output:
1
121
12321
1234321
123454321
"""

# ========================================

"""
Pattern R1 — Hollow Rectangle

Write a Python program to print:

*****
*   *
*   *
*****
"""

print()

for i in range(1, 5):
    if i == 1 or i == 4:
        for j in range(i, i + 5):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for k in range(3):
            print(" ", end="")
        print("*", end="")
        print()

"""
Output:
*****
*   *
*   *
*****
"""     

# ===========================================

"""

New Pattern 
Pattern N1 — Pascal-Style Number Triangle (Simple Version)

Write a Python program to print:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

print()

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

"""
Output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""

# =================================================

"""
Revision Pattern
Pattern R2 — Hollow Inverted Half Pyramid
Problem Statement

Write a Python program using nested for loops to print:

*****
*  *
* *
**
*

"""

print()
for i in range(1, 6):
    if i == 1 or i == 4 or i == 5:
        for j in range(6, i, -1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for k in range(4, i, -1):
            print(" ", end="")
        print("*", end="")
        print()

"""
Output:
*****
*  *
* *
**
*
"""

# ===================================

"""
New Pattern 
Pattern N2 — Continuous Number Square
Problem Statement

Print the following pattern:

1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
"""

print()
num = 1
for i in range(1, 5):
    for j in range(4):
        print(num, end=" ")
        num += 1
    print()

"""
Output:
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
"""

# ==========================================

"""
Revision Pattern
Pattern R3 — Hollow Rectangle (Revision)

******
*    *
*    *
******
"""
print()
for i in range(1, 5):
    if i == 1 or i == 4:
        for j in range(i, i + 6):
            print("*", end="")
    else:
        print("*", end="")
        for k in range(4):
            print(" ", end="")
        print("*", end="")
    print()

"""
Output:
******
*    *
*    *
******
"""

# ========================================

"""
New Pattern 
Pattern N3 — Reverse Floyd's Triangle
Problem Statement

Print:

15
14 13
12 11 10
9 8 7 6
5 4 3 2 1
"""

print()

num = 15

for i in range(5, 0, -1):
    for j in range(i, 6):
        print(num, end=" ")
        num -= 1
    print()

"""
15 
14 13 
12 11 10 
9 8 7 6 
5 4 3 2 1
"""

# ==========================================

"""
Revision Pattern — 10 Minutes
Pattern R4 — Right-Aligned Number Triangle
    1
   22
  333
 4444
55555
"""

print()
for i in range(1, 6):
    for k in range(5 - i):
        print(" ", end="")
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

# ===========================================