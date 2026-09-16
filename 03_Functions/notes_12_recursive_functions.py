# =================================================

"""
RECURSION
---------

Recursion = A function calling itself.

Every recursive function generally has:

1. Base Case
   → Stops the recursion.

2. Recursive Case
   → Function calls itself with a smaller/simpler problem.

Basic structure:

def function(value):

    if base_condition:
        return

    function(smaller_value)


Example:

def countdown(number):
    print(number)

    if number > 1:
        countdown(number - 1)

countdown(5)

Output:
5
4
3
2
1


Important:
- Base case is essential.
- Recursive call should move toward the base case.
- Recursion uses the call stack.
- Missing/incorrect base case can cause RecursionError.
- Recursion and loops can sometimes solve the same problem.
- Recursion is especially useful for trees, graphs, backtracking,
  divide-and-conquer and recursive mathematical problems.
"""

# ===============================================

"""
Problem 1: Print numbers from 5 down to 1

Create a recursive function:

def countdown(number):
    # your code

When you call:

countdown(5)

Expected output:

5
4
3
2
1
Your rules 🧠

You must use recursion.

Your function should have:

A print()
A base case
A function call to itself

Don't use a for or while loop.
"""

def countdown(number):
    print(number)

    if number > 1:
        countdown(number - 1)

countdown(5)

"""
Output:
5
4
3
2
1
"""

# ========================================

"""
🔁 Recursion — Problem 2

This time, we'll introduce something important: recursion with return.

Write a recursive function:

sum_numbers(5)

It should return the sum:

5 + 4 + 3 + 2 + 1 = 15

Expected output:

15
Your task 🎯

Complete this:

def sum_numbers(number):
    # your logic here


result = sum_numbers(5)
print(result)

Don't worry about explaining it yet. Just try solving it yourself.
"""

print()

def sum_numbers(number):
    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

result = sum_numbers(5)
print(result)

"""
Output:
15
"""

# ==============================================

"""
🔁 Simple Recursion Practice

Write a function called count_up(number).

If we call:

count_up(5)

the output should be:

1
2
3
4
5
Your skeleton 🐍
def count_up(number):

    # your logic here


count_up(5)
💡 One small hint

Your recursion should keep reducing the number:

count_up(number - 1)

But think carefully about where you put the print().
"""

print()

def count_up(number):

    if number > 1:
        count_up(number - 1)
    print(number)

count_up(5)

"""
Output:
1
2
3
4
5
"""

# ============================================

"""
Problem 1 - Factorial Recurssion Problem
"""

def factorial(number):
    
    if number == 1:
        return number
        
    return number * factorial(number - 1)


result = factorial(5)
print(result)

"""
Output:
120
"""

# ============================

"""
🔁 Recursion Problem 1 — Sum from 1 to N

Create:

def sum_numbers(number):
    # your logic

result = sum_numbers(5)
print(result)

Expected output:

15

Because:

1 + 2 + 3 + 4 + 5 = 15

Rules:

No for
No while
Must use recursion
Must return the answer
"""

def sum_numbers(number):
    
    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

result = sum_numbers(5)
print(result)

"""
Output:
15
"""

# ============================================

"""
🔁 Recursion Problem 2 — Power of a Number

Create:

def power(base, exponent):
    # your logic

result = power(2, 5)
print(result)

Expected output:

32

Because:

2 x 2 x 2 x 2 x 2 = 32

Rules:

No for
No while
Must use recursion
Must have a base case
Must return the result
"""

def power(base, exponent):

    if exponent == 1:
        return base
    
    return  base * power(base, exponent - 1)

result = power(2, 5)
print(result)

"""
Output:
32
"""

# ===============================================

"""

Problem 1 — Sum from 1 to N
🔁 Recursion Revision — Sum from 1 to N

Create:

def sum_numbers(number):
    # your logic

result = sum_numbers(5)
print(result)

Expected output:

15

Because:

1 + 2 + 3 + 4 + 5 = 15

Rules:

No for
No while
Must use recursion
Must have a base case
Must return the answer
"""

print()

def sum_numbers(number):
    if number == 1:
        return number

    return number + sum_numbers(number - 1)

result = sum_numbers(5)
print(result)

"""
Output:
15
"""

# ===========================================

"""
🔁 Recursion Revision — Power of a Number

Create:

def power(base, exponent):
    # your logic

result = power(2, 5)
print(result)

Expected output:

32

Because:

2 x 2 x 2 x 2 x 2 = 32

Rules:

No for
No while
Must use recursion
Must have a base case
Must return the result
"""

