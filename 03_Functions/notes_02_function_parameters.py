# ================================================

# Python Functions - Day 2

# Topic: Function Parameters

# ================================================

# """

# RECAP
"""
Yesterday we learned:

def greet():
print("Hello")

greet()

Output:

Hello

The function always prints the same output because it does not accept any input.

==================================================
THE PROBLEM
===========

Suppose we want to greet different people.

Hello Muskan
Hello Doraemon
Hello Rahul

Should we create three different functions?

def greet_muskan():
...

def greet_doraemon():
...

def greet_rahul():
...

No.

That would create unnecessary duplicate code.

==================================================
THE SOLUTION → PARAMETERS
=========================

A Parameter is a variable written inside the parentheses of a function definition.

It acts as a placeholder.

When the function is called, a value is passed into that placeholder.

Syntax:

def function_name(parameter):
# code

==================================================
EXAMPLE
=======

def greet(name):
print("Hello", name)

Here,

name

is called a Parameter.

==================================================
FUNCTION CALL
=============

greet("Muskan")

Python internally thinks:

name = "Muskan"

So the function becomes:

print("Hello", "Muskan")

Output:

Hello Muskan

---

greet("Doraemon")

Python internally thinks:

name = "Doraemon"

Output:

Hello Doraemon

---

greet("Rahul")

Python internally thinks:

name = "Rahul"

Output:

Hello Rahul

==================================================
IMPORTANT OBSERVATION
=====================

The function never changes.

Only the value passed to the parameter changes.

One function.

Different inputs.

Different outputs.

==================================================
REAL-LIFE EXAMPLE
=================

Imagine a Restaurant.

Waiter = Function

Customer's Order = Parameter

Customer 1:

Pizza

Customer 2:

Burger

Customer 3:

Pasta

The waiter is the same.

Only the order changes.

Similarly,

The function is the same.

Only the parameter value changes.

==================================================
FUNCTION WITH PARAMETER
=======================

def greet(name):
print("Hello", name)

greet("Muskan")
greet("Python")
greet("Future Founder")

Output:

Hello Muskan
Hello Python
Hello Future Founder

==================================================
KEYWORDS TO REMEMBER
====================

Function Definition

def greet(name):

Function Call

greet("Muskan")

Parameter

name

Value Passed During Function Call

"Muskan"

==================================================
ADVANTAGES OF PARAMETERS
========================

1. Avoid creating multiple similar functions.

2. Make functions reusable.

3. Accept different values every time.

4. Reduce duplicate code.

5. Make programs flexible.

==================================================
IMP DEFINITION
====================

A Parameter is a variable declared inside the parentheses of a function definition.

It receives a value when the function is called, allowing the same function to work with different inputs.

==================================================
SUMMARY
=======

Function
A reusable block of code.

Parameter
A variable inside the function definition.

Function Call
Executes the function.

Value Passed
The data given while calling the function.

One Function
Multiple Inputs
Multiple Outputs
"""

# ===============================================================

"""
Problem 1

Create a function:

def country(name):

It should print:

Welcome to <name>

Call the function with:

India
Japan
Canada
"""

def country(name):                            # Here name is a parameter
    print(f"Welcome to {name}")

country("India")   # Here, name receives the value "India".
country("Japan")
country("Canada")

"""
Output:
Welcome to India
Welcome to Japan
Welcome to Canada
"""

# =========================================================================================== #

"""
# ==================================================

======== MULTIPLE PARAMETERS CONCEPT ================

# ==================================================

# RECAP

We learned functions with one parameter.

Example:

def greet(name):
print("Hello", name)

greet("Muskan")

Output:
Hello Muskan

Here,
name
is a Parameter.

==================================================
THE PROBLEM:
===========

Suppose we want to store more than one piece of information.

Example:

Student Name
Course

One parameter is not enough.
We need two parameters.

==================================================
THE SOLUTION
============

A function can have multiple parameters.
Parameters are separated using commas (,).

Syntax:

def function_name(parameter1, parameter2):
# code

==================================================
EXAMPLE
=======

def student(name, course):
print(f"Student: {name}")
print(f"Course: {course}")

Here,
name and course are Parameters.

==================================================
FUNCTION CALL
=============

student("Muskan", "Python")

Python internally thinks:

name = "Muskan"

course = "Python"

So the function becomes:

print(f"Student: {name}")
print(f"Course: {course}")

Output:

Student: Muskan
Course: Python

---

student("Rahul", "Java")

Python internally thinks:

name = "Rahul"

course = "Java"

Output:

Student: Rahul
Course: Java

==================================================
IMPORTANT RULE
==============

Python matches arguments with parameters according to their position.

Example:

student("Muskan", "Python")

Matching:

Parameter      Argument

name       ->  "Muskan"

course     ->  "Python"

==================================================
ORDER MATTERS
=============

Correct:

student("Muskan", "Python")

Output:

Student: Muskan
Course: Python

Incorrect Order:

student("Python", "Muskan")

Python thinks:

name = "Python"

course = "Muskan"

Output:

Student: Python
Course: Muskan

==================================================
ADVANTAGES
==========

1. One function can accept multiple values.

2. Reduces duplicate code.

3. Makes functions more flexible.

4. Keeps related information together.

==================================================
DEFINITION
====================

A function can have multiple parameters.
Each parameter receives one value (argument) when the function is called.

Python matches arguments to parameters from left to right according to their position.

==================================================
SUMMARY
=======

One Parameter

def greet(name)

Multiple Parameters

def student(name, course)

Parameter

Variable inside the function definition.

Arguments

Actual values passed during the function call.

Python Matching Rule

First Argument  -> First Parameter

Second Argument -> Second Parameter

Third Argument  -> Third Parameter

and so on...

NOTE:
Python matches arguments to parameters from left to right according to their position.
"""

# =======================================================

"""
Problem Statement

Create a function named:

employee(name, company)

The function should print:

Employee: <name>
Company: <company>
Call the function three times using:
Muskan      SWT Club
Rahul       Google
Doraemon    Future Tech
"""

def employee(name, company):
    print(f"Employee: {name}")
    print(f"Company: {company}")

print()
employee("Muskan", "SWT Club")
print()
employee("Rahul", "Google")
print()
employee("Doraemon", "Future Tech")

"""
Output:
Employee: Muskan
Company: SWT Club

Employee: Rahul
Company: Google

Employee: Doraemon
Company: Future Tech
"""

# =====================================