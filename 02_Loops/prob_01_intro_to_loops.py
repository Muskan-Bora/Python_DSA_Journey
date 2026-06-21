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

no_count = 1

while no_count <= 5:
    print(no_count)
    no_count += 1

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

no_count1 = 5

while no_count1 >= 1:
    print(no_count1)
    no_count1 -= 1

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

# ---------------------------------------------

"""
Problem 7 — Count Digits in a Number

Take a number from user.

Example input:

45892
Count how many digits are present.
"""

num = 45892
count = 0

while num > 0:
    num = num // 10
    print(num)
    count += 1

print("Total Count =", count)

"""
4589
458
45
4
0
Total Count = 5
"""

# ----------------------------------------

"""
Problem 8 — Reverse Countdown (Even Numbers Only)

Using while, print only even numbers from 20 to 2.
Expected output:

20
18
16
14
12
10
8
6
4
2

Rules
Use while
Print only even numbers
Reverse order (decreasing)
"""

count_down = 20

while count_down >= 1:
    if count_down % 2 == 0:
        print(count_down)
    count_down -= 1

"""
Output:
20
18
16
14
12
10
8
6
4
2
"""

# ------------------------------------  

"""
Problem 9 — Sum of Digits

Take a number from user.
Example:
45892

Calculate sum of digits:
4 + 5 + 8 + 9 + 2 = 28

Output:
Sum of digits = 28
"""

num = int(input("Enter the numbers: "))
total = 0

while num > 0:
    digit = num % 10
    total = digit + total
    num = num // 10
    
print(total)

"""
Enter the numbers: 45892
28
"""

# -------------------------------------------------  

"""
Problem 10 — Multiplication Table from User Input

Take a number from user.
Example:
Input:
7

Output:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

Rules
Use while
Number should come from user input
"""

user_num = int(input("Enter a Number: "))
num = 1

print(f"The table of {user_num}")

while num < 11:
    print(f"{user_num} x {num} = {user_num * num}")
    num += 1

"""
Enter a Number: 7
The table of 7
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

# ---------------------------------------------------

"""
Problem 11 — Reverse a Number

Take a number from user.

Example:
Input:
45892

Output:
29854
"""

num = int(input("Enter a Number: "))
reverse = 0
print("Reverse Number:")

while num > 1:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

"""
Enter a Number: 45892
Reverse Number:
29854
"""

# ------------------------------------------

"""
Problem 12 — Password Retry System (Very Practical)

Create:
stored_password = "python123"

Ask user to enter password.

Rules:
If password correct → print Access Granted
Else → ask again
User gets 3 attempts only
After 3 wrong attempts → print Account Locked

Example:

Enter password: hello
Wrong password

Enter password: admin
Wrong password

Enter password: python123
Access Granted

OR

Enter password: aaa
Wrong password

Enter password: bbb
Wrong password

Enter password: ccc
Wrong password
Account Locked
"""

stored_password = "python123"

attempt = 1

while attempt <= 3:
    user_password = input("Enter a password: ") 
    print("Attempt:", attempt) 
    if user_password.lower() == stored_password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        
    attempt += 1
    if attempt > 3:
        print("Sorry Your Account has locked you have done with 3 attempt please try later..")


"""
Output:
Enter a password: Python1234
Attempt: 1
Wrong Password
Attempt: 2
Enter a password: python  
Wrong Password
Attempt: 3
Enter a password: python123
Access Granted

# ---------

Enter a password: 123
Attempt: 1
Wrong Password
Attempt: 2
Enter a password: Py1234
Wrong Password
Attempt: 3
Enter a password: Python145
Sorry Your Account has locked you have done with 3 attempt please try later..

# ---------

Enter a password: Python123
Attempt: 1
Access Granted

# ---------

Enter a password: Python
Attempt: 1
Wrong Password
Attempt: 2
Enter a password: Python123
Access Granted
"""

# ------------------------------------------------------