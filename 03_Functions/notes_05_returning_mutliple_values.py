# =================================================================================

"""

===========================================================
Python Functions — Returning Multiple Values
===========================================================

A function can return more than one value.

Example:

def get_user():
    return "Muskan", "Developer"

name, role = get_user()

print(name)
print(role)

Output:

Muskan
Developer


The returned values can be stored in multiple variables.

The returned values are internally represented as a tuple:

("Muskan", "Developer")


Example:

def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference

total, difference = calculate(20, 5)

Output:

total = 25
difference = 15


Key Point:

return value1, value2

can be received as:

variable1, variable2 = function_call()


This is commonly called tuple unpacking.


Mental Model:

Function
    ↓
returns multiple values
    ↓
(value1, value2)
    ↓
variable1, variable2

"""

# =======================================

"""
Problem — get_student_info()

Create:

def get_student_info():

The function should return:

"Muskan"
"Python Developer"

Then:

Store the two returned values in:
name
role
Print both.
"""

def get_student_info():
    return "Muskan", "Python Developer"

name, role = get_student_info()

print(name)
print(role)

"""
Output:
Muskan
Python Developer
"""

# ===================================

"""
Problem 2 — Multiple Return Values
Problem Statement

Create a function:

def calculate(a, b):

The function should:

Calculate the sum of a and b.
Calculate the difference of a and b.
Return both values.

Then:

Call the function with a = 50 and b = 20.
Store the returned values in:
total
difference
Print both values.
"""

def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference

total, difference = calculate(50, 20)

print(total)
print(difference)

"""
Output:
70
30
"""

# =====================================================