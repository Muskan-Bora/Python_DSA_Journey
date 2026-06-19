# -------------------------------------------------------- #

# Python Loops

"""
What is a Loop?

A loop is used to execute a block of code repeatedlyuntil a condition becomes False or until all items
in a sequence are processed.

Why do we need loops?

Imagine printing:
Hello
Hello
Hello
Hello
Hello

Without loop:
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

This becomes repetitive.

With loop:
Python can repeat the task automatically.

So loops help us:
1. Reduce repetitive code
2. Save time
3. Process large data
4. Build logic for DSA

Examples of real-world loop usage:
- Reading database records
- Processing API responses
- Iterating through lists
- Training AI models
- Running repeated calculations
"""

# -------------------------------------------------------- #

"""
Types of Loops in Python

1. while loop
2. for loop
"""

# -------------------------------------------------------- #

"""
1. while loop

Syntax:

while condition:
    code block

Meaning:
As long as condition is True,
the loop keeps running.

Example:
"""

# count = 1

# while count <= 3:
#     print(count)
#     count += 1

"""
Output:
1
2
3
"""

# Execution:
# count = 1 -> print -> count becomes 2
# count = 2 -> print -> count becomes 3
# count = 3 -> print -> count becomes 4
# count = 4 -> condition False -> loop stops

# -------------------------------------------------------- #

"""
Important Concept: Infinite Loop

If condition never becomes False,
loop runs forever.

Example:
"""

# while True:
#     print("Infinite Loop")

"""
Be careful.

This is called an infinite loop.
"""

# -------------------------------------------------------- #

"""
2. for loop

Used when we know:
- how many times to repeat
OR
- which sequence to iterate over

Syntax:

for variable in sequence:
    code block
"""

# for i in range(3):
#     print(i)

"""
Output:
0
1
2
"""

# -------------------------------------------------------- #

"""
What is range()?

range() generates numbers.

Examples:

range(5)      -> 0,1,2,3,4
range(1,5)    -> 1,2,3,4
range(1,10,2) -> 1,3,5,7,9
"""

# -------------------------------------------------------- #

"""
Loop Control Statements (will practice later)

break    -> Exit loop immediately
continue -> Skip current iteration
pass     -> Do nothing
"""

# -------------------------------------------------------- #

"""
Important for DSA:

Loops are the backbone of:
- Arrays
- Strings
- Lists
- Searching
- Sorting
- Binary Search
- Graph Traversal

Without loops:
DSA is impossible.
"""

# -------------------------------------------------------- #

"""
Problem 1 — Print 1 to 5 using while

Task:
Print:
1
2
3
4
5

Using while loop only.
"""

# no_count = 1

# while no_count <= 5:
#     print(no_count)
#     no_count += 1

"""
Output:
1
2
3
4
5
"""

# -------------------------------

"""
Problem 2 — Print 5 to 1 using while

Print:
5
4
3
2
1
"""

# no_count1 = 5

# while no_count1 >= 1:
#     print(no_count1)
#     no_count1 -= 1

"""
Output:
5
4
3
2
1
"""
# ----------------------------------

"""
Problem 3 — Print Even Numbers

Using while loop, print:

2
4
6
8
10
"""

num = 1

while num < 11:
    if num % 2 == 0:
        print(num)
    num += 1

"""
Output:
2
4
6
8
10
"""

# -----------------------------------------

"""
Problem 4 — Sum from 1 to 5

Calculate:
1 + 2 + 3 + 4 + 5

Print final sum.
Expected output:
15
"""

count = 1
total = 0

while count < 6:
    total = total + count
    count += 1

print(total)   # Output 15

# ---------------------------------------

"""
Problem 5 — User Countdown

Take number from user.

Example input:

10

Output:
10
..
3
2
1
Blast Off!
"""

countdown = int(input("Enter the number: "))

while countdown >= 1:
    print(countdown)
    countdown -= 1

print("Blast Off!")

"""
Enter the number: 10
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
Blast Off!
"""

# ----------------------------------

"""
Problem 6 — Multiplication Table of 3

Using while loop, print:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
"""

number = 1
mul = 3

while number < 11:
    print(mul, "x", number, "=", mul * number)
    number += 1

"""
Output:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
"""