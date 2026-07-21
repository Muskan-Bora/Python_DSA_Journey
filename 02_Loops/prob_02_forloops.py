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

"""
Problem 8 — Multiplication Table of User Input

Take a number from the user.
Example:
Input:
7

Output:

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
Rules
Use for loop only
Number should come from user input
"""

print("Problem 8:")

num = int(input("Enter a Number: "))
print(f"Multiplication Table of {num}:") 

for i in range (1, 11):
    print(f"{num} x {i} = {num * i}")

"""
Output:
Problem 8:
Enter a Number: 7
Multiplication Table of 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"""

# --------------------------------------------------

"""
Problem 9 — Sum of Even Numbers from 1 to 20

Calculate:
2 + 4 + 6 + ... + 20
Print only the final sum.

Rules
Use for loop
Use an if condition
Print only the final answer
"""

print("Problem 9:")

total = 0

for i in range(1, 21):
    if i % 2 == 0:
        total = total + i

print(f"The final sum of all even numbers from 1 to 20 is {total}")

"""
Output:
Problem 9:
The final sum of all even numbers from 1 to 20 is 110
"""

# ---------------------------------------------------

"""
Problem 10 — Count Characters in a Word

Take a word from the user.
Example:
Input:
Developer

Output:
Total characters = 9
Rules
Use a for loop
Do not use len()
Count characters manually
"""

print("Problem 10: ")
word = input("Enter a word: ")
count = 0

for letter in word:
    count += 1
    
print(f"Total Characters = {count}")

"""
Problem 10: 
Enter a word: Developer
Total Characters = 9
"""

# ---------------------------------------------

"""
Problem 11 — Print Odd Numbers from 1 to 15

Print:

1
3
5
7
9
11
13
15

Rules
Use for
Use an if condition
"""

print("Probelm 11:")

for i in range(1, 16):
    if i % 2 != 0:
        print(i)

"""
Output:
Probelm 11:
1
3
5
7
9
11
13
15
"""

# ---------------------------------------------------

"""
Problem 12 — Sum of Numbers Divisible by 3
Calculate the sum of all numbers from 1 to 30 that are divisible by 3.

Example numbers:
3
6
9
12
...
30

Print only the final sum.
"""

print("problem 12:")

total = 0

for i in range (1, 11):
    num = i * 3
    total = total + num

print(f"The final sum is {total}")

"""
Output:
problem 12:
The final sum is 165
"""

# --------------------------------------------------

"""
Problem 13 — Count Vowels in a Word (Using for)

Take a word from the user.
Example:
Input:
Developer

Output:
Total vowels = 4
(e, e, o, e)

Rules
Use for
Use if
Don't use count()
"""

print("Problem 13:")

count = 0

new_word = input("Enter the word: ").lower()

for letter in new_word:
    if letter in "aeiou":
        count += 1

print(f"Total vowles = {count}")

"""
Output:
Enter the word: Developer
Total vowles = 4
"""
# ---------------------------------------------

"""
Problem 14 — Count Consonants in a Word

Take a word from the user.
Example:

Input:
Developer

Output:
Total consonants = 5

Explanation:
D, v, l, p, r

Rules
Use for
Use if
Don't use .count()
Don't use len()
"""

print("Problem 14:")

count = 0

new_words = input("Enter the word: ").lower()

for new_letter in new_words:
    if new_letter.isalpha() and new_letter not in "aeiou":
        count += 1

print(f"Total consonants = {count}")

"""
Output:
Enter the word: Developer
Total consonants = 5
"""

# -----------------------------------

"""
Problem 15 — Print Numbers Divisible by Both 3 and 5

Print all numbers from 1 to 50 that are divisible by both 3 and 5.

Expected Output:
15
30
45

Rules
Use for
Use if
Don't hardcode the answers

Hint: A number must satisfy both conditions at the same time.
"""

print("Problem 15:")

print("The numbers which are divisble by both 3 and 5 are:")

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

"""
Output:
The numbers which are divisble by both 3 and 5 are:
15
30
45
"""

# ----------------------------------------