# ------------------------------------------------------- #

# Python Operators

# ------------------------------------------------------- #

"""
Python Operators

Definition:
Operators are special symbols used to perform operations on variables and values.

Operators help us:

1. Perform mathematical calculations.
2. Compare values.
3. Combine conditions.
4. Assign values to variables.
5. Check membership and identity.

Common Types of Operators in Python:

1. Arithmetic Operators
   +   Addition
   -   Subtraction
   *   Multiplication
   /   Division
   %   Modulus
   **  Exponent
   //  Floor Division

2. Comparison Operators
   ==  Equal To
   !=  Not Equal To
   >   Greater Than
   <   Less Than
   >=  Greater Than or Equal To
   <=  Less Than or Equal To

3. Assignment Operators
   =
   +=
   -=
   *=
   /=
   %=

4. Logical Operators
   and
   or
   not

5. Membership Operators
   in
   not in

6. Identity Operators
   is
   is not

Why Are Operators Important?

Operators are used everywhere in Python:
- Calculations
- Conditions
- Loops
- Functions
- APIs
- Django Projects
- Data Analysis
- AI & Machine Learning
"""

#  -------------------------------------------------------------------- #

"""
Problem 1: Arithmetic Operators

Task
Create two variables:

num1 = 20
num2 = 5

Perform and print:
Addition
Subtraction
Multiplication
Division
Modulus
Exponent
Floor Division
"""

num1 = 20
num2 = 5

print("Addition: ", num1, "+", num2, "=", num1 + num2)   
print("Subtraction: ", num1, "-", num2, "=", num1 - num2)
print("Multiplication: ", num1, "*", num2, "=", num1 * num2)
print("Division: ", num1, "/", num2, "=", num1 / num2)
print("Modulus: ", num1, "%", num2, "=", num1 % num2)
print("Exponent: ", num1, "**", num2, "=", num1 ** num2)
print("Floor Division: ", num1, "//", num2, "=", num1 // num2)

"""
Output:
Addition:  20 + 5 = 25
Subtraction:  20 - 5 = 15
Multiplication:  20 * 5 = 100
Division:  20 / 5 = 4.0
Modulus:  20 % 5 = 0
Exponent:  20 ** 5 = 3200000
Floor Division:  20 // 5 = 4
"""

# ---------------------------------- #

"""
Problem 2: User Calculator

Task
Take two numbers from the user.

Print:
Sum
Difference
Product
Division
"""

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print(f"Sum: {num_1 + num_2}")
print(f"Difference: {num_1 - num_2}")
print(f"Product: {num_1 * num_2}")
print(f"Division: {num_1 / num_2}")

"""
Output:
Enter first number: 60
Enter second number: 5
Sum: 65
Difference: 55
Product: 300
Division: 12.0
"""

# ----------------------------------- #