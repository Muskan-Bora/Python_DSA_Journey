# ===============================================

"""
🐍 Python Tuples — Complete Notes

1. What is a Tuple?
A tuple is a built-in Python data structure used to store multiple items in a single variable.

Tuples are ordered and immutable.
Ordered means the items have a defined position.
Immutable means individual elements cannot be reassigned, added, or removed after the tuple is created.

2. Creating Tuples

numbers = (10, 20, 30, 40)
names = ("Muskan", "Doraemon", "Aarav")
student = ("Muskan", 22, 85.5, True)

3. Empty Tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))
print(len(empty_tuple))

4. Single-Element Tuple

a = (10)       # Integer, not a tuple
b = (10,)      # Tuple containing one element
c = 10,        # Also a tuple

A comma is required to create a single-element tuple.

5. Checking the Type

numbers = (10, 20, 30)
print(type(numbers))  # <class 'tuple'>

6. Tuple Indexing

languages = ("Python", "Django", "JavaScript", "React")

print(languages[0])   # Python
print(languages[2])   # JavaScript
print(languages[-1])  # React
print(languages[-2])  # JavaScript

Positive indexing starts at 0.
Negative indexing starts at -1 from the end.

7. Tuple Slicing

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[3:])    # (40, 50, 60)
print(numbers[::2])   # (10, 30, 50)
print(numbers[::-1])  # (60, 50, 40, 30, 20, 10)

Syntax: tuple_name[start:stop:step]
The stop index is excluded.
Slicing returns a new tuple.

8. Membership Operators

languages = ("Python", "Django", "React")

print("Python" in languages)      # True
print("Java" not in languages)    # True

9. Tuple Length

numbers = (10, 20, 30, 40, 50)
print(len(numbers))  # 5

len() counts top-level elements.
A nested list counts as one element.

10. Tuple Traversal

languages = ("Python", "Django", "React")

for language in languages:
    print(language)

11. Traversal Using Index

for index in range(len(languages)):
    print(index, languages[index])

12. Traversal Using enumerate()

for index, language in enumerate(languages):
    print(index, language)

enumerate() provides each element's index and value.

13. Tuple count()

numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))  # 3

count(value) returns the number of occurrences.

14. Tuple index()

numbers = (10, 20, 30, 20, 40)
print(numbers.index(20))  # 1

index(value) returns the first matching index.
If the value is missing, it raises ValueError.

15. Immutability

numbers = (10, 20, 30)

# numbers[0] = 100
# TypeError: tuples do not support item assignment

Tuples do not support direct element reassignment,
append(), or remove().

16. Tuple With a Mutable Element

data = (10, [20, 30])
data[1].append(40)
print(data)  # (10, [20, 30, 40])

The tuple cannot be reassigned at the element level,
but a mutable object inside it may still be modified.

17. Common Uses

- Coordinates
- Fixed configuration values
- RGB colour values
- Returning multiple values from functions

18. List vs Tuple

List:
- Uses square brackets []
- Mutable
- Supports append(), insert(), remove(), and other
  in-place modification methods

Tuple:
- Usually uses parentheses ()
- Immutable at the element level
- Has count() and index() methods
- Useful for fixed collections of values

Important:
Tuples can be created without parentheses when commas separate the values, for example: coordinates = 10, 20
"""

# ===================================================

## Tuple Practice ##

"""
Problem 1 — Creating Tuples
Beginner

Task: Create the following three tuples:

numbers containing 10, 20, 30, 40, 50

languages containing "Python", "Django", "React"

student containing "Muskan", 22, 85.5, True

Then print each tuple and its data type using type().

Requirements
Use parentheses ().
Use meaningful variable names.
Use print() and type().

"""

numbers = (10, 20, 30, 40, 50)
print(f"{numbers}, And the data type is {type(numbers)}")

languages = ("Python", "Django", "React")
print(f"{languages}, And the data type is {type(languages)}")

student = ("Muskan", 22, 85.5, True)
print(f"{student}, And the data type is {type(student)}")

"""
Output:
(10, 20, 30, 40, 50), And the data type is <class 'tuple'>
('Python', 'Django', 'React'), And the data type is <class 'tuple'>
('Muskan', 22, 85.5, True), And the data type is <class 'tuple'>
"""

# =========================================

"""
Problem 2 — Empty Tuple
Beginner

Task: Create an empty tuple named empty_tuple.

Then print:

The tuple itself.

Its data type using type().

Its length using len().

Expected output:

()
<class 'tuple'>
0

Requirements
Use ().
Use print(), type(), and len().
Write the code yourself without copying the notes.
"""

print()

empty_tuple = ()

print(empty_tuple)                                      # Output: ()

print(f"Its data type is {type(empty_tuple)}")          # Output: Its data type is <class 'tuple'>

print(f"Its length is {len(empty_tuple)}")              # Output: Its length is 0

# =========================================

"""
Problem 3 — Tuple or Integer?
Important concept

Create two variables:

first_value = (50)

second_value = (50,)

Then print each variable and its data type using type().

Expected output:

50
<class 'int'>
(50,)
<class 'tuple'>

Requirements
Use both assignments exactly as shown.
Use print() and type().
Explain in a comment why their data types differ.
"""

print()

first_value = (50)

print(first_value)                 # Output: 50
print(type(first_value))           # Output: <class 'int'>

"""
Reason: first_value = (50) is an integer because the parentheses only group the expression. They don't create a tuple.
"""

second_value = (50,)

print(second_value)                 # Output: (50,)
print(type(second_value))           # Output: <class 'tuple'>

""" 
Reason:
second_value = (50,) is a tuple because the comma is what makes it a tuple.
"""

# ================================================

"""
Problem 4 — Mixed Tuple
Beginner

Task: Create a tuple named employee containing:
- Name: "Muskan"
- Age: 22
- Salary: 25000
- Experience: 2.5
- Currently employed: True
Then print:
1. The entire tuple.
2. Its data type using type().
3. Its length using len().
Expected output:
('Muskan', 22, 25000, 2.5, True)
<class 'tuple'>
5

Requirements
- Use parentheses ().
- Use print(), type(), and len().
- Add a comment explaining why the tuple's length is 5.
"""

print()

employee = ("Muskan", 22, 25000, 2.5, True)

print(employee)                                   # Output: ('Muskan', 22, 25000, 2.5, True)

print(f"Its Data type is {type(employee)}")       # Output: Its Data type is <class 'tuple'>

print(f"Its Length is {len(employee)}")           # Output: Its Length is 5

# Length is 5 because the tuple contains five elements.

# ========================================== 

"""
Problem 5 — Tuple Indexing
Beginner

Given this tuple:
languages = ("Python", "Django", "JavaScript", "React", "SQL")

Task: Print the following values using indexing:
1. The first element.
2. The third element.
3. The last element.
4. The second-last element.
Expected output:
Python
JavaScript
SQL
React

Requirements
- Use positive and negative indexing.
- Do not use a loop.
- Do not use slicing.
"""

print()

languages = ("Python", "Django", "JavaScript", "React", "SQL")

print(languages[0])                # Output: Python
print(languages[2])                # Output: JavaScript
print(languages[4])                # Output: SQL
print(languages[-2])               # Output: React

# ============================================