# -----------------------------------------------------

# Python Mini Test

# ------------------------------------------------------

"""
Question 1 — Variables & Output
Create a variable named city and store your city name.

Print:
I live in <city>.

Example:
I live in Mumbai.
"""

city = "Mumbai"

print(f"I live in {city}.")

"""
Output:
I live in Mumbai.
"""

# ============================================== #

"""
Question 2 — Input
Take the user's name as input.

Print:
Welcome, <name>!
"""

first_name = input("Enter your Name: ")

print(f"Welcome, {first_name}!")

"""
Output:
Enter your Name: John
Welcome, John!
"""

# ===============================================

"""
Question 3 — If-Else

Take a number from the user.
Print:
"Positive" if the number is greater than 0.
"Negative" if the number is less than 0.
"Zero" if the number is 0.
"""

num = int(input("Enter a Number: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Invalid")

"""
Output:
Enter a Number: 4
Positive

Enter a Number: 0
Zero

Enter a Number: -7
Negative
"""

# =====================================================

"""
Question 4 — While Loop

Print all numbers from 10 down to 1 using a while loop.
Expected output:
10
9
8
7
6
5
4
3
2
1
"""

number = 10

while number >= 1:
    print(number)
    number -= 1

"""
Output:
10
9
8
7
6
5
4
3
2
1
"""
