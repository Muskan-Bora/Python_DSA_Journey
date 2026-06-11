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

# print("Age Calculator")

# age = int(input("Enter your age: "))

# future_age = age + 5
# print(f"After 5 years your age will be {future_age} years")

"""
Output:
Age Calculator
Enter your age: 15
After 5 years your age will be 20 years
"""

# -------------------------------------------

"""
Problem 7: Product Price Calculator

Task
Take:
Product Price
GST Percentage

Calculate:

Final Price

Use type casting wherever needed.
"""

print("Product Price Calculator")

product_price = (input("Enter Product Price: "))
gst_percent = (input("Enter Gst Percentage: "))

float_product_price = float(product_price)
float_gst_percent = float(gst_percent)

gst_amount = (float_gst_percent / 100) * float_product_price

final_price = float_product_price + float(gst_amount)

print(type(product_price))
print(type(gst_percent))
print(type(float_product_price))
print(type(float_gst_percent))
print(type(final_price))

print(
   f"The Product Price is {float_product_price} "
   f"and GST Percentage is {float_gst_percent}% "
   f"so Final price is {final_price:.2f}"
)

"""
Output:
Product Price Calculator
Enter Product Price: 500
Enter Gst Percentage: 18
<class 'str'>
<class 'str'>
<class 'float'>
<class 'float'>
<class 'float'>
The Product Price is 500.0 and GST Percentage is 18.0% so Final price is 590.00
"""

# ---------------------------------------------------

"""
Problem 8: Type Investigation

Task
Create:
num = "100"

Convert it into:
int
float
bool

Print:
Converted Value
Data Type

for each.
"""

num = "100"

print(f"Original Value: {num}, Data Type: {type(num)}")

int_num = int(num)
print(f"Converted Integer Value: {int_num}, Data Type: {type(int_num)}")

float_num = float(num)
print(f"Converted Float Value: {float_num}, Data Type: {type(float_num)}")

bool_num = bool(num)
print(f"Converted Boolean Value: {bool_num}, Data Type: {type(bool_num)}")

"""
Output:
Original Value: 100, Data Type: <class 'str'>
Converted Integer Value: 100, Data Type: <class 'int'>
Converted Float Value: 100.0, Data Type: <class 'float'>
Converted Boolean Value: True, Data Type: <class 'bool'>
"""

# ----------------------------------------------

"""
Problem 9: User Profile Generator

Task
Take:
Name
Age
Salary

Convert appropriate values into correct data types.
Print a professional profile using f-strings.
"""

print("Profile Generator")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_salary = input("Enter your salary: ")

print(user_name, type(user_name))
print(user_age, type(user_age))
print(user_salary, type(user_salary))

int_user_age = int(user_age)
float_user_salary = float(user_salary)

print(int_user_age, type(int_user_age))
print(float_user_salary, type(float_user_salary))

print(f"Your Profile has generated successfully:\n",
      f"Name: {user_name}\n",
      f"Age: {int_user_age}\n",
      f"Salary: {float_user_salary:.2f}\n")

"""
Output:
Profile Generator
Enter your name: Rohny
Enter your age: 26
Enter your salary: 50000
Rohny <class 'str'>
26 <class 'str'>
50000 <class 'str'>
26 <class 'int'>
50000.0 <class 'float'>
Your Profile has generated successfully:
Name: Rohny
Age: 26
Salary: 50000.00
"""

# -------------------------------------------------------------

"""
Problem 10: Mixed Type Casting Challenge
Task

Create:

marks = "85"
attendance = "92.5"

Convert:

marks → int
attendance → float

Print:

Student Marks: 85
Student Attendance: 92.5%
"""

# --------------------------------------------------------------

"""
Bonus Challenge 1

Predict before running:

print(bool("False"))
print(bool("True"))
print(bool(""))

Then execute and verify.
"""

"""
Bonus Challenge 2

Create:

num1 = "10"
num2 = "20"

First print:

num1 + num2

Then convert them into integers and print:

num1 + num2

Observe the difference.
"""

"""
Bonus Challenge 3 (Important)

Predict before running:

print(int(True))
print(int(False))

What will be the output?

This is a very common Python interview question.
"""