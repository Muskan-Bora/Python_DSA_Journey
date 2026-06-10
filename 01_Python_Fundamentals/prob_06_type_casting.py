# ------------------------------------------------------- #

# Python Type Casting

# ------------------------------------------------------- #

"""
Python Type Casting

Definition:
Type Casting is the process of converting one data type
into another data type.

Why Do We Need Type Casting?

Sometimes data is available in one type but we need it in another type to perform calculations, comparisons,
or other operations.

Example:

age = "24"

The value above is a string.

To perform mathematical operations, we must convert it:

age = int(age)

Now age becomes an integer.

Common Type Casting Functions:

1. int()
   Converts data into Integer

   Example:
   int("100") → 100

2. float()
   Converts data into Float

   Example:
   float("99.5") → 99.5

3. str()
   Converts data into String

   Example:
   str(100) → "100"

4. bool()
   Converts data into Boolean

   Example:
   bool(1) → True
   bool(0) → False

Type Casting is widely used in:
- User Input
- Calculations
- Conditions
- Loops
- APIs
- Django Projects
- Data Analysis
- AI & Machine Learning

Important Note:

input() always returns a string.

Therefore type casting is often required when taking numeric input from users.
"""

# -----------------------------------------------------------

"""
Problem 1: String to Integer

Task
Create:
age = "24"

Convert it into an integer.
"""

age = "24"

# Data Type Before Conversion
print(type(age), age)                      # Output: <class 'str'> 24

int_age = int(age)

# Data Type After Conversion
print(type(int_age), int_age)              # <class 'int'> 24

# -----------------------------------

"""
Problem 2: String to Float

Task
Create:
rating = "4.8"

Convert it into a float.
"""

rating = "4.8"

# Data Type Before Conversion
print(type(rating), rating)                            # Output: <class 'str'> 4.8

float_rating = float(rating)

# Data Type After Conversion
print(type(float_rating), float_rating)               # Output: <class 'float'> 4.8

# -----------------------------------

"""
Problem 3: Integer to String

Task
Create:
salary = 50000

Convert it into a string.
"""

salary = 50000

# Data Type Before Conversion
print(type(salary), salary)                            # Output: <class 'int'> 50000

str_salary = str(salary)

# Data Type After Conversion
print(type(str_salary), str_salary)               # Output: <class 'str'> 50000

# -----------------------------------------

"""
Problem 4: Float to Integer

Task
Create:
height = 5.9

Convert it into an integer.
"""

height = 5.9

# Data Type Before Conversion
print(type(height), height)                            # Output: <class 'float'> 5.9

int_height = int(height)

# Data Type After Conversion
print(type(int_height), int_height)               # Output: <class 'int'> 5

# -------------------------------------

"""
Problem 5: Boolean Conversion

Task
Create and test:
bool(1)
bool(0)
bool("")
bool("Python")

Print all outputs.
"""

testbool_1 = bool(1)
print(type(testbool_1), testbool_1)                      # Output: <class 'bool'> True

testbool_2 = bool(0)
print(type(testbool_2), testbool_2)                      # Output: <class 'bool'> False

testbool_3 = bool("")
print(type(testbool_3), testbool_3)                      # Output: <class 'bool'> False

testbool_4 = bool("Python")
print(type(testbool_4), testbool_4)                      # Output: <class 'bool'> True

# --------------------------------------

"""
Problem 6: User Age Calculator
Task
Take age from user.

Remember:
input()

returns string.

Convert it properly and print:

After 5 years your age will be X
"""

print("Age Calculator")

age = int(input("Enter your age: "))

future_age = age + 5
print(f"After 5 years your age will be {future_age} years")

"""
Output:
Age Calculator
Enter your age: 15
After 5 years your age will be 20 years
"""

# -------------------------------------------