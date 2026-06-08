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

# num1 = 20
# num2 = 5

# print("Addition: ", num1, "+", num2, "=", num1 + num2)   
# print("Subtraction: ", num1, "-", num2, "=", num1 - num2)
# print("Multiplication: ", num1, "*", num2, "=", num1 * num2)
# print("Division: ", num1, "/", num2, "=", num1 / num2)
# print("Modulus: ", num1, "%", num2, "=", num1 % num2)
# print("Exponent: ", num1, "**", num2, "=", num1 ** num2)
# print("Floor Division: ", num1, "//", num2, "=", num1 // num2)

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

# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))

# print(f"Sum: {num_1 + num_2}")
# print(f"Difference: {num_1 - num_2}")
# print(f"Product: {num_1 * num_2}")
# print(f"Division: {num_1 / num_2}")

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

"""
Problem 3: Comparison Operators

Task
Create:

age = 24
required_age = 18
"""

age = 24
required_age = 18

equal_to = age == required_age
print(f"{age} == {required_age} = {equal_to}")

not_equal = age != required_age
print(f"{age} != {required_age} = {not_equal}")

greater_than = age > required_age
print(f"{age} > {required_age} = {greater_than}")

lesser_than = age < required_age
print(f"{age} < {required_age} = {lesser_than}")

greater_equalto = age >= required_age
print(f"{age} >= {required_age} = {greater_equalto}")

lesser_equalto = age <= required_age
print(f"{age} <= {required_age} = {lesser_equalto}")

"""
Output: 
24 == 18 = False
24 != 18 = True
24 > 18 = True
24 < 18 = False
24 >= 18 = True
24 <= 18 = False
"""

# ----------------------------------- #

"""
Problem 4: Student Eligibility Check

Task
Ask user for marks.

Check:
Marks >= 35

Print the result.
"""

print("Student Eligibility Check: ")
eligible = input("Please Enter your Marks: ")

is_eligible = int(eligible) >= 35
print("Eligible:", is_eligible)

"""
Output:
Student Eligibility Check: 
Please Enter your Marks: 26
Eligible: False

Student Eligibility Check: 
Please Enter your Marks: 69
Eligible: True
"""

# ----------------------------------------- #

"""
Problem 5: Assignment Operators

Task
Create:
salary = 25000

Print value after every operation.
"""

salary = 25000

salary += 25000
print(salary)                # Output = 50000

salary -= 25000
print(salary)                # Output = 25000

salary *= 25000
print(salary)                # Output = 625000000

salary /= 25000
print(salary)                # Output = 25000.0

salary %= 25000
print(salary)                # Output = 0.0

# -------------------------------------------- #

"""
Problem 6: Logical Operators

Task
Create:
age = 24
has_id = True
"""

age = 24
has_id = True

print(age >= 18 and has_id)  # Output: True

print(age >= 18 or has_id)   # Output: True

print(not has_id)            # Output: False

# ---------------------------------------------- #

"""
Problem 7: Movie Ticket Eligibility

Task
Ask user:
Age
Has Ticket (True/False)

Check whether the person can enter. [Using Logical Opertor]
"""

print("Movie Ticket Eligibility: ")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket (True/False): ")

has_ticket = has_ticket.lower() == "true"

can_enter =  age >= 18 and has_ticket
print("Can Enter:", can_enter)

"""
Output:
Movie Ticket Eligibility: 
Enter your age: 19
Do you have the ticket (True/Flase): True
Can Enter: True

Enter your age: 26
Do you have the ticket (True/Flase): False
Can Enter: False

Movie Ticket Eligibility: 
Enter your age: 16
Do you have the ticket (True/Flase): True
Can Enter: False
"""