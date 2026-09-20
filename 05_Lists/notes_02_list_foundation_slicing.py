# ==========================================================

# List Problems

"""
🟢 List Problem 1 — Creating a List

Create a Python list called fruits containing these three values:

Apple
Banana
Mango

Then print the list.
"""
print()

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

"""
Output:
['Apple', 'Banana', 'Mango']
"""

# ================================

"""
🟢 List Problem 2 — Creating Different Lists

Create three lists:

numbers containing 10, 20, 30, 40
names containing "Muskan", "Rahul", "Priya"
empty_list containing nothing

Then print all three lists.
"""

print()

numbers = [10, 20, 30, 40]
names = ["Muskan", "Rahul", "Priya"]
empty_list = []

print(numbers)
print(names)
print(empty_list)

"""
Output:
[10, 20, 30, 40]
['Muskan', 'Rahul', 'Priya']
[]
"""

# =======================================

"""
🟢 List Problem 3 — Different Data Types

Now let's check an important List property.

Create a list called data containing:

"Python" → string
24 → integer
5.5 → float
True → boolean

Then print:

The complete list
The type of the list using type()
"""

print()

diff_data = ["Python", 24, 5.5, True]

print(diff_data, type(diff_data))   

"""
Output:
['Python', 24, 5.5, True] <class 'list'>
"""

# =======================================

"""
🟢 List Problem 4 — len()

Now we're moving to the next foundation concept: finding how many elements are in a list.

Create:

numbers = [10, 20, 30, 40, 50]

Then print the number of elements in the list using len().

Expected output
5
"""
print()

numbers = [10, 20, 30, 40, 50]

print(f"The length is {len(numbers)}")  # Output: The length is 5

# =======================

"""
🟢 List Problem 5 — Positive Indexing

Now let's access individual elements.

Create:

languages = ["Python", "Java", "C++", "JavaScript"]

Print:

The first element
The second element
The last element
Expected output
Python
Java
JavaScript

Use positive indexing only for this problem.
"""

print()

languages = ["Python", "Java", "C++", "JavaScript"]

print(f"The first element is {languages[0]}")
print(f"The second element is {languages[1]}")
print(f"The last element is {languages[3]}")

"""
Output:
The first element is Python
The second element is Java
The last element is JavaScript
"""

# =============================================

"""
🟢 List Problem 6 — Negative Indexing

Now let's make the connection with the negative indexing you already learned with Strings.

Create:

languages = ["Python", "Java", "C++", "JavaScript"]

Print:

The last element using negative indexing
The second-last element using negative indexing
The third-last element using negative indexing
Expected output
JavaScript
C++
Java

Use negative indexing only for this problem.
"""
print()

languages = ["Python", "Java", "C++", "JavaScript"]

print(f"The last element is {languages[-1]}")
print(f"The second last element is {languages[-2]}")
print(f"The third last element is {languages[-3]}")

"""
Output:
The last element is JavaScript
The second last element is C++
The third last element is Java
"""

# =========================================

"""
🟢 List Problem 7 — in and not in

Create:

languages = ["Python", "Java", "C++", "JavaScript"]

Then check:

Is "Python" present in the list?
Is "PHP" present in the list?
Is "Ruby" not present in the list?

Use:

in
not in

and print the results.
"""
print()

languages = ["Python", "Java", "C++", "JavaScript"]

print("Python" in languages)               # Output: True
print("PHP" in languages)                  # Output: False 
print("Ruby" not in languages)             # Output: True


# ==========================================

"""
🟢 List Problem 8 — Basic Slicing

Create:

numbers = [10, 20, 30, 40, 50]

Print the elements from index 1 up to index 4.

Remember:

Start is included, end is excluded.
"""

print()

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

"""
Output:
[20, 30, 40]
"""

# =====================================

"""
🟢 List Problem 9 — Omitted Start

Using:

numbers = [10, 20, 30, 40, 50]

Print everything from the beginning up to index 3.
"""
print()

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

"""
Output:
[10, 20, 30]
"""

# ================================

"""
🟢 List Problem 10 — Omitted End

Using:

numbers = [10, 20, 30, 40, 50]

Print everything from index 2 to the end of the list.
"""

print()

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])

"""
Output:
[30, 40, 50]
"""

# ====================================

"""
🟢 List Problem 11 — Slicing with Step

Using:

numbers = [10, 20, 30, 40, 50, 60]

Print every second element, starting from the beginning.
"""
print()

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])

"""
Output:
[10, 30, 50]
"""

# =====================================

"""
🟢 List Problem 12 — Reverse a List Using Slicing

Using:

numbers = [10, 20, 30, 40, 50]

Print the list in reverse order using slicing.

Expected output:

[50, 40, 30, 20, 10]
"""
print()

numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])

"""
Output:
[50, 40, 30, 20, 10]
"""

# ===================================

"""
🟢 List Problem 13 — Modifying a List

Create:

numbers = [10, 20, 30, 40, 50]

Change the third element from 30 to 99.

Then print the updated list.

Expected output
[10, 20, 99, 40, 50]
"""
print()

numbers = [10, 20, 30, 40, 50]

numbers[2] = 99
print(numbers)

"""
Output:
[10, 20, 99, 40, 50]
"""
# Note: Lists are mutable, meaning we can directly change their elements after the list has been created.

# ===============================

"""
🟢 List Problem 14 — Modify Multiple Elements

Create:

numbers = [10, 20, 30, 40, 50]

Now:

Change 20 to 200
Change 50 to 500
Print the updated list.
Expected output
[10, 200, 30, 40, 500]

💡 Use index-based modification again.
"""
print()

numbers = [10, 20, 30, 40, 50]
numbers[1] = 200
numbers[4] = 500
print(numbers)

"""
Output:
[10, 200, 30, 40, 500]
"""

# =====================================

"""
🟢 List Problem 15 — Modify Using Slicing

Now let's take the next step. 😎

Create:

numbers = [10, 20, 30, 40, 50]

Change the second and third elements to:

200, 300

using slicing, not individual indexes.

Expected output
[10, 200, 300, 40, 50]

💡 Hint: You need to replace a slice containing two elements.
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [200, 300]
print(numbers)

"""
Output:
[10, 200, 300, 40, 50]
"""

# =================================

"""
🟢 List Problem 16 — Mutability Check

Now let's make sure you understand what mutability actually means, rather than only knowing the syntax.

Create:

numbers = [10, 20, 30]

Then:

Change the first element to 100.
Print numbers.
Print len(numbers).
Expected output
[100, 20, 30]
3
"""

print()

numbers = [10, 20, 30]

numbers[0] = 100
print(numbers)                  # Output: [100, 20, 30]
print(len(numbers))             # Output: 3

# =====================================