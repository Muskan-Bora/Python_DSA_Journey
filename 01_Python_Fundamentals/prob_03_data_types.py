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

# -------------------------------------------------------------- 

# Type Conversion Concept [Another important Data Type Concept]

# 1. Str to Int

num_str = "100"
print(type(num_str))

num_int = int(num_str)                     # Output --> <class 'str'>
print(type(num_int))                       # Output --> <class 'int'>

# -----------------

# 2. Str to Float

height_str = "6.2"

height_float = float(height_str)
print(height_float)                       # Output --> 6.2
print(type(height_float))                 # Output --> <class 'float'>

# ------------------

# 3. Integer to String

my_age = 29

age_str = str(my_age)
print(age_str)                          # Output --> 29
print(type(age_str))                    # Output --> <class 'str'>

# --------------------

# 4. Boolean to String

software_developer = True

str_software_developer = str(software_developer)
print(str_software_developer)          # Output --> True
print(type(str_software_developer))    # Output --> <class 'str'>

# ---------------------------------------------

# 2. Type Checking Using isinstance()

my_name = "Alia"
print(isinstance(my_name, str))       # Output --> True

# --------------

alia_age = 20
print(isinstance(alia_age, float))    # Output --> False

# --------------

price = 99.99
print(isinstance(price, int))         # Output --> False

# --------------

is_active = True
print(isinstance(is_active, bool))    # Output --> True

# ----------------------------------------------------------- #