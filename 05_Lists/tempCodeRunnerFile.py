"""
🟢 Problem 66 — List + Condition

Start with:

numbers = [5, 12, 18, 25, 31, 40]

Traverse the list and print only the even numbers.

Expected output:

12
18
40
Requirements
Use a for loop
Use an if condition
Work directly with the list
Don't manually print the answers
"""

print()

numbers = [5, 12, 18, 25, 31, 40]

for number in numbers:
   if number % 2 == 0:
      print(number)

"""
Output:
12
18
40
"""

# =================================