# -------------------------------------------

# Python Data Types

# IMP Note:
"""
A variable is a container.

A data type tells Python:

"What kind of data is stored inside the container?"
"""

"""
Problem 3: Data Types

Task 1: Create Variables

Create the following variables:
"""

first_name = "Rohan"
age = 28
height = 6.2
is_developer = False

# ----------------------------------

"""
Task 2: Print Values
"""

print(first_name)                          # Output --> Rohan
print(age)                                 # Output --> 28
print(height)                              # Output --> 6.2
print(is_developer)                        # Output --> False

# -----------------------------------

"""
Task 3: Print Data Types -- type()
"""

print(type(first_name))                   # Output --> <class 'str'>
print(type(age))                          # Output --> <class 'int'>
print(type(height))                       # Output --> <class 'float'>
print(type(is_developer))                 # Output --> <class 'bool'>

# ------------------------------------

"""
Task 4: Use f-Strings
"""

print(f"Name:{first_name}")               # Output --> Name:Rohan
print(f"Age:{age}")                       # Output --> Age:28
print(f"Height:{height}")                 # Output --> Height:6.2
print(f"Developer:{is_developer}")        # Output --> Developer:False

# --------------------------------------

"""
Task 5: Type Checking
"""

salary = 25000

print(f"The data type of salary is {type(salary)}")

# Output: --> The data type of salary is <class 'int'>

# -----------------------------------------

# BONUS CHALLENGE:

city = "Mumbai"
rating = 9.4
working = True
hours = 9

# Print Value

print(f"City: {city}")                     # Output --> City: Mumbai
print(f"Rating: {rating}")                 # Output --> Rating: 9.4
print(f"Working: {working}")               # Output --> Working: True
print(f"Hours: {hours}")                   # Output --> Hours: 9

# --------------------------------

# Print Type
print(type(city))                          # Output --> <class 'str'>
print(type(rating))                        # Output --> <class 'float'>
print(type(working))                       # Output --> <class 'bool'>
print(type(hours))                         # Output --> <class 'int'>

# -------------------------------------------------------------- #