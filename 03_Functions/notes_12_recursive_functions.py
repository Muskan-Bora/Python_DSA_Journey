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