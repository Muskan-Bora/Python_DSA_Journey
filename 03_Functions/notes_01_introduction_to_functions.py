# ================================================

# Python Functions 

# Topic: Introduction to Functions

# ================================================

"""

# WHAT IS A FUNCTION?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code again and again,
we write it once inside a function and call it whenever needed.

Think of a function as your own custom command.

Example:

Instead of writing:

print("Welcome")
print("Welcome")
print("Welcome")

we can create:

def welcome():
print("Welcome")

Now we only need:

welcome()
welcome()
welcome()

The same code is reused multiple times.

==================================================
REAL LIFE EXAMPLE
=================

Imagine a TV Remote.

You press:

Power Button

The TV turns ON.

You don't know what happens internally.

The remote already knows what work to perform.

A function works exactly the same way.

You call it.

Python performs the task.

==================================================
WHY DO WE USE FUNCTIONS?
========================

Without Functions:

print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")

The same code is repeated many times.

---

With Functions:

def welcome():
print("Welcome")

welcome()
welcome()
welcome()
welcome()
welcome()

The code becomes shorter, cleaner, and easier to maintain.

==================================================
ADVANTAGES OF FUNCTIONS
=======================

1. Code Reusability
   Write once.
   Use many times.

2. Cleaner Code
   Large programs become easy to read.

3. Easy Maintenance
   If something changes,
   change it only once inside the function.

4. Better Organization
   Programs become divided into small logical parts.

5. Easy Debugging
   Finding mistakes becomes easier.

==================================================
FUNCTION SYNTAX
===============

def function_name():
# code
# code
# code

function_name()

Explanation:

def
Keyword used to create a function.

function_name
Name given by the programmer.

():
Parentheses.

:
Starts the function body.

Indented Code
Work that belongs to the function.

function_name()
Calling (executing) the function.

==================================================
FLOW OF EXECUTION
=================

Step 1
Python reads the function definition.

↓

Step 2
Python DOES NOT execute it immediately.

↓

Step 3
When the function is called,

Python jumps into the function,

executes the code,

then comes back.

==================================================
EXAMPLE 1
=========

def greet():
print("Hello")

greet()

Output:

Hello

==================================================
EXAMPLE 2
=========

def welcome():
print("Welcome to Python")

welcome()
welcome()
welcome()

Output:

Welcome to Python
Welcome to Python
Welcome to Python

==================================================
IMPORTANT POINT
===============

Creating a function does NOT execute it.

Example:

def greet():
print("Hello")

Nothing happens.

Only after calling:

greet()

Python prints:

Hello

==================================================
BUILT-IN FUNCTIONS
==================

Python already provides many functions.

Examples:

print()
input()
len()
type()
int()
str()
range()

These are called Built-in Functions.

Today we are learning to create our own functions,
called User-Defined Functions.

==================================================
SUMMARY
=======

Function
A reusable block of code.

Purpose
Avoid repeating code.

Created Using
def keyword

Executed Using
Function Call

Benefit
Cleaner, reusable, and organized code.

==================================================
IMP DEFINITION
====================

"A function is a reusable block of code designed to perform a specific task.
It helps reduce code duplication, improves readability, and makes programs
easier to maintain."

"""

# ================================================

"""
Problem 1 — Create Your First Function
Question
Write a function named:
greet()

The function should print:
Hello, Future Founder!

After creating it, call the function 3 times.
"""

def greet():
    print("Hello, Future Founder!")

greet()
greet()
greet()

"""
Output:
Hello, Future Founder!
Hello, Future Founder!
Hello, Future Founder!
"""

# ===============================================