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
