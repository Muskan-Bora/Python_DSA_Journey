# ----------------------------------------------------- #

# Python Journey Begins 

# -----------------------------

# PROBLEM 1: Print Statement Basics

"""
Write a Python program that prints the following message:
Hello World!..
"""

# Solution:

# Method 1: Basic Print

print("Hello World!..")               # Output --> Hello World!..

# --------------

# Method 2: Single Quotes

print('Hello World!..')               # Output --> Hello World!..

# ----------------

# Method 3: Multiple Arguments

print("Hello", "World!..")            # Output --> Hello World!..

# ----------------

# Method 4: Using sep

print("Hello", "World", sep="-")      # Output --> Hello-World

# ----------------

# Method 5: Using end

print("Hello", end=" ")
print("World!..")                     # Output --> Hello World!..

# ----------------

# Method 6: Multi-Line String

print("""                           
Hello
World!..
""")              

# Output --> 
# Hello
# World!..

# ----------------

# Method 7: Escape Characters

print("Hello\nWorld!..")

# Output --> 
# Hello
# World!..

# ----------------

# Method 8: Tab Character

print("Hello\tWorld!..")           # Output --> Hello   World!..

# ----------------

# Method 9: Printing Numbers

print(10)                         # Output --> 10
print(20)                         # Output --> 20

# -----------------

# Method 10: Printing Different Data Types

print("Age:", 24)
print("Marks:", 85.5)
print("Passed:", True)

"""
Output -->
Age: 24
Marks: 85.5
Passed: True
"""

# -----------------

# Method 11: f-string Method [This is one of the most used print methods in modern Python]

first_name = "John"
print(f"Hello {first_name}")            # Output --> Hello John

# ---------------------------------------------------------------------- #