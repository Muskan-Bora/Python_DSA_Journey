# ===============================================

"""
🐍 Python Tuples — Complete Notes

1. What is a Tuple?
A tuple is a built-in Python data structure used to store multiple items in a single variable.

Tuples are ordered and immutable.
Ordered means the items have a defined position.
Immutable means individual elements cannot be reassigned, added, or removed after the tuple is created.

2. Creating Tuples

numbers = (10, 20, 30, 40)
names = ("Muskan", "Doraemon", "Aarav")
student = ("Muskan", 22, 85.5, True)

3. Empty Tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))
print(len(empty_tuple))

4. Single-Element Tuple

a = (10)       # Integer, not a tuple
b = (10,)      # Tuple containing one element
c = 10,        # Also a tuple

A comma is required to create a single-element tuple.

5. Checking the Type

numbers = (10, 20, 30)
print(type(numbers))  # <class 'tuple'>

6. Tuple Indexing

languages = ("Python", "Django", "JavaScript", "React")

print(languages[0])   # Python
print(languages[2])   # JavaScript
print(languages[-1])  # React
print(languages[-2])  # JavaScript

Positive indexing starts at 0.
Negative indexing starts at -1 from the end.

7. Tuple Slicing

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[3:])    # (40, 50, 60)
print(numbers[::2])   # (10, 30, 50)
print(numbers[::-1])  # (60, 50, 40, 30, 20, 10)

Syntax: tuple_name[start:stop:step]
The stop index is excluded.
Slicing returns a new tuple.

8. Membership Operators

languages = ("Python", "Django", "React")

print("Python" in languages)      # True
print("Java" not in languages)    # True

9. Tuple Length

numbers = (10, 20, 30, 40, 50)
print(len(numbers))  # 5

len() counts top-level elements.
A nested list counts as one element.

10. Tuple Traversal

languages = ("Python", "Django", "React")

for language in languages:
    print(language)

11. Traversal Using Index

for index in range(len(languages)):
    print(index, languages[index])

12. Traversal Using enumerate()

for index, language in enumerate(languages):
    print(index, language)

enumerate() provides each element's index and value.

13. Tuple count()

numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))  # 3

count(value) returns the number of occurrences.

14. Tuple index()

numbers = (10, 20, 30, 20, 40)
print(numbers.index(20))  # 1

index(value) returns the first matching index.
If the value is missing, it raises ValueError.

15. Immutability

numbers = (10, 20, 30)

# numbers[0] = 100
# TypeError: tuples do not support item assignment

Tuples do not support direct element reassignment,
append(), or remove().

16. Tuple With a Mutable Element

data = (10, [20, 30])
data[1].append(40)
print(data)  # (10, [20, 30, 40])

The tuple cannot be reassigned at the element level,
but a mutable object inside it may still be modified.

17. Common Uses

- Coordinates
- Fixed configuration values
- RGB colour values
- Returning multiple values from functions

18. List vs Tuple

List:
- Uses square brackets []
- Mutable
- Supports append(), insert(), remove(), and other
  in-place modification methods

Tuple:
- Usually uses parentheses ()
- Immutable at the element level
- Has count() and index() methods
- Useful for fixed collections of values

Important:
Tuples can be created without parentheses when commas separate the values, for example: coordinates = 10, 20
"""

# ===================================================

## Tuple Practice ##

"""
Problem 1 — Creating Tuples
Beginner

Task: Create the following three tuples:

numbers containing 10, 20, 30, 40, 50

languages containing "Python", "Django", "React"

student containing "Muskan", 22, 85.5, True

Then print each tuple and its data type using type().

Requirements
Use parentheses ().
Use meaningful variable names.
Use print() and type().

"""

numbers = (10, 20, 30, 40, 50)
print(f"{numbers}, And the data type is {type(numbers)}")

languages = ("Python", "Django", "React")
print(f"{languages}, And the data type is {type(languages)}")

student = ("Muskan", 22, 85.5, True)
print(f"{student}, And the data type is {type(student)}")

"""
Output:
(10, 20, 30, 40, 50), And the data type is <class 'tuple'>
('Python', 'Django', 'React'), And the data type is <class 'tuple'>
('Muskan', 22, 85.5, True), And the data type is <class 'tuple'>
"""

# =========================================

"""
Problem 2 — Empty Tuple
Beginner

Task: Create an empty tuple named empty_tuple.

Then print:

The tuple itself.

Its data type using type().

Its length using len().

Expected output:

()
<class 'tuple'>
0

Requirements
Use ().
Use print(), type(), and len().
Write the code yourself without copying the notes.
"""

print()

empty_tuple = ()

print(empty_tuple)                                      # Output: ()

print(f"Its data type is {type(empty_tuple)}")          # Output: Its data type is <class 'tuple'>

print(f"Its length is {len(empty_tuple)}")              # Output: Its length is 0

# =========================================

"""
Problem 3 — Tuple or Integer?
Important concept

Create two variables:

first_value = (50)

second_value = (50,)

Then print each variable and its data type using type().

Expected output:

50
<class 'int'>
(50,)
<class 'tuple'>

Requirements
Use both assignments exactly as shown.
Use print() and type().
Explain in a comment why their data types differ.
"""

print()

first_value = (50)

print(first_value)                 # Output: 50
print(type(first_value))           # Output: <class 'int'>

"""
Reason: first_value = (50) is an integer because the parentheses only group the expression. They don't create a tuple.
"""

second_value = (50,)

print(second_value)                 # Output: (50,)
print(type(second_value))           # Output: <class 'tuple'>

""" 
Reason:
second_value = (50,) is a tuple because the comma is what makes it a tuple.
"""

# ================================================

"""
Problem 4 — Mixed Tuple
Beginner

Task: Create a tuple named employee containing:
- Name: "Muskan"
- Age: 22
- Salary: 25000
- Experience: 2.5
- Currently employed: True
Then print:
1. The entire tuple.
2. Its data type using type().
3. Its length using len().
Expected output:
('Muskan', 22, 25000, 2.5, True)
<class 'tuple'>
5

Requirements
- Use parentheses ().
- Use print(), type(), and len().
- Add a comment explaining why the tuple's length is 5.
"""

print()

employee = ("Muskan", 22, 25000, 2.5, True)

print(employee)                                   # Output: ('Muskan', 22, 25000, 2.5, True)

print(f"Its Data type is {type(employee)}")       # Output: Its Data type is <class 'tuple'>

print(f"Its Length is {len(employee)}")           # Output: Its Length is 5

