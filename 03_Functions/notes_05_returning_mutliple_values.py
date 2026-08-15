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

# def get_student_info():
#     return "Muskan", "Python Developer"

# name, role = get_student_info()

# print(name)
# print(role)

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

"""
🔄 Functions Master Revision — One Combined Problem
🧩 Problem — student_result()

Create a function:

def student_result(name, marks, bonus=0):

The function should:

Accept name as a parameter.
Accept marks as a parameter.
Have a default parameter bonus=0.
Calculate the final marks:
final_marks = marks + bonus
Return both:
name
final_marks
Then call the function twice
Call 1 — Without bonus
name = Muskan
marks = 85

Don't provide the bonus argument.

Store the returned values in:

student_name
final_marks

Call 2 — With bonus
name = Rahul
marks = 78
bonus = 5

Store the returned values in:

student_name
final_marks

Then print the result after each call.

Expected output
Student: Muskan
Final Marks: 85


Student: Rahul
Final Marks: 83
"""

def student_result(name, marks, bonus=0):
    return name, marks + bonus

student_name, final_marks = student_result("Muskan", 85, bonus=0)

print(f"Student: {student_name}")
print(f"Final Marks: {final_marks}")

"""
Output:
Student: Muskan
Final Marks: 85
"""

student_name, final_marks = student_result("Rahul", 78, bonus=5)

print(f"Student: {student_name}")
print(f"Final Marks: {final_marks}")

"""
Student: Rahul
Final Marks: 83
"""