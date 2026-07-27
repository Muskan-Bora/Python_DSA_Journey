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

# ==========================================================

"""
Question 5 — While Loop + Logic

Take a number from the user.
Count how many odd digits are present.

Example:
Input:
458927

Output:
Odd digits = 3

(Odd digits are: 5, 9, 7)
"""

num_1 = int(input("Enter a Number: "))
total = 0

while num_1 > 0:
    digit = num_1 % 10
    if digit % 2:
        print(digit)
        total += 1
    num_1 = num_1 // 10

print(f"Total odd digits: {total}")

"""
Output: 
Enter a Number: 458927
7
9
5
Total odd digits: 3
"""

# ==================================================

"""
Question 6 — For Loop

Print the multiplication table of 9.
Expected:

9 x 1 = 9
...
9 x 10 = 90
"""

mul = 9

print("The multiplication table of 9.")

for i in range (1, 11):
    print(f"{mul} x {i} = {mul * i}")

"""
Output:
The multiplication table of 9.
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
"""

# ===========================================================

"""
Question 7 — For Loop + String

Take a word from the user.
Count only consonants.

Rules:
Use for
Don't use len()
Don't use .count()
"""

word = input("Enter a word: ")
count = 0

for letter in word:
    if letter.isalpha() and letter not in "aeiou":
        count += 1

print(count)

"""
Output:
Enter a word: Python Fundamentals
13
"""

# ===========================================

"""
Question 8 — Logic
Print all numbers from 1 to 30 that are divisible by 2 and 3.
"""

for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

"""
Output:
6
12
18
24
30
"""

# =============================================