# Length is 5 because the tuple contains five elements.

# ========================================== 

"""
Problem 5 — Tuple Indexing
Beginner

Given this tuple:
languages = ("Python", "Django", "JavaScript", "React", "SQL")

Task: Print the following values using indexing:
1. The first element.
2. The third element.
3. The last element.
4. The second-last element.
Expected output:
Python
JavaScript
SQL
React

Requirements
- Use positive and negative indexing.
- Do not use a loop.
- Do not use slicing.
"""

print()

languages = ("Python", "Django", "JavaScript", "React", "SQL")

print(languages[0])                # Output: Python
print(languages[2])                # Output: JavaScript
print(languages[4])                # Output: SQL
print(languages[-2])               # Output: React

# ============================================

"""
Problem 6 — Access from the End
Beginner

Given:
numbers = (10, 20, 30, 40, 50, 60, 70)

Task: Print these elements using negative indexing only:
1. The last element.
2. The third-last element.
3. The fifth-last element.
Expected output:
70
50
30

Requirements
- Use negative indexes only.
- No loops.
- No slicing.
"""

print()

numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[-1])      # Output: 70
print(numbers[-3])      # Output: 50
print(numbers[-5])      # Output: 30

# ======================================

"""
Problem 7 — Basic Tuple Slicing
Beginner

Given this tuple:
numbers = (10, 20, 30, 40, 50, 60, 70)

Task: Print the following slices:
1. Elements from index 1 to index 4 (excluding index 4).
2. The first three elements.
3. All elements from index 3 to the end.
Expected output:
(20, 30, 40)
(10, 20, 30)
(40, 50, 60, 70)

Requirements
- Use tuple slicing.
- Use print().
- Do not use loops or list comprehensions.
"""

print()

numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:4])    # Output: (20, 30, 40)

print(numbers[0:3])    # Output: (10, 20, 30)

print(numbers[3:])     # Output: (40, 50, 60, 70)

# ==============================================

"""
Problem 8 — Step Slicing
Beginner

Given:
numbers = (10, 20, 30, 40, 50, 60, 70, 80)

Task: Print the following:
1. Every second element, starting from the first element.
2. Every second element, starting from the second element.
3. Every third element, starting from the first element.
Expected output:
(10, 30, 50, 70)
(20, 40, 60, 80)
(10, 40, 70)

Requirements
- Use tuple slicing with the step parameter.
- Use print().
- No loops or list comprehensions.
"""

print()

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

print(numbers[::2])            # Output: (10, 30, 50, 70)

print(numbers[1::2])            # Output: (20, 40, 60, 80)

print(numbers[::3])            # Output: (10, 40, 70)

# ===================================

"""
Problem 9 — Reverse Slicing
Beginner

Given:
numbers = (10, 20, 30, 40, 50, 60)

Task: Print:
1. The entire tuple in reverse order.
2. Every second element in reverse order, starting from the last element.
Expected output:
(60, 50, 40, 30, 20, 10)
(60, 40, 20)

Requirements
- Use tuple slicing.
- Use a negative step.
- Use print().
- No loops or list comprehensions.
"""

print()

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[-1::-1])         # Output: (60, 50, 40, 30, 20, 10)

print(numbers[-1::-2])         # Output: (60, 40, 20)

# ==============================

"""
Problem 10: Tuple Membership
Topic: in and not in

Your turn
Problem statement
You are given the following tuple:
languages = ("Python", "Django", "JavaScript", "React", "SQL")

Write a Python program that:
1. Checks whether "Python" exists in the tuple.
2. Checks whether "Java" exists in the tuple.
3. Checks whether "React" does not exist in the tuple.
4. Checks whether "C++" does not exist in the tuple.
Requirements:
- Use the in and not in operators.
- Print all four results using clear, descriptive messages.
- Use f-strings for your output.
"""

print()

languages = ("Python", "Django", "JavaScript", "React", "SQL")

languages_test_1 = "Python" in languages
print(f"{languages_test_1}, Python exist in the Tuple")

languages_test_2 = "Java" in languages
print(f"{languages_test_2}, Java does not exist in the Tuple")

languages_test_3 = "React" not in languages
print(f"{languages_test_3}, React does not exist in the Tuple")

languages_test_4 = "C++" not in languages
print(f"{languages_test_4}, C++ does not exist in the Tuple")

"""
Output:
True, Python exist in the Tuple
False, Java does not exist in the Tuple
False, React does not exist in the Tuple
True, C++ does not exist in the Tuple
"""

# ==================================================

"""
🐍 Problem 11: Tuple Traversal Using a for Loop
Now let's move forward! This problem will help you practise looping through a tuple.
Your next challenge

Problem statement
Given this tuple:
numbers = (10, 20, 30, 40, 50)

Write a Python program that:
1. Uses a for loop to traverse the tuple.
2. Prints each number on a separate line.
3. Prints the square of each number on a separate line, using a descriptive message.
Requirements:
- Use a for loop.
- Do not use while.
- Do not use enumerate() yet.
- You may use a loop variable and an f-string.
- No need to store the results in another tuple or list.
"""

print()

numbers = (10, 20, 30, 40, 50)

for number in numbers:
    print(number)
    print(f"The square of {number} is {number} x {number} = {number * number}")

"""
Output:
10
The square of 10 is 10 x 10 = 100
20
The square of 20 is 20 x 20 = 400
30
The square of 30 is 30 x 30 = 900
40
The square of 40 is 40 x 40 = 1600
50
The square of 50 is 50 x 50 = 2500
"""

# ======================================

"""
Problem statement 12:
Given this tuple:
subjects = ("Python", "Django", "SQL", "React")

Write a Python program that:
1. Uses a for loop with enumerate().
2. Prints each subject alongside its index.
3. Starts indexing from 1 instead of the default 0.
Requirements
- Use enumerate().
- Use a for loop.
- Use two loop variables: one for the index and one for the subject.
- Use an f-string to display each result.
- Do not use while or manually increment a counter.
"""

print()

subjects = ("Python", "Django", "SQL", "React")

for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")

"""
Output:
1. Python
2. Django
3. SQL
4. React
"""

# ===================================

"""
🐍 Problem 13: Tuple Traversal Using range() and len()
Now let's practise another approach to tuple traversal, using indexes directly.
Your next challenge

Problem statement
Given this tuple:
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

Write a Python program that:
1. Uses for, range(), and len() to traverse the tuple.
2. Prints each fruit alongside its index.
3. Uses zero-based indexing, starting from 0.
Requirements
- Use range(len(fruits)).
- Access each fruit using its index.
- Use an f-string for each output line.
- Do not use enumerate() or while.
- Don't create another list or tuple.
"""

