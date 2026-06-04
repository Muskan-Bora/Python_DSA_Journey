# --------------------------------------------------------

# PROBLEM 2: Variables

"""
Create variables and print their values using
different approaches.
"""

first_name = "Muskan"
age = 24
profession = "Full Stack Engineer"

# Method 1: Simple Print

print(first_name)  
print(age)
print(profession)

# Output:
"""
Muskan
24
Full Stack Engineer
"""

# --------------------------------

# Method 2: Multiple Arguments

print("Name:", first_name)
print("Age:", age)
print("Profession:", profession)

# Output:
"""
Name: Muskan
Age: 24
Profession: Full Stack Engineer
"""

# --------------------------------

# Method 3: f-Strings

print(f"My name is {first_name}")
print(f"My age is {age}")
print(f"My profession is {profession}")

# Output:
"""
My name is Muskan
My age is 24
My profession is Full Stack Engineer
"""

# ----------------------------------------------------------

# Mini Challenge
"""
Create variables:

Company: SWT Club
Experience: 1.5

Print:

I work at SWT Club and have 1.5 years of experience.

using an f-string.
"""

company = "SWT Club"
no_years_exp = 1.5


print(f"I work at {company} and have {no_years_exp} years of experience.")

# Output:
# I work at SWT Club and have 1.5 years of experience.

# -------------------------------------------------

# Some of the more imp variable concepts

# 1. Reassigning Variables

your_age = 24
print(your_age)   # Output --> 24

your_age = 25
print(your_age)   # Output --> 25

# ----------------

# 2. Copying Variables

your_name = "Muskan"
developer_name = your_name

print(developer_name)   # Output --> Muskan

# -----------------

# 3. Multiple Assignment

x, y, z = 1, 2, 3

print(x)      # Output --> 1
print(y)      # Output --> 2
print(z)      # Output --> 3

# ---------------------

# 4. Swapping Variables [One of Python's coolest features.]

a = 10
b = 20

a, b = b, a

print(a)   # Output --> 20
print(b)   # Output --> 10

# ---------------------------------------------------------- #