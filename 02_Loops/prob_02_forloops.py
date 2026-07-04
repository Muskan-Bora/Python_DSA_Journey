# =========================================
# FOR LOOP IN PYTHON
# =========================================

"""
1) What is a For Loop?

A for loop is used to repeat a block of code for each item in a sequence.

Sequence can be:

String
List
Tuple
Range
Set
Dictionary (later)

Example:

for x in sequence:
    # code

Meaning:

“Take each value from sequence one by one and run the code.”
"""

"""

2) Why Use For Loop?

Use for when you already know:

how many times to loop
OR
you want to traverse items one by one

Examples:

Print 1 to 10
Print characters of a word
Traverse list items

3) Basic Syntax
for variable in sequence:
    print(variable)

Example:

for num in [1, 2, 3]:
    print(num)

Output:

1
2
3

"""

"""
Using range()

Most common with for.

range(stop)
"""

for i in range(5):
    print(i)

"""
Output:
0
1
2
3
4

Important:
range(5)

means:
Start = 0 (default)
Stop = 5 (excluded)
Step = 1 (default)
"""

# ----------------------

"""
range(start, stop)
"""

for i in range(1, 6):
    print(i)

"""
Output:
1
2
3
4
5
"""

# --------------------------------

"""
range(start, stop, step)
"""

for i in range(2, 11, 2):
    print(i)

"""
Output:
2
4
6
8
10

Step = increment/decrement amount
"""

# -------------------------------

"""
Reverse Loop
"""

for i in range(5, 0, -1):
    print(i)

"""
Output:
5
4
3
2
1

Here:
-1
means decrease by 1
"""

# ----------------------------------

"""
For Loop with String
"""

word = "Python"

for letter in word:
    print(letter)

"""
Output:
P
y
t
h
o
n
"""

# ---------------------------------

"""
Difference: While vs For

While Loop:
Runs while condition is True
Manual increment needed
More flexible

For Loop
Runs through sequence
Automatic iteration
Cleaner for iteration
"""

# Example of While Loop:

count = 1

while count <= 5:
    print(count)
    count += 1

"""
Output:
1
2
3
4
5
"""

# Example of For Loop:

for count in range(1, 6):
    print(count)

"""
Output:
1
2
3
4
5

Same output, less code
"""

# ------------------------ Problems Start ------------------------- #

"""
Problem 1 — Print 1 to 5 using for

Print:

1
2
3
4
5
Rules
Use for loop only
No while
"""

print("Problem 1:")
for i in range(1, 6):
    print(i)

"""
Output:
Problem 1:
1
2
3
4
5
"""

# --------------------------------------

"""
Problem 2 — Print Even Numbers from 2 to 10

Print:

2
4
6
8
10

Rules
Use for loop
Try using range() smartly
"""

print("Problem 2:")

for a in range(2, 11, 2):
    print(a)

# Another way in for loop we can use if else also:

for b in range(2, 11):
    if b % 2 == 0:
        print(b)

"""
Output:
Problem 2:
2
4
6
8
10
"""

# ----------------------------------------------

"""
Problem 3 — Print 10 to 1 using for

Print:

10
9
8
7
6
5
4
3
2
1
Rules
Use for loop
Use range()
No while
"""

print("Problem 3:")
for i in range (10, 0, -1):
    print(i)

"""
Output:
Problem 3:
10
9
8
7
6
5
4
3
2
1
"""

# ---------------------------------------

"""
Problem 4 — Sum from 1 to 5 using for

Calculate:
1 + 2 + 3 + 4 + 5

Print final sum.

Expected output:
15
Rules
Use for
Store sum in variable
Print only final sum
"""

print("Problem 4:")
total = 0

for i in range(1, 6):
    total = total + i

print("Final Sum for 1 + 2 + 3 + 4 + 5 =", total)

"""
Problem 4:
Final Sum for 1 + 2 + 3 + 4 + 5 = 15
"""

# -------------------------------------

"""
Problem 5 — Print Multiples of 5

Print:
5
10
15
20
25
Rules
Use for loop
Use range()
"""

num = 5

print("Problem 5")
print("Mutiples of 5")
for i in range(1, 6):
    multiple = num * i
    print(multiple)

"""
Output:
Problem 5
Mutiples of 5
5
10
15
20
25
"""

# ------------------------------------------

"""
Problem 6 — Print Squares from 1 to 5

Print:

1
4
9
16
25

Rules
Use for loop
Don't hardcode the answers
"""

print("Problem 6:")

for i in range(1, 6):
    print(i * i)

"""
Output:
Problem 6:
1
4
9
16
25
"""
# ------------------------------------------

"""
Problem 7 — Count from 1 to 5 and Print "Done"

Output:

1
2
3
4
5
Done!
Rules
Use for loop
Print "Done!" only after the loop finishes
"""

print("Problem 7")

for i in range(1, 6):
    print(i)
    
print("Done!")

"""
Output:
Problem 7
1
2
3
4
5
Done!
"""

# --------------------------------------