print()

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

for i in range(len(fruits)):
    print(f"{i}. {fruits[i]}")

"""
Output:
0. Apple
1. Banana
2. Mango
3. Orange
4. Grapes
"""

# ==========================================

"""
Problem statement: 14
Given this tuple:
numbers = (10, 20, 30, 40, 50, 60)

Write a Python program that:
1. Uses a for loop to traverse the tuple.
2. Checks whether each number is greater than 30.
3. Prints only the numbers greater than 30.
4. Counts how many numbers are greater than 30 and prints the final count.
Requirements
- Use a for loop.
- Use an if statement.
- Store the count in a variable initialised before the loop.
- Increase the count when a number satisfies the condition.
- Do not use while, enumerate(), sum(), or list comprehensions.
- Use f-strings for the output.
"""

print()

numbers = (10, 20, 30, 40, 50, 60)

count = 0

for number in numbers:
    if number > 30:
        print(number)
        count += 1

print(f"So, the final count is {count}")

"""
Output:
40
50
60
So, the final count is 3
"""

# ==========================================

"""
Problem statement: 15
Given this tuple:
numbers = (10, 20, 30, 40, 50)

Write a Python program that:
1. Uses a for loop to traverse the tuple.
2. Calculates the total of all numbers without using sum().
3. Counts how many numbers are in the tuple.
4. Calculates and prints the average.
Requirements
- Use a for loop.
- Initialise total and count before the loop.
- Update both variables inside the loop.
- Calculate the average after the loop.
- Do not use sum(), while, enumerate(), or list comprehensions.
- Use f-strings for the final output.
"""

print()

numbers = (10, 20, 30, 40, 50)

total = 0
count = 0

for number in numbers:
    count += 1
    total = total + number

average = total / count

print(f"The count of numbers in tuple is {count}")
print(f"The total of the tuple is {total}")
print(f"The average of the tuple is {average}")


"""
Output:
The count of numbers in tuple is 5
The total of the tuple is 150
The average of the tuple is 30.0
"""

# ============================================

"""
Problem 16: Tuple Traversal with a Condition
Filter and count even numbers
Topics: tuples, for, if, modulo operator

Problem statement
Given this tuple:
numbers = (12, 7, 18, 25, 30, 9, 42, 15)

Write a Python program that:
1. Traverses the tuple using a for loop.
2. Checks whether each number is even.
3. Prints only the even numbers.
4. Counts how many even numbers are present.
5. Prints the final count.

Requirements
- Use a for loop and an if statement.
- Use the modulo operator % to check even numbers.
- Initialise the counter before the loop.
- Increment the counter only when a number is even.
- Use f-strings for descriptive output.
- Do not use while, enumerate(), sum(), or list comprehensions.
- Include your expected output in a comment.
"""

print()

numbers = (12, 7, 18, 25, 30, 9, 42, 15)

count = 0

print("The even numbers are: ")

for number in numbers:
    if number % 2 == 0:
        print(number)
        count += 1

print(f"The final count of the even numbers is {count}")

"""
Output:
The even numbers are: 
12
18
30
42
The final count of the even numbers is 4
"""

# ===========================================

"""
Problem 17: Filter and Count Odd Numbers

Problem statement
Given this tuple:
numbers = (11, 24, 35, 40, 17, 52, 63, 28)

Write a Python program that:
1. Traverses the tuple using a for loop.
2. Checks whether each number is odd.
3. Prints only the odd numbers.
4. Counts how many odd numbers are present.
5. Prints the final count.

Requirements
- Use a for loop and an if statement.
- Use % to check whether a number is odd.
- Initialise the counter before the loop.
- Increment the counter only when the condition is true.
- Use descriptive output messages and f-strings.
- Do not use while, enumerate(), sum(), or list comprehensions.
- Include the expected output in a comment.
"""

print()

numbers = (11, 24, 35, 40, 17, 52, 63, 28)

count = 0

print("The odd numbers are:")

for number in numbers:
    if number % 2:
        print(number)
        count += 1

print(f"The final count of the odd number is {count}")

"""
Output:
The odd numbers are:
11
35
17
63
The final count of the odd number is 4
"""

# =============================================

"""
Problem 18: Count Numbers Greater Than the Average

Problem statement
Given this tuple:
numbers = (10, 20, 30, 40, 50, 60)

Write a Python program that:
1. Calculates the average of all numbers using a for loop (do not use sum()).
2. Prints the calculated average.
3. Traverses the tuple again using a for loop.
4. Prints only the numbers greater than the average.
5. Counts and prints how many numbers are greater than the average.

Requirements
- Use for loops and if statements.
- Initialise the total and count variables before the appropriate loops.
- Calculate the average before checking which numbers exceed it.
- Use descriptive output messages and f-strings.
- Do not use while, enumerate(), sum(), or list comprehensions.
- Include your expected output in a comment.
"""

print()

numbers = (10, 20, 30, 40, 50, 60)

total = 0
count= 0
average = 0

for number in numbers: 
    count += 1
    total = total + number

average = total / count
print(f"The average of all numbers is {average}")

count_greater_avg = 0

print("The numbers which are greater than the average:")

for num in numbers:
    if num > average:
        print(num)
        count_greater_avg += 1

print(f"The count of the numbers which are greater than average is {count_greater_avg}")

"""
Output:
The average of all numbers is 35.0
The numbers which are greater than the average:
40
50
60
The count of the numbers which are greater than average is 3
"""

# =======================================

"""
Problem 19: Find the Largest Number in a Tuple

Problem statement
Given this tuple:
numbers = (25, 12, 48, 7, 63, 31, 54)

Write a Python program that:
1. Finds the largest number using a for loop.
2. Prints the largest number with a descriptive message.

Requirements
- Use a for loop.
- Do not use max() or sorted().
- Initialise a variable to hold the largest number before the loop.
- Compare each number with the current largest value and update it when necessary.
- Use an if statement.
- Use an f-string for the final output.
- Include the expected output in a comment.
"""

print()

numbers = (25, 12, 48, 7, 63, 31, 54)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is {largest}")

"""
Output:
The largest number is 63
"""

# ============================================

