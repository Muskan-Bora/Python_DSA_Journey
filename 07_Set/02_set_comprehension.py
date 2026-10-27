# =============================================

# Python Set Comprehensions

"""
What is a set comprehension?
A set comprehension is a short, convenient way to create a set from an iterable, such as a list or a range,
optionally applying a condition or transformation.

Instead of writing a loop and adding each item to a set, you can often create the entire set in one line.

Example 1 — Create a set of squares
Suppose we want to create a set containing the squares of numbers from 1 to 5.

squares = set()

for number in range(1, 6):
    squares.add(number ** 2)

print(squares)

Output:

{1, 4, 9, 16, 25}

# -----------------

# Using a set comprehension

squares = {number ** 2 for number in range(1, 6)}
print(squares)

Output:

{1, 4, 9, 16, 25}

Understand the syntax
Here is the general syntax:

{expression for item in iterable}

# ---------------

Expression
number ** 2
The value to calculate or place in the set.


Item
number
The variable representing each item during iteration.


Iterable
range(1, 6)
The sequence of values to process: 1, 2, 3, 4, 5.

Remember the curly braces {}. They indicate that we're creating a set comprehension, provided the expression 
isn't a dictionary key-value expression.

# ---------------

"""

# ==========================================

"""
Python Set Comprehensions — Notes
1. A set comprehension creates a set in a concise way.
2. Basic syntax: {expression for item in iterable}.
3. Use an optional if condition to filter elements: {expression for item in iterable if condition}.
4. The expression determines what value is added to the set.
5. Duplicate values are automatically removed.
6. Set elements must be hashable; for example, numbers and strings can be set elements, but lists cannot.
7. Set comprehensions are useful for transforming values, filtering data, and finding unique values.
8. Set display order is not guaranteed.
9. A set comprehension creates a new set; it does not modify the source iterable.
"""

# ===========================================

"""
Problem 26 — Squares using Set Comprehension

Write a program that:
1. Creates a set of squares of numbers from 1 to 10
   using a set comprehension.
2. Prints the resulting set.
3. Prints the total number of elements using len().
4. Uses f-strings for every output statement.
"""

squares = {number ** 2 for number in range(1, 11)}

print(f"A set of squares from 1 to 10 is {squares}")

print(f"The total number of elements: {len(squares)}")

"""
Output:
A set of squares from 1 to 10 is {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
The total number of elements: 10

"""

# ========================================

"""
Problem 27 — Even Numbers using Set Comprehension

Write a program that:
1. Creates a set of even numbers from 1 to 20
   using a set comprehension.
2. Prints the resulting set.
3. Prints the total number of elements using len().
4. Uses f-strings for every output statement.
"""

print()

even_numbers = {number for number in range(1, 21)
                if number % 2 == 0}

print(f"A set of even numbers: {even_numbers}")
print(f"The total number of elements: {len(even_numbers)}")

"""
Output:
A set of even numbers: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
The total number of elements: 10
"""

# =========================================

"""
Problem 28 — Odd Numbers using Set Comprehension

Write a program that:
1. Creates a set of odd numbers from 1 to 25
   using a set comprehension.
2. Prints the resulting set.
3. Prints the total number of elements using len().
4. Uses f-strings for every output statement.
"""

print()

odd_numbers = {number for number in range(1, 26)
                if number % 2 != 0}

print(f"A set of odd numbers from 1 to 25: {odd_numbers}")
print(f"The total number of elements: {len(odd_numbers)}")

"""
Output:
A set of odd numbers from 1 to 25: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25}
The total number of elements: 13
"""

# ======================================

"""
One important thing to remember:
{expression for item in iterable if condition}

Think of it in three steps:
1. Iterable: Where do the values come from?
2. Condition: Which values should be kept?
3. Expression: What value should be added to the set?
"""

# =====================================