# ------------------------------------------------------- #

# Python - user input comcept 

# -----------------------------------

"""
Problem 1: Take Name Input

Task - 
Ask the user to enter their name.
Print a welcome message.
"""

first_name = input("Enter your name: ")
print("Welcome,", first_name)

# Another way in 1 line
print("Welcome,",input("Enter your name: "))

"""
Output:
Enter your name: Rohan
Welcome, Rohan
"""

# ---------------------------------

"""
Problem 2: Multiple Inputs

Task
Ask the user for:
Name
Age
City

Print all details neatly.
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

print(f"My name is {name}, and my age is {age} and i live in {city} city.")

"""
Output:
Name: Ram
Age: 24
City: Mumbai
My name is Ram, and my age is 24 and i live in Mumbai city.
"""

# ---------------------------------

"""
Problem 3: Age After One Year
Task

Ask the user for their age.

Print:

Next year you will be X years old.
"""

your_age = input("Enter your age: ")

print(f"Next year you will be {int(your_age) + 1} years old.")

"""
Output:
Enter your age: 24
Next year you will be 25 years old.
"""

# ---------------------------------

"""
Problem 4: Add Two Numbers

Task
Ask the user for two numbers.
Print their sum.
"""

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

print(f"The sum of the number is {int(num1) + int(num2)}")

"""
Output:
Enter number 1: 10
Enter number 2: 8
The sum of the number is 18
"""

# ---------------------------------

"""
Problem 5: Calculate Rectangle Area
Task

Ask the user for:

Length
Width

Print the area.
"""

# Formula : Area = Length × Width

length = input("Enter length: ")
width = input("Enter width: ")

print(f"The area of the rectangle is {int(length) * int(width)}")

"""
Output:
Enter length: 5
Enter width: 20
The area of the rectangle is 100
"""

# ------------------------------------

"""
Problem 6: Simple Profile Generator

Task
Ask the user for:
Name
Company
Role
Years of Experience

Print a professional profile.
"""

emp_name = input("Enter your name: ")
name_company = input("Enter your company name: ")
role = input("Enter your role: ")
years_of_exp = input("Enter your years of experience: ")

print(f"Hello, {emp_name}.")
print(f"You work as a {role} at {name_company}.")
print(f"You have {years_of_exp} years of experience.")

"""
Output:
Enter your name: Riya
Enter your company name: XYZ Pvt Ltd
Enter your role: Full Stack Developer
Enter your years of experience: 2
Hello, Riya.
You work as a Full Stack Developer at XYZ Pvt Ltd.
You have 2 years of experience.
"""

# -------------------------------------------

"""
Problem 7: Type Investigation

Task
Ask the user for:
Age
Salary

Print the data type immediately after taking input.

Then convert them to appropriate types and print the data type again.
"""

age = input("Enter your age: ")
salary = input("Enter your salary: ")

print(type(age))
print(type(salary))

"""
Output:
<class 'str'>
<class 'str'>
"""

age_1 = int(age)
print(type(age_1), age_1)

salary_1 = float(salary)
print(type(salary_1), salary_1)

"""
Output:
Enter your age: 24
Enter your salary: 25000
<class 'int'> 24
<class 'float'> 25000.0
"""

# ----------------------------------

"""
Bonus Challenge

Task
Create a mini EMI calculator.
Ask for:
Loan Amount
Number of Months

Calculate:

Monthly Amount = Loan Amount / Number of Months

Print the result.
"""

print("Calcuate your EMI Amount for per month")

loan_amount = input("Enter your loan Amount: ")
no_months = input("Enter your umber of months: ")

monthly_emi_amount = float(loan_amount) / int(no_months)
print(f"Your monthly EMI Amount is {float(monthly_emi_amount)} + interest")

"""
Output:
Calcuate your EMI Amount for per month
Enter your loan Amount: 500000
Enter your umber of months: 36
Your monthly EMI Amount is 13888.89 + interest
"""

# -------------------------------------------------------------