"""
Problem 20 — Find the Smallest Number in a Tuple 🌱

numbers = (34, 12, 56, 7, 89, 23, 5, 41)

Write a Python program that:
1. Finds the smallest number using a for loop.
2. Prints the smallest number with a descriptive message.

Requirements:
- Use a for loop.
- Do not use min() or sorted().
- Initialise a variable to hold the smallest number before the loop.
- Compare each number with the current smallest value and update it when necessary.
- Use an if statement.
- Use an f-string for the final output.
- Include the expected output in a comment.
"""

print()

numbers = (34, 12, 56, 7, 89, 23, 5, 41)

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"The smallest number is {smallest}")

"""
Output:
The smallest number is 5
"""

# =============================================

"""
Problem 21 — Count Occurrences of an Element in a Tuple 
Given this tuple:
numbers = (10, 20, 10, 30, 40, 10, 50, 20, 10)

Write a Python program that:
1. Counts how many times the number 10 appears in the tuple.
2. Prints the final count with a descriptive message.

Requirements:
- Use a for loop.
- Do not use the tuple's .count() method.
- Initialise a counter before the loop.
- Use an if statement to check whether each number equals 10.
- Increase the counter whenever a match is found.
- Use an f-string for the final output.
- Include the expected output in a comment.
"""

print()

numbers = (10, 20, 10, 30, 40, 10, 50, 20, 10)

count = 0

for number in numbers:
    if number == 10:
        count += 1

print(f"The final count of the number 10 is {count}")

"""
Output:
The final count of the number 10 is 4
"""

# =====================================================

"""
Problem 22 — Find All Positions of an Element in a Tuple

Given this tuple:
numbers = (10, 20, 10, 30, 40, 10, 50, 20, 10)

Write a Python program that finds and prints every index position where the number 10 appears.
Requirements
1. Use a for loop with range() and len().
2. Do not use the tuple's .index() method.
3. Use an if statement to check whether the current element equals 10.
4. Print the index whenever a match is found.
5. Use an f-string for the output.
6. Include the expected output in a comment.
"""

print()

numbers = (10, 20, 10, 30, 40, 10, 50, 20, 10)

print("The index position where the number 10 appears is: ")

for i in range(len(numbers)):
    if numbers[i] == 10:
        print(i)

"""
Output:
The index position where the number 10 appears is: 
0
2
5
8
"""

# ====================================

"""
Problem 23 — Count Even and Odd Numbers in a Tuple 🔢

Let's build on your for loop and if statement skills.
Given this tuple:
numbers = (12, 7, 18, 25, 30, 9, 42, 15, 8, 11)

Write a Python program that:
1. Counts how many numbers are even.
2. Counts how many numbers are odd.
3. Prints both counts using descriptive f-strings.
Requirements:
- Use a for loop.
- Use if-else.
- Initialise two counters before the loop.
- Use the modulo operator % to identify even and odd numbers.
- Do not use count() or any other built-in counting shortcut.
- Include the expected output in a comment.
"""

print()

numbers = (12, 7, 18, 25, 30, 9, 42, 15, 8, 11)

count_even = 0
count_odd = 0

for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"The total number of even numbers is {count_even}")
print(f"The total number of odd numbers is {count_odd}")

"""
Output:
The total number of even numbers is 5
The total number of odd numbers is 5
"""

# ==================================

"""
Problem 24 — Find the Second Largest Number in a Tuple 🧠

Given this tuple:
numbers = (25, 12, 48, 7, 63, 31, 54)

Write a Python program that:
1. Finds the second-largest number in the tuple.
2. Prints the result using a descriptive f-string.
Requirements
- Use a for loop.
- Do not use sorted() or max().
- Use if statements to compare and update values.
- Initialise the variables before the loop.
- Include the expected output in a comment.
"""

print()

numbers = (25, 12, 48, 7, 63, 31, 54)

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number < largest:
        second_largest = number

print(f"The second largest number in the tuple is {second_largest}")

"""
Output:
The second largest number in the tuple is 54
"""

# =================================

"""
Problem 25 — Remove Duplicate Values from a Tuple
Given this tuple:
numbers = (10, 20, 10, 30, 20, 40, 10, 50)

Write a Python program that creates a new tuple containing only unique values, preserving their original order.
Expected result: (10, 20, 30, 40, 50)
Requirements
1. Use a for loop.
2. Do not use set() or any other shortcut that removes duplicates automatically.
3. Use an if statement to check whether a number has already been added.
4. Preserve the original order.
5. Print the new tuple using a descriptive message.
6. Include the expected output in a comment.
"""

print()

numbers = (10, 20, 10, 30, 20, 40, 10, 50)

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"The new Tuple is {tuple(unique_numbers)}")

"""
Output:
The new Tuple is (10, 20, 30, 40, 50)
"""

# ===============================================

"""
Problem 26 — Find Common Elements Between Two Tuples
Given these two tuples:
tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (30, 50, 70, 90, 10, 100)

Write a Python program that finds and prints the elements that appear in both tuples, preserving the order in which they
appear in tuple1.
Expected result: (10, 30, 50)
Requirements
1. Use a for loop.
2. Use an if statement to check whether an element from tuple1 exists in tuple2.
3. Do not use set() or any automatic intersection shortcut.
4. Store the common elements in a list first.
5. Convert the resulting list into a tuple.
6. Print the result using an f-string.
7. Include the expected output in a comment.
"""

print()

tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (30, 50, 70, 90, 10, 100)

common_element = []

for number in tuple1:
    if number in tuple2:
        common_element.append(number)

print(f"The common elements in both the tuples with its preserving order of tuple1 are {tuple(common_element)}")

"""
Output:
The common elements in both the tuples with its preserving order of tuple1 are (10, 30, 50)
"""

# ========================================

"""
Problem 27 — Find Elements Present in One Tuple but Not the Other 
Now let's build on Problem 26.
Given these tuples:
tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (30, 50, 70, 90, 10, 100)

Write a Python program that finds the elements that appear in tuple1 but do not appear in tuple2.
Expected result: (20, 40, 60)
Requirements
1. Use a for loop to traverse tuple1.
2. Use an if statement with the not in operator.
3. Do not use set() or any automatic difference operation.
4. Store the matching elements in a list.
5. Convert the list into a tuple.
6. Print the result using an f-string.
7. Include the expected output in a comment.
"""

tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (30, 50, 70, 90, 10, 100)

print()

uncommon_elements = []

for number in tuple1:
    if number not in tuple2:
        uncommon_elements.append(number)

print(f"The elements that appear in tuple1 but do not appear in tuple2 are {tuple(uncommon_elements)}")

"""
Output:
The elements that appear in tuple1 but do not appear in tuple2 are (20, 40, 60)
"""

# =========================================