print()

def power(base, exponent):

    if exponent == 1:
        return base 

    return base * power(base, exponent - 1) 

result = power(2, 5)
print(result)

"""
Output:
32
"""

# ======================================================

"""
Problem 3 — Factorial 🔢

This is the one new problem for today:

🔢 Recursion Problem — Factorial

Create:

def factorial(number):
    # your logic

result = factorial(5)
print(result)

Expected output:

120

Because:

5 x 4 x 3 x 2 x 1 = 120

Rules:

No for
No while
Must use recursion
Must have a base case
Must return the result
"""

print()

def factorial(number):
    
    if number == 1:
        return number

    return number * factorial(number - 1)

result = factorial(5)
print(result)

"""
Output:
120
"""

# =========================================

"""
Let's start with #1 🔥
def sum_numbers(number):
    # logic
Problem:

Write a recursive function sum_numbers(number) that returns the sum of all numbers from 1 to number.

For example:

sum_numbers(5) → 15
sum_numbers(3) → 6
sum_numbers(1) → 1

Rules:

❌ No for loop
❌ No while loop
✅ Must use recursion
✅ Must have a base case
✅ Must use return
"""

print()

def sum_numbers(number):

    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

result = sum_numbers(6)
print(result)

"""
Output:
21
"""

# ===============================================

"""
🔁 Recursion Problem
Problem 1 — Count Down Sum

Write a recursive function:
sum_even_numbers(number)

It should return the sum of all even numbers from number down to 2.

Example:

sum_even_numbers(6) → 12

Because:
6 + 4 + 2 = 12

Another example:

sum_even_numbers(10) → 30

Because:

10 + 8 + 6 + 4 + 2 = 30
Rules
❌ No loops
✅ Must use recursion
✅ Must have a base case
✅ Must use return

Test it with:

result = sum_even_numbers(8)
print(result)

Expected output:

20
"""
print()
def sum_even_numbers(number):
   
    if number == 0 :
        return 0

    if number % 2 == 0:
        return number + sum_even_numbers(number - 1)
        
    return sum_even_numbers(number - 1)

result = sum_even_numbers(8)
print(result) 

"""
Output: 20
"""

# ===================================================

"""
🔁 Question 1 — Recursion

Write a recursive function:

sum_odd_numbers(number)

It should return the sum of all odd numbers from number down to 1.

Examples:

sum_odd_numbers(7) → 16
sum_odd_numbers(5) → 9
sum_odd_numbers(10) → 25
Rules
❌ No loops
✅ Use recursion
✅ Use a base case
✅ Use return
Think carefully about what should happen when the number is odd vs even.
"""

print()
def sum_odd_numbers(number):
   
    if number == 0 :
        return 0

    if number % 2 != 0:
        return number + sum_odd_numbers(number - 1)
        
    return sum_odd_numbers(number - 1)

result = sum_odd_numbers(7)
print(result) 

"""
Output:
16
"""

# =========================================

"""
🔁 Question 1 — Basic Recursion

Write a recursive function:

multiply_numbers(number)

It should return the product of all numbers from number down to 1.

Examples:

multiply_numbers(5) → 120
multiply_numbers(4) → 24
multiply_numbers(3) → 6
Rules
❌ No loops
✅ Recursion
✅ Base case
✅ return
"""
print()
def multiply_numbers(number):
    if number == 1:
        return 1

    return number * multiply_numbers(number - 1)

result = multiply_numbers(4)
print(result)

"""
OUTPUT:
24
"""

# ======================

"""
🧩 Recursion Revision Problem — Sum of Numbers

Write a recursive function that takes a number n and returns the sum of all numbers from 1 to n.

Example

If:

n = 5

The result should be:

15

Because:

1 + 2 + 3 + 4 + 5 = 15
Your task

Complete this:

def sum_numbers(n):
    # write your recursive logic here


result = sum_numbers(5)
print(result)
Rules 🎯
Must use recursion
No for loop
No while loop
Think about:
What should the base case be?
What should the recursive call be?
What should you return?
"""

print()

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

result = sum_numbers(5)
print(result)

"""
Output:
15

What should the base case be?  n == 1 
What should the recursive call be? sum_numbers(n - 1) 
What should you return? n + sum_numbers(n - 1) return logic
"""

# ========================================