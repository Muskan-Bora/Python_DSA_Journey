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

"""
Problem 1 — Basic if

Create:
age = 24

Check:
If age is 18 or above, print:

Adult
"""

age = 24

if age == 18 or age > 18:
    print("Adult")           # Output: Adult

# ----------------------------

"""
Problem 2 — if-else

Take age from user.
If age >= 18:
Eligible to Vote

Else:
Not Eligible to Vote
"""

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

"""
Output:
Enter your age: 19
Eligible to Vote

Enter your age: 16
Not Eligible to Vote
"""

# ----------------------------------------

"""
Problem 3 — Positive or Negative [using if-elif-else]

Take a number from user.
Check:
Positive
Negative
Zero
"""

num = int(input("Enter the number: "))

if num > 0:
    print(num, "Positive")
elif num < 0:
    print(num, "Negative")
else:
    print(num, "Zero")

"""
Output:
Enter the number: 2
2 Positive

Enter the number: -5
-5 Negative

Enter the number: 0
0 Zero
"""

# ---------------------------------

"""
Problem 4 — Even or Odd

Take number from user.
Check whether number is:
Even
or
Odd
"""

num_1 = int(input("Enter the number: "))

if num_1 % 2 == 0:
    print(num_1, "even")
else:
    print(num_1, "odd")

"""
Output:
Enter the number: 5
5 odd

Enter the number: 10
10 even

Enter the number: -6
-6 even
"""

# -----------------------------------

"""
Problem 5 — Pass or Fail

Take marks from user.
If marks >= 35:
Pass

Else:
Fail
"""

user_marks = int(input("Enter your marks: "))

if user_marks >= 35:
    print(f"Congratulations, your result is pass and got {user_marks} marks.")
else:
    print(f"Sorry, Better luck next time you got {user_marks} marks so your result is fail.")

"""
Output:
Enter your marks: 90
Congratulations, your result is pass and got 90 marks.

Enter your marks: 32
Sorry, Better luck next time you got 32 marks so your result is fail.
"""

# -------------------------------------

"""
Problem 6 — Grade Calculator

Take marks.

Rules:
90+ → Grade A
75 - 89 → Grade B
50 - 74 → Grade C
Below 50 → Grade D
"""

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Sorry, your marks is invalid")
elif marks >= 90:
    print(f"Outstanding you scored {marks} marks, so your Grade is A.")
elif marks >= 75 and marks <= 89:
    print(f"Good you scored {marks} marks, so your Grade is B.")
elif marks >= 50 and marks <= 74:
    print(f"Satisfactory, you scored {marks} marks, so your Grade is C.")
else:
    print(f"You need to work hard more you scored {marks} marks, so your Grade is D.")

"""
Output:

Enter your marks: 152
Sorry, your marks is invalid

Enter your marks: 90
Outstanding you scored 90 marks, so your Grade is A.

Enter your marks: 75
Good you scored 75 marks, so your Grade is B.

Enter your marks: 52
Satisfactory, you scored 52 marks, so your Grade is C.

Enter your marks: 49
You need to work hard more you scored 49 marks, so your Grade is D.
"""

# ----------------------------------

"""
Problem 7 — Salary Bonus

Take salary.

Rules:
salary >= 50000 → Bonus = 10000
salary >= 30000 → Bonus = 5000
Otherwise → Bonus = 2000

Print final bonus.
"""

salary = int(input("Enter your salary: "))

if salary >= 50000:
    print(f"Congratulations, your salary is {salary} so, you will receive 10000 in Bonus so after Bonus your total salary will be {salary + 10000}.")
elif salary >= 30000:
    print(f"Congratulations, your salary is {salary} so, you will receive 5000 in Bonus so after Bonus your total salary will be {salary + 5000}.")
else:
    print(f"OK, your salary is {salary} so, you will receive only 2000 in Bonus so after Bonus your total salary will be {salary + 2000}.")

"""
Output:
Enter your salary: 50000
Congratulations, your salary is 50000 so, you will receive 10000 in Bonus so after Bonus your total salary will be 60000.

Enter your salary: 49000 
Congratulations, your salary is 49000 so, you will receive 5000 in Bonus so after Bonus your total salary will be 54000.

Enter your salary: 25000
OK, your salary is 25000 so, you will receive only 2000 in Bonus so after Bonus your total salary will be 27000.
"""

# --------------------------------------------------

"""
Problem 8 — Login Check

Create:
stored_username = "admin"
stored_password = "python123"

Take input:
username
password

Check login.
Print:
Login Successful
or
Invalid Credentials
"""

stored_username = "admin"
stored_password = "python123"

username = input("Enter your username: ").lower().strip()
password = input("Enter your passowrd: ").lower().strip()

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials. Please try again.")

"""
Output:
Enter your username: Admin
Enter your passowrd: Python123
Invalid Credentials. Please try again.

Enter your username: admin
Enter your passowrd: Python123
Invalid Credentials. Please try again.

Enter your username: admin
Enter your passowrd: python123 
Login Successful
"""

# ----------------------------------------------

"""
Problem 9 — Movie Entry (Nested If)

Take:
age
has_ticket (True/False)

Rules:
If age >= 18:
Check ticket
Else:
Not allowed

Use nested if.
"""

age = int(input("Enter your age: "))
ticket_input = input("Do yo have ticket? yes/no: ")
has_ticket = ticket_input.lower()

if age >= 18:
    if has_ticket == "yes":
        print("OK, you are allowed. Please enter and enjoy your show.")
    else:
        print("Sorry you don't have ticket so you are not allowed.")
else:
    print("Sorry you are underage so you are not allowed.")

"""
Output:
Enter your age: 19
Do yo have ticket? yes/no: no
Sorry you don't have ticket so you are not allowed.

Enter your age: 19
Do yo have ticket? yes/no: Yes
OK, you are allowed. Please enter and enjoy your show.

Enter your age: 17
Do yo have ticket? yes/no: yes
Sorry you are underage so you are not allowed.
"""

# -------------------------------------------

"""
Problem 10 — Biggest of Today 

Mini ATM Withdrawal System
Take:
account_balance
withdrawal_amount

Rules:
If withdrawal <= balance → Success
Else → Insufficient Balance

Print remaining balance if success.
"""

print("Mini ATM Withdrawal System.")

account_balance = int(input("Enter your Balance Amount: "))
withdrawal_amount = int(input("Enter the Amount you want to Withdraw: "))

if withdrawal_amount <= 0 or account_balance <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount <= account_balance:
    bal_after_withdraw = account_balance - withdrawal_amount
    print(f"Your withdrawal is Success, and your remaining balance after withdrwal is {bal_after_withdraw}")
else: 
    print(f"Sorry, currently insufficient balance, you can withdraw the amount upto {account_balance}")

"""
Output:
Mini ATM Withdrawal System.
Enter your Balance Amount: 50000
Enter the Amount you want to Withdraw: 20000
Your withdrawal is Success, and your remaining balance after withdrwal is 30000

Mini ATM Withdrawal System.
Enter your Balance Amount: 24000
Enter the Amount you want to Withdraw: 25000
Sorry, currently insufficient balance, you can withdraw the amount upto 24000
"""

# ---------------------------------------------------------------- #