"""
Problem 28 — Check Whether One Tuple Is a Subset of Another 
Let's practise membership checks again, but this time we'll check whether every element of one tuple exists in another tuple.
Given these tuples:
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (20, 40)

Write a Python program to determine whether every element in tuple2 is present in tuple1.
Expected output:
All elements of tuple2 are present in tuple1: True

Requirements
1. Use a for loop.
2. Use an if statement to check membership.
3. Do not use set() or automatic subset operations.
4. Initialise a Boolean variable before the loop.
5. If any element of tuple2 is missing from tuple1, update the Boolean variable to False.
6. Print the result using an f-string.
7. Include the expected output in a comment.
"""

print()

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (20, 40)

result = True

for number in tuple2:
    if number not in tuple1:
        result = False

print(f"All elements of tuple2 are present in tuple1: {result}")

"""
Output:
All elements of tuple2 are present in tuple1: True
"""

# ============================================

"""
Problem 29 — Check Whether Two Tuples Are Equal 🐍
Given these tuples:
tuple1 = (10, 20, 30, 40)
tuple2 = (10, 20, 30, 40)

Write a Python program to check whether the two tuples contain the same elements in the same order.
Expected output:
Both tuples are equal: True

Requirements
1. Use a for loop.
2. Do not use tuple1 == tuple2 to perform the whole comparison.
3. Initialise a Boolean variable before the loop.
4. Compare corresponding elements at the same index.
5. If a mismatch is found, update the Boolean variable to False.
6. Print the result using an f-string.
7. Include the expected output in a comment.
"""

print()

tuple1 = (10, 20, 30, 40)
tuple2 = (10, 20, 30, 40)

result = True

for i in range(len(tuple1)):
    if tuple1[i] != tuple2[i]:
        result = False

print(f"Both tuples are equal: {result}")

"""
Output:
Both tuples are equal: True
"""

# ================================

"""
Problem 30 — Find the First Repeated Element in a Tuple 
Let's build on your duplicate-checking skills from Problem 25.
Given this tuple:
numbers = (10, 20, 30, 20, 40, 50, 10)

Write a Python program that finds and prints the first element that appears again while traversing the tuple from left to right.
Expected output:
The first repeated element is 20

Requirements
1. Use a for loop.
2. Do not use set() or automatic duplicate-removal shortcuts.
3. Use a list to store elements already visited.
4. Use an if-else statement to check for a repeated element.
5. Stop the loop when the first repeated element is found.
6. Print the result using an f-string.
7. Include the expected output in a comment.
"""

print()

numbers = (10, 20, 30, 20, 40, 50, 10)

visited = []

for number in numbers:
    if number in visited:
        break
    else:
        visited.append(number)

print(f"The first repeated element is {number}")

"""
Output:
The first repeated element is 20
"""

# ============================================

## New concept: Tuple Packing and Unpacking

"""
Tuple Packing
- Packing means grouping multiple values into a single tuple.
- Parentheses are optional when commas separate the values.
- Example: person = "Asha", 22, "Developer"

Tuple Unpacking
- Unpacking assigns tuple elements to separate variables.
- Values are assigned in their original order.
- Without starred unpacking, the number of variables must match the number of tuple elements.
- Example: name, age, role = person
"""

# -----------------

"""
🧩 Problem 31 — Employee Tuple Packing and Unpacking

Problem statement:
Write a Python program that performs the following tasks:
1. Create a tuple named employee using tuple packing, without explicitly writing parentheses around the values.
2. Store these three values in the tuple, in order:
   - Name: "Muskan"
   - Age: 25
   - Designation: "Full Stack Engineer"
3. Use tuple unpacking to assign the three tuple elements to separate variables named name, age, and designation.
4. Print each variable using an f-string.
Expected output
Employee Name: Muskan
Employee Age: 25
Employee Designation: Full Stack Engineer

Your rules:
- Use tuple packing without explicit parentheses when creating employee.
- Use tuple unpacking rather than indexing to retrieve the values.
- Use f-strings for the output.
"""
print()

employee = "Muskan", 25, "Full Stack Engineer"    # Packing

name, age, designation = employee                 # Unpacking

print(f"Employee Name: {name}")
print(f"Employee Age: {age}")
print(f"Employee Designation: {designation}")

"""
Output:
Employee Name: Muskan
Employee Age: 25
Employee Designation: Full Stack Engineer
"""

# ==========================================

"""
Problem 32 — Unpacking Values from a Tuple

Problem statement:
Create a tuple named product containing these values, in order:
- Product name: "Laptop"
- Price: 55000
- Quantity: 2
- Category: "Electronics"
Then:
1. Use tuple unpacking to assign the values to product_name, price, quantity, and category.
2. Calculate the total cost using price * quantity.
3. Print all four unpacked values and the total cost using f-strings.
Expected output
Product Name: Laptop
Price: 55000
Quantity: 2
Category: Electronics
Total Cost: 110000

Rules:
- Use tuple packing without explicitly writing parentheses around the values.
- Use tuple unpacking, not indexing.
- Use an expression to calculate the total cost.
- Do not hardcode the total cost.
"""

print()

product = "Laptop", 55000, 2, "Electronics"

product_name, price, quantity, category = product

total_cost = price * quantity

print(f"Product Name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Category: {category}")
print(f"Total Cost: {total_cost}")

"""
Output:
Product Name: Laptop
Price: 55000
Quantity: 2
Category: Electronics
Total Cost: 110000
"""

# =====================================

"""
Problem 33 — Packing and Unpacking with Multiple Data Types

Problem statement:
Create a tuple named student containing these values, in order:
- Name: "Riya"
- Age: 21
- Percentage: 87.5
- Passed: True
Then:
1. Use tuple packing without explicitly writing parentheses.
2. Unpack the tuple into name, age, percentage, and passed.
3. Print all four values using f-strings.
4. Print the data type of each unpacked variable using type().
Expected output
Student Name: Riya
Student Age: 21
Student Percentage: 87.5
Passed: True
Type of name: <class 'str'>
Type of age: <class 'int'>
Type of percentage: <class 'float'>
Type of passed: <class 'bool'>

Rules: Use tuple unpacking, don't use indexing, and don't hardcode the data types in the output.
"""

print()

student = "Riya", 21, 87.5, True

student_name, student_age, student_percentage, passed = student

print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Student Percentage: {student_percentage}")
print(f"Passed: {passed}")
print(f"Type of name: {type(student_name)}")
print(f"Type of age: {type(student_age)}")
print(f"Type of percentage: {type(student_percentage)}")
print(f"Type of passed: {type(passed)}")

