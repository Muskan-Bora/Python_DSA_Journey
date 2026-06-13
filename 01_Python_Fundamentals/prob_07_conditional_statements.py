# --------------------------------------------------------------- #

# Python Conditional Statements

"""
Conditional Statements are used to make decisions in Python.

They allow the program to execute different blocks of code
based on whether a condition is True or False.

In simple words:
"If a condition is true, do something.
Otherwise, do something else."

Why do we need Conditional Statements?
- To make decisions in programs
- To control program flow
- To build logic-based systems like:
    * Login Systems
    * ATM Machines
    * Eligibility Checks
    * AI Decision Models

Types of Conditional Statements in Python:

1. if
   Executes code only when condition is True

   Syntax:
   if condition:
       code

2. if-else
   Executes one block if True, another if False

   Syntax:
   if condition:
       code_if_true
   else:
       code_if_false

3. if-elif-else
   Used when multiple conditions need checking

   Syntax:
   if condition1:
       code1
   elif condition2:
       code2
   else:
       code3

4. Nested if
   An if statement inside another if statement

Important Notes:
- Python uses indentation (spaces/tab) to define blocks
- Comparison operators are commonly used:
    ==  !=  >  <  >=  <=
- Logical operators can also be used:
    and  or  not

Example:
age = 24

if age >= 18:
    print("Adult")
else:
    print("Minor")
"""

# --------------------------------------------------------------- #