"""
Output:
Student Name: Riya
Student Age: 21
Student Percentage: 87.5
Passed: True
Type of name: <class 'str'>
Type of age: <class 'int'>
Type of percentage: <class 'float'>
Type of passed: <class 'bool'>
"""

# ==================================

# Starred Tuple Unpacking

"""
- Starred unpacking uses * to collect multiple values into one variable.
- The starred variable receives a list, not a tuple.
- It can appear at the beginning, middle, or end of an unpacking assignment.
- Only one starred target is allowed at the same unpacking level.
- Regular variables receive individual values; the starred variable collects the remaining values after
 accounting for those regular variables.

Examples
first, *remaining = (10, 20, 30, 40)
# first = 10
# remaining = [20, 30, 40]

*remaining, last = (10, 20, 30, 40)
# remaining = [10, 20, 30]
# last = 40

first, *middle, last = (10, 20, 30, 40, 50)
# first = 10
# middle = [20, 30, 40]
# last = 50
"""

# ========================================= #

"""
Problem 34 — Starred Tuple Unpacking

Problem statement:
Write a Python program that:
1. Creates a tuple named scores containing these values, in order: 85, 90, 78, 92, 88, 95, 80.
2. Uses starred unpacking to assign:
   - The first score to first_score.
   - All middle scores to middle_scores.
   - The last score to last_score.
3. Prints all three variables using f-strings.
4. Prints the data type of middle_scores using type().
Expected output
First Score: 85
Middle Scores: [90, 78, 92, 88, 95]
Last Score: 80
Type of middle_scores: <class 'list'>

Your rules:
- Create the tuple without explicitly writing parentheses around the values.
- Use starred unpacking; do not use indexing or slicing to extract the values.
- Calculate nothing extra and don't hardcode the output.
- Use f-strings for every printed line.
"""

print()

scores = 85, 90, 78, 92, 88, 95, 80

first_score, *middle_scores, last_score = scores

print(f"First Score: {first_score}")
print(f"Middle Scores: {middle_scores}")
print(f"Last Score: {last_score}")
print(f"Type of middle_scores: {type(middle_scores)}")

"""
Output:
First Score: 85
Middle Scores: [90, 78, 92, 88, 95]
Last Score: 80
Type of middle_scores: <class 'list'>
"""

# ====================================

"""
Problem 35 — Starred Unpacking at the Beginning
Let's practise placing the * at a different position.
Problem statement:
Create a tuple named temperatures containing these values, in order:
28, 30, 27, 32, 29, 31
Then:
1. Use starred unpacking to assign all values except the last one to previous_temperatures.
2. Assign the last value to latest_temperature.
3. Print both variables using f-strings.
4. Print the data type of previous_temperatures using type().
Expected output
Previous Temperatures: [28, 30, 27, 32, 29]
Latest Temperature: 31
Type of previous_temperatures: <class 'list'>


Rules:
- Create the tuple without explicitly writing parentheses around its values.
- Use starred unpacking, not indexing or slicing.
- Use f-strings for every printed line.
- Don't hardcode the output.
"""

print()

temperatures = 28, 30, 27, 32, 29, 31

*previous_temperatures, latest_temperature = temperatures

print(f"Previous Temperatures: {previous_temperatures}")
print(f"Latest Temperature: {latest_temperature}")
print(f"Type of previous_temperatures: {type(previous_temperatures)}")

"""
Output:
Previous Temperatures: [28, 30, 27, 32, 29]
Latest Temperature: 31
Type of previous_temperatures: <class 'list'>
"""

# ==================================================

"""
Problem 36 — Starred Unpacking at the End
One more practice problem will help reinforce the final position of *.
Problem statement:
Create a tuple named daily_sales containing these values, in order:
1200, 1500, 1350, 1800, 1650, 2000
Then:
1. Assign the first value to first_day_sales.
2. Collect all remaining values into remaining_sales using starred unpacking.
3. Print both variables using f-strings.
4. Print the data type of remaining_sales using type().
Expected output
First Day Sales: 1200
Remaining Sales: [1500, 1350, 1800, 1650, 2000]
Type of remaining_sales: <class 'list'>

Rules:
- Create the tuple without explicitly writing parentheses around its values.
- Use starred unpacking, not indexing or slicing.
- Use f-strings for every printed line.
- Don't hardcode the output.
"""
print()

daily_sales = 1200, 1500, 1350, 1800, 1650, 2000

first_day_sales, *remaining_sales = daily_sales

print(f"First Day Sales: {first_day_sales}")
print(f"Remaining Sales: {remaining_sales}")
print(f"Type of remaining_sales: {type(remaining_sales)}")

"""
Output:
First Day Sales: 1200
Remaining Sales: [1500, 1350, 1800, 1650, 2000]
Type of remaining_sales: <class 'list'>
"""

# Remember: the starred variable receives a list, even when the original collection is a tuple.

# ================================================

# 📘 Swapping Variables Using Tuple Unpacking

"""
- Swapping means exchanging values between variables.
- Python supports swapping using tuple packing and unpacking.
- Syntax: a, b = b, a
- Python evaluates the right-hand side before assigning the new values to the left-hand variables.
- This technique works with more than two variables as well, provided the assignment has matching numbers of values and targets.
Example:
a, b, c = 10, 20, 30

a, b, c = c, a, b

# a = 30
# b = 10
# c = 20
"""

# ==========================================

"""
Problem 37 — Swap Two Values

Write a Python program that:
1. Creates two variables: first_number = 100 and second_number = 250.
2. Prints both variables before swapping.
3. Swaps their values using tuple unpacking, without a temporary variable.
4. Prints both variables after swapping.
Expected output
Before swapping:
First number: 100
Second number: 250

After swapping:
First number: 250
Second number: 100

Rules:
- Use first_number, second_number = second_number, first_number to swap.
- Use f-strings for the variable values.
- Don't hardcode the values in the output.
"""

print()

first_number = 100
second_number = 250

print("Before swapping:")
print(f"First number: {first_number}")
print(f"Second number: {second_number}")

print()

first_number, second_number = second_number, first_number

print("After swapping:")
print(f"First number: {first_number}")
print(f"Second number: {second_number}")

"""
Output:
Before swapping:
First number: 100
Second number: 250

After swapping:
First number: 250
Second number: 100
"""

"""
NOTE:
Python evaluates the right-hand side first, so it captures the original values 250 and 100.
It then assigns them to the left-hand variables in order.
"""

# =========================================

"""
Problem 38 — Swap Three Values
Let's strengthen the swapping concept with three variables.
Problem statement:
Write a Python program that:
1. Creates three variables:
   - a = 10
   - b = 20
   - c = 30
2. Prints all three variables before swapping.
3. Performs this assignment:
   a, b, c = c, a, b
4. Prints all three variables after swapping.
Expected output
Before swapping:
a: 10
b: 20
c: 30

After swapping:
a: 30
b: 10
c: 20

Rules:
- Use tuple unpacking to swap the values.
- Don't use a temporary variable.
- Use f-strings for the variable values.
- Don't hardcode the values in your output.
"""

print()

a = 10
b = 20
c = 30

print("Before swapping:")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print()

a, b, c = c, a, b

print("After swapping:")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

"""
Output:
Before swapping:
a: 10
b: 20
c: 30

After swapping:
a: 30
b: 10
c: 20
"""

# =========================================

# Tuple Concatenation and Tuple Repetition

"""
Tuple Concatenation
- Concatenation joins tuples using +.
- It creates a new tuple.
- The original tuples remain unchanged.
- Element order is preserved.
- Both operands must be compatible sequence types; for tuple concatenation, use tuples on both sides.

a = (10, 20)
b = (30, 40)
result = a + b

# result = (10, 20, 30, 40)

# ---------------------------

Tuple Repetition
- Repetition uses * with an integer.
- It repeats the tuple's elements the specified number of times.
- Multiplying by zero or a negative integer produces an empty tuple.
- The original tuple remains unchanged.

numbers = (5, 10)
result = numbers * 3

# result = (5, 10, 5, 10, 5, 10)
"""

# =======================================

"""
Problem 39 — Tuple Concatenation and Repetition

Problem statement - Write a Python program that performs these tasks:
1. Create a tuple named morning_tasks containing
 "Exercise", "Reading", and "Python Practice", without explicitly writing parentheses around the values.
2. Create another tuple named evening_tasks containing "Job Search" and "Project Work",
 also without explicitly writing parentheses around the values.
3. Concatenate both tuples into a new tuple named daily_tasks.
4. Repeat daily_tasks twice and store the result in repeated_tasks.
5. Print all four tuples using f-strings.
6. Print the data types of daily_tasks and repeated_tasks using type().
Expected output
Morning Tasks: ('Exercise', 'Reading', 'Python Practice')
Evening Tasks: ('Job Search', 'Project Work')
Daily Tasks: ('Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work')
Repeated Tasks: ('Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work', 'Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work')
Type of daily_tasks: <class 'tuple'>
Type of repeated_tasks: <class 'tuple'>

Rules:
- Create both original tuples without explicit parentheses.
- Use + for concatenation and * for repetition.
- Don't hardcode the output.
- Use f-strings for every printed line.
"""

print()

morning_tasks = "Exercise", "Reading", "Python Practice"

evening_tasks = "Job Search", "Project Work"

daily_tasks = morning_tasks + evening_tasks

repeated_tasks = daily_tasks * 2

print(f"Morning Tasks: {morning_tasks}")
print(f"Evening Tasks: {evening_tasks}")
print(f"Daily Tasks: {daily_tasks}")
print(f"Repeated Tasks: {repeated_tasks}")
print(f"Type of daily_tasks: {type(daily_tasks)}")
print(f"Type of repeated_tasks: {type(repeated_tasks)}")

"""
Output:
Morning Tasks: ('Exercise', 'Reading', 'Python Practice')
Evening Tasks: ('Job Search', 'Project Work')
Daily Tasks: ('Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work')
Repeated Tasks: ('Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work', 'Exercise', 'Reading', 'Python Practice', 'Job Search', 'Project Work')
Type of daily_tasks: <class 'tuple'>
Type of repeated_tasks: <class 'tuple'>
"""

# ========================================

## Converting Other Data Types into Tuples

"""
The tuple() Function
- Converts an iterable into a tuple.
- tuple(list) converts a list into a tuple.
- tuple(string) creates a tuple of individual characters.
- tuple(range(...)) converts the generated numbers into a tuple.
- tuple() creates an empty tuple.
- The order of elements is preserved.
"""

# ---------------------------------------- #

"""
Problem 40 — Convert a List into a Tuple
Write a Python program that:
1. Creates a list named subjects containing "Python", "SQL", "DSA", and "Django".
2. Converts the list into a tuple named subject_tuple using tuple().
3. Prints the original list.
4. Prints the new tuple.
5. Prints the data type of both variables using type().
Expected output
Original List: ['Python', 'SQL', 'DSA', 'Django']
Converted Tuple: ('Python', 'SQL', 'DSA', 'Django')
Type of subjects: <class 'list'>
Type of subject_tuple: <class 'tuple'>

Rules: Use tuple() for conversion, don't hardcode the output, and use f-strings for every printed line.
"""

print()

subjects = ["Python", "SQL", "DSA", "Django"]

subject_tuple = tuple(subjects)

print(f"Original List: {subjects}")
print(f"Converted Tuple: {subject_tuple}")
print(f"Type of subjects: {type(subjects)}")
print(f"Type of subject_tuple: {type(subject_tuple)}")

"""
Output:
Original List: ['Python', 'SQL', 'DSA', 'Django']
Converted Tuple: ('Python', 'SQL', 'DSA', 'Django')
Type of subjects: <class 'list'>
Type of subject_tuple: <class 'tuple'>
"""

# ========================================

# Nested Tuples

"""
- A nested tuple contains other tuples as elements.
- Use one index to access an inner tuple.
- Use two indices to access a value inside an inner tuple.
- Nested loops can traverse all values in a nested tuple.

data = (("A", 10), ("B", 20))

# data[0]     -> ("A", 10)
# data[0][0]  -> "A"
# data[0][1]  -> 10
"""

# =================================

"""
Problem 41 — Accessing Values in a Nested Tuple

Create a nested tuple named students containing:
- ("Riya", 85)
- ("Aarav", 92)
- ("Neha", 78)
Then:
1. Print the first student's name.
2. Print the second student's marks.
3. Print the third student's name.
4. Print the first student's complete tuple.
5. Use f-strings for every printed line.
Expected output
First Student Name: Riya
Second Student Marks: 92
Third Student Name: Neha
First Student Record: ('Riya', 85)

Rules:
- Create the nested tuple directly.
- Use indexing to access the requested values.
- Don't hardcode the output.
- Use f-strings for every printed line.
"""

print()

students = (
    ("Riya", 85),
    ("Aarav", 92),
    ("Neha", 78)
)

print(f"First Student Name: {students[0][0]}")
print(f"Second Student Marks: {students[1][1]}")
print(f"Third Student Name: {students[2][0]}")
print(f"First Student Record: {students[0]}")

"""
Output:
First Student Name: Riya
Second Student Marks: 92
Third Student Name: Neha
First Student Record: ('Riya', 85)
"""

# ==============================================

# Traversing a Nested Tuple

"""
A nested loop is a loop inside another loop.
The outer loop selects each inner collection.
The inner loop processes the values within that collection.
"""

# ============================

"""
Problem 42 — Traversing a Nested Tuple

Create the following nested tuple:
employees = (    
    ("Amit", "Sales", 25000),
    ("Priya", "IT", 35000),    
    ("Rahul", "HR", 30000)
)

Using nested for loops, print every value in every employee record, one value per line.
Requirements:
- Use nested for loops.
- Do not access values using manual indexing.
- Use an f-string for each printed line, with the label Employee Detail:.
- Do not hardcode the output.

Expected output:
Employee Detail: Amit
Employee Detail: Sales
Employee Detail: 25000
Employee Detail: Priya
Employee Detail: IT
Employee Detail: 35000
Employee Detail: Rahul
Employee Detail: HR
Employee Detail: 30000
"""

print()

employees = (    
    ("Amit", "Sales", 25000),
    ("Priya", "IT", 35000),    
    ("Rahul", "HR", 30000)
)

for employee in employees:                
    for value in employee:                  
        print(f"Employee Detail: {value}")

"""
Output:
Employee Detail: Amit
Employee Detail: Sales
Employee Detail: 25000
Employee Detail: Priya
Employee Detail: IT
Employee Detail: 35000
Employee Detail: Rahul
Employee Detail: HR
Employee Detail: 30000
"""

# =========================================

# Mixed tuple revision

"""
Problem 43
Analyze a tuple of numbers
Create the following tuple:
numbers = (12, 25, 8, 25, 40, 12, 7, 30)

Write a program that does all of the following:
1. Print the total number of elements in the tuple.
2. Print the first three elements as a tuple.
3. Print the tuple in reverse order.
4. Count how many times 25 appears.
5. Print all the even numbers, one per line.
6. Print the number of elements greater than 20.
Requirements
- Use the original tuple; don't change it.
- Use f-strings for all output lines.
- Don't hardcode calculated answers.
- For the even numbers, print each number with the label Even Number:.
"""

print()

numbers = (12, 25, 8, 25, 40, 12, 7, 30)

# 1. Print the total number of elements in the tuple.

print(f"Total Elements: {len(numbers)}")

# Another way without len()

total = 0

for number in numbers:
    total += 1

print(f"Total Elements: {total}")

# ---------

# 2. Print the first three elements as a tuple.

print(f"First Three Elements: {numbers[0:3]}")

# ---------

# 3. Print the tuple in reverse order.

print(f"Reversed Tuple: {numbers[-1::-1]}")

# ---------

# 4. Count how many times 25 appears.

count = 0

for number in numbers:
    if number == 25:
        count += 1

print(f"Occurrences of 25: {count}")

# ------------

# 5. Print all the even numbers, one per line.

for number in numbers:
    if number % 2 == 0:
        print(f"Even Number: {number}")

# -----------

# 6. Print the number of elements greater than 20.

greater = 0

for number in numbers:
    if number > 20:
        greater += 1

print(f"Elements Greater Than 20: {greater}")

# ---------------

"""
Final Output of all:
Total Elements: 8
Total Elements: 8
First Three Elements: (12, 25, 8)
Reversed Tuple: (30, 7, 12, 40, 25, 8, 25, 12)
Occurrences of 25: 2
Even Number: 12
Even Number: 8
Even Number: 40
Even Number: 12
Even Number: 30
Elements Greater Than 20: 4
"""

# ========================================

"""
Problem 44 — Mixed tuple revision
Analyze and filter a tuple
Create this tuple:
scores = (45, 72, 90, 45, 68, 100, 72, 35)

Write a program that:
1. Prints the number of elements in the tuple.
2. Prints the last four elements as a tuple.
3. Counts how many times 72 appears, using a loop rather than .count().
4. Prints all scores greater than or equal to 70, one per line.
5. Counts how many scores are below 50.
6. Prints the highest score without using max() or sorted().
Requirements
- Keep the original tuple unchanged.
- Use f-strings for every output line.
- Do not hardcode calculated answers.
- For filtered scores, use the label Qualifying Score:.
"""

print()

scores = (45, 72, 90, 45, 68, 100, 72, 35)

# 1. Prints the number of elements in the tuple.

print(f"Total Scores: {len(scores)}")

# -----------

# 2. Prints the last four elements as a tuple.

print(f"Last Four Scores: {scores[-4:]}")

# -----------

# 3. Counts how many times 72 appears, using a loop rather than .count().

count = 0

for score in scores:
    if score == 72:
        count += 1

print(f"Occurrences of 72: {count}")

# -------------

# 4. Prints all scores greater than or equal to 70, one per line.

for score in scores:
    if score >= 70:
        print(f"Qualifying Score: {score}")

# ----------------

# 5. Counts how many scores are below 50.

count = 0

for score in scores:
    if score < 50:
        count += 1

print(f"Scores Below 50: {count}")

# --------------------

# 6. Prints the highest score without using max() or sorted().

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print(f"Highest Score: {highest}")

# --------------

"""
Final Output of all:
Total Scores: 8
Last Four Scores: (68, 100, 72, 35)
Occurrences of 72: 2
Qualifying Score: 72
Qualifying Score: 90
Qualifying Score: 100
Qualifying Score: 72
Scores Below 50: 3
Highest Score: 100
"""

# ==================================

# Edge cases

"""
Problem 45 — Search for a missing element
Create this tuple:
numbers = (10, 20, 30, 40, 50)

Write a program that:
1. Searches for the number 35.
2. If 35 exists, print Number Found: 35.
3. Otherwise, print Number Not Found: 35.
Requirements
- Use a for loop.
- Do not use the in operator for the search.
- Use a Boolean variable to track whether the number was found.
- Use an f-string for the output.
- Do not hardcode the search result.
"""

print()

numbers = (10, 20, 30, 40, 50)

found = False

# Check the final result after searching:

for number in numbers:
    if number == 35:
        found = True     
    
if found:
    print(f"Number Found: 35")
else:
    print(f"Number Not Found: 35")

"""
Output:
Number Not Found: 35
"""

# ==============================================