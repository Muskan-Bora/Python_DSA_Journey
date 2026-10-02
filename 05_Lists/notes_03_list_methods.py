## ================================== ##

# List - Methods

"""
🐍 PYTHON LIST METHODS

A list method is a function that belongs to a list object.

We call a list method using dot notation:

    list_name.method()

Example:

    numbers.append(40)


Main List Methods:

1. Adding Elements
   - append()  → adds one element at the end
   - insert()  → adds one element at a specific index
   - extend()  → adds multiple elements

2. Removing Elements
   - remove()  → removes an element by value
   - pop()     → removes an element by index
   - clear()   → removes all elements

3. Searching / Counting
   - index()   → finds the index of a value
   - count()   → counts how many times a value appears

4. Ordering
   - sort()    → sorts the original list
   - reverse() → reverses the original list

Important:
We will learn each method through:
    What → How → When to use → Difference → Practice
"""

# ======================================

"""
🟢 List Problem 17 — append()
First understand the purpose

append() is used when you want to:

Add ONE new element to the end of a list.

For example, conceptually:

[10, 20, 30]
       ↓ append 40
[10, 20, 30, 40]
Your task

Create:

numbers = [10, 20, 30]

Add 40 to the end of the list using the appropriate list method.

Then print the list.
"""

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)   

"""
Output:
[10, 20, 30, 40]
"""

"""
🧠 What you've learned

append():

Adds one element ✅
Adds it to the end of the list ✅
Changes the original list ✅
Increases the list length by 1 ✅

So:

Before → [10, 20, 30]
After  → [10, 20, 30, 40]
"""

# ====================================

"""
🟢 List Problem 18 — append() with Different Data Types

Now let's make sure you understand that append() can add different types of values, not just numbers.

Create:

items = ["Python", 24, True]

Then use append() to add:

5.5

Print the updated list.

Expected output
["Python", 24, True, 5.5]
"""

print()

items = ["Python", 24, True]

items.append(5.5)

print(items)

"""
Output:
['Python', 24, True, 5.5]
"""

# =============================================

"""
🟢 List Problem 19 — append() and List Length

Now let's connect append() with something you already learned: len().

Create:

numbers = [10, 20, 30]

Then:

Print the length of the list.
Use append() to add 40.
Print the length again.
Print the final list.
Expected output
3
4
[10, 20, 30, 40]
"""

print()

numbers = [10, 20, 30]

print(numbers)           # Output of original list elements [10, 20, 30]

print(len(numbers))      # Length is 3 before append 

numbers.append(40)       # Added the new element in the list

print(len(numbers))      # Length is 4 after new element got added

print(numbers)           # Output after new element added - [10, 20, 30, 40]

# ===============================

"""
🟢 List Problem 20 — append() vs Adding Multiple Values

Now we're going to learn something very important about append().

Create:

numbers = [10, 20, 30]

Use one append() call to add these two values:

40, 50

Then print the list.

Expected output
[10, 20, 30, [40, 50]]
"""

print()

numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)

"""
Output:
[10, 20, 30, [40, 50]]
"""

# ==============================

"""
🟢 List Problem 21 — extend()

Create:

numbers = [10, 20, 30]

Use extend() to add:

40, 50

Then print the list.

Expected output
[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)

"""
Output:
[10, 20, 30, 40, 50]
"""

# =======================================

"""
🟢 List Problem 22 — extend() with Different Data Types

Now let's make sure extend() isn't limited to numbers.

Create:

items = ["Python", 24]

Use extend() to add these three elements:

"Java", 5.5, True

Then print the final list.

Expected output
["Python", 24, "Java", 5.5, True]
"""

print()

items = ["Python", 24]

items.extend(["Java", 5.5, True])

print(items)

"""
Output:
['Python', 24, 'Java', 5.5, True]
"""

# =============================================

"""
🟢 List Problem 23 — append() vs extend()

Now we're going to test whether you can choose the correct method, rather than just reproduce syntax.

Start with:

numbers = [10, 20, 30]

You want the final list to be:

[10, 20, 30, 40, 50]
Your task

Add 40 and 50 to the end of the list.

You must use one method call.

The important part: decide yourself whether append() or extend() is appropriate.

Then print the final list.
"""

print()

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)          

"""
Output:
[10, 20, 30, 40, 50]
"""

# ========================================

"""
🟢 List Problem 24 — append() vs extend() — Your Decision

Now let's reverse the situation.

Start with:

items = ["Python", "Java"]

You want the final list to be:

["Python", "Java", ["C++", "JavaScript"]]
Your task

Add ["C++", "JavaScript"] as ONE element at the end of the list.
"""

print()

items = ["Python", "Java"]

items.append(["C++", "JavaScript"])
print(items)

"""
Output:
['Python', 'Java', ['C++', 'JavaScript']]
"""

# ====================================

"""
🟢 List Problem 25 — Basic insert()

Create:

numbers = [10, 20, 40, 50]

Insert 30 at index 2.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)   # Output: [10, 20, 30, 40, 50]

# ==========================================

"""
🟢 Problem 26 — insert() at the Beginning

Create:

numbers = [20, 30, 40, 50]

Insert 10 at the beginning of the list.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [20, 30, 40, 50]

numbers.insert(0, 10)
print(numbers)    # Output: [10, 20, 30, 40, 50]

# ==========================================

"""
List Problem 27 — insert() in the Middle

Create:

numbers = [10, 20, 40, 50]

Insert 30 between 20 and 40.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)      # Output: [10, 20, 30, 40, 50]

# ===================================

"""
🟢 List Problem 28 — append() vs insert()

Start with:

numbers = [10, 20, 30]

You need to add 40 at the end of the list.

Question: Should you use append() or insert()?
"""

print()

numbers = [10, 20, 30]

numbers.append(40)    # used append() because the question said You need to add 40 at the end of the list. so it means at the end 

print(numbers)  # Output: [10, 20, 30, 40]

# ==================================

"""
🟢 List Problem 29 — insert() vs append()

Start with:

items = ["Python", "Java", "C++"]

You need to add "JavaScript" between "Java" and "C++".

Question: Should you use append() or insert()?
"""

print()

items = ["Python", "Java", "C++"]

items.insert(2, "JavaScript")     # Here insert() used becaus ethe requirement was the elemnet should be add between "Java" and "C++" means its specified its position.

print(items)          # output: ['Python', 'Java', 'JavaScript', 'C++']

# ======================================

"""
🟢 List Problem 30 — insert() Understanding

Start with:

numbers = [10, 20, 30, 40]

You want the final list to be:

[10, 20, 25, 30, 40]

Your task: Use insert() to add 25 in the correct position.
"""

print()

numbers = [10, 20, 30, 40]

numbers.insert(2, 25)

print(numbers)      # Output: [10, 20, 25, 30, 40]

# =======================================

"""
🟢 List Problem 31 — remove() Basics

Start with:

numbers = [10, 20, 30, 40, 50]

Remove the value 30 from the list.

Expected output:

[10, 20, 40, 50]
Your task:

Use the appropriate list method to remove 30.
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
print(numbers)    # Output: [10, 20, 40, 50]

# ===============================================

"""
🟢 List Problem 32 — remove() with Duplicate Values

Start with:

numbers = [10, 20, 30, 20, 40]

Remove the value 20 once.

Expected output:

[10, 30, 20, 40]
Your task

Use remove() and think carefully about what happens when a value appears more than once.
"""

print()

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)
print(numbers)       # Output: [10, 30, 20, 40] --> It reove the 1st 20 from the list

# ===============================

"""
🟢 List Problem 33 — remove() and a Missing Value

Start with:

numbers = [10, 20, 30, 40, 50]

Try to remove the value 100.

Your task

Write the code using remove().
"""

print()

# numbers = [10, 20, 30, 40, 50]
# numbers.remove(100)
# print(numbers)

"""
Error will come: 
ValueError: list.remove(x): x not in list
"""

# ===================================================

"""
🟢 List Problem 34 — remove() by Value

Let's correct the problem so it stays within today's learning scope.

Start with:

numbers = [10, 20, 30, 40, 50]

Remove the value 40 from the list.

Expected output:

[10, 20, 30, 50]
Your task

Use remove().
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.remove(40)
print(numbers)       # OUTPUT: [10, 20, 30, 50]

# ====================================

"""
🟢 List Problem 35 — remove() with Strings

Start with:

languages = ["Python", "Java", "C++", "JavaScript"]

Remove "Java" from the list.

Expected output:

["Python", "C++", "JavaScript"]
Your task

Use remove().
"""

print()

languages = ["Python", "Java", "C++", "JavaScript"]

languages.remove("Java")
print(languages)                    # Output: ['Python', 'C++', 'JavaScript']

# ====================================

"""
🟢 List Problem 36 — remove() + Duplicate Strings

Start with:

languages = ["Python", "Java", "C++", "Java", "JavaScript"]

Remove "Java" once.

Expected output:

["Python", "C++", "Java", "JavaScript"]
Your task

Use remove() and send me your code.
"""

print()

languages = ["Python", "Java", "C++", "Java", "JavaScript"]

languages.remove("Java")
print(languages)                  # ['Python', 'C++', 'Java', 'JavaScript']

# =======================================

"""
🟢 List Problem 37 — pop() Basics

Now we're learning something new, so don't worry about comparing it with remove() yet.

Start with:

numbers = [10, 20, 30, 40, 50]

Use pop() to remove the last element from the list.

Expected output:

[10, 20, 30, 40]
Your task

Use pop().
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.pop()
print(numbers)        # Output: [10, 20, 30, 40]

# ==================================

"""
🟢 List Problem 38 — pop() with an Index

Start with:

numbers = [10, 20, 30, 40, 50]

Use pop() to remove the element at index 2.

Expected output:

[10, 20, 40, 50]
Your task

Use pop() with the appropriate index.
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.pop(2)
print(numbers)       # Output: [10, 20, 40, 50]

# =============================================

"""
🟢 List Problem 39 — Store the Removed Value

Start with:

numbers = [10, 20, 30, 40, 50]

Use pop() to remove the last element, but this time store the removed value in a variable called removed_value.

Then print both:

Removed value: 50
Remaining list: [10, 20, 30, 40]
"""

print()

numbers = [10, 20, 30, 40, 50]

removed_value = numbers.pop()
print(f"Removed value: {removed_value}")             # Output: Removed value: 50 [Because last elemnet is 50 so its geot removed]
print(f"Remaining list: {numbers}")                   # Output: Remaining list: [10, 20, 30, 40]

# ============================================

"""
🟢 List Problem 40 — pop(index) + Store Removed Value

Now let's combine what you've learned.

Start with:

numbers = [10, 20, 30, 40, 50]

Use pop() to remove the element at index 2, and store the removed value in:

removed_value

Expected result:

Removed value: 30
Remaining list: [10, 20, 40, 50]
"""
print()

numbers = [10, 20, 30, 40, 50]

removed_value = numbers.pop(2)
print(f"Removed value: {removed_value}")          # OUTPUT: Removed value: 30
print(f"Remaining list: {numbers}")               # OUTPUT: Remaining list: [10, 20, 40, 50]

# ====================================

"""
🟢 List Problem 41 — pop() + Empty List

One more important behavior before we move forward.

Start with:

numbers = [10]

Use pop() to remove the only element.

Then print:

Removed value: 10
Remaining list: []
Your task

Use pop() and store the removed value in removed_value
"""

print()

numbers = [10]
removed_value = numbers.pop()
print(f"Removed value: {removed_value}")    # Output: Removed value: 10
print(f"Remaining list: {numbers}")         # Output: Remaining list: []


"""
🧠 One important concept 

If you call pop() on an empty list, Python will raise an:

IndexError: pop from empty list
"""

# ===============================

"""
🟢 List Problem 42 — clear() Basics

Now let's move to our next list method: clear().

Start with:

numbers = [10, 20, 30, 40, 50]

Remove all elements from the list using the appropriate list method.

Expected output:

[]
Your task

Use clear() and print the list afterward.
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.clear()
print(numbers)       # Output: [] -> The empty list came because we have used clear() since it removes all the elements

# The list still exists:

numbers = []

numbers.append(500)    
print(numbers)        # Output: [500] 

"""
So:

remove(value) → removes one matching value ✅
pop(index) → removes one element and returns it ✅
clear() → removes all elements ✅
"""

# ======================================

"""
🟢 List Problem 43 — clear() and Reuse

Start with:

numbers = [10, 20, 30]
Remove all elements using clear().
Then add 100 to the now-empty list using append().
Print the final list.

Expected output:

[100]
"""

print()

numbers = [10, 20, 30]

numbers.clear()   
print(numbers)         # Output: []

numbers.append(100)    # Here that empty list will get reused to add a new element

print(numbers)         # Output: [100]

# ====================================

"""
🟢 List Problem 44 — remove() + pop() + append()

Now we're going to combine methods, but nothing new.

Start with:

numbers = [10, 20, 30, 40, 50]

Perform these steps in order:

Remove the value 20 using remove().
Remove the element at index 2 using pop().
Add 100 at the end using append().
Print the final list.
Expected output
[10, 30, 50, 100]
"""

print()

numbers = [10, 20, 30, 40, 50]

# Remove the value 20 using remove().

numbers.remove(20)
print(numbers)             # Output: [10, 30, 40, 50]

# So, new list becomes
numbers = [10, 30, 40, 50]

# Remove the element at index 2 using pop().

numbers.pop(2)
print(numbers)             # Output: [10, 30, 50]

# So, now new list becomes
numbers = [10, 30, 50]

# Add 100 at the end using append().

numbers.append(100)
print(numbers)             # Output: [10, 30, 50, 100]

final_list = numbers
print(f"Final List: {numbers}")      # Output: Final List: [10, 30, 50, 100]

# ====================================

# Count()

"""
What does count() do?

It tells us how many times a particular value appears in a list.
"""

"""
🟢 Problem 45

Start with:

numbers = [10, 20, 20, 30, 20, 40]

Find how many times 20 appears in the list.

Expected output:

3
"""

print()

numbers = [10, 20, 20, 30, 20, 40]

print(numbers.count(20))    # Output: 3

# =====================

"""
🟢 List Problem 46 — count() with a Value That Doesn't Exist

Start with:

numbers = [10, 20, 20, 30, 20, 40]

Find how many times 100 appears in the list.

Expected output:

0
"""

print()

numbers = [10, 20, 20, 30, 20, 40]

print(numbers.count(100))     # Output: 0

# ==============================

"""
🟢 List Problem 47 — count() with Strings

Let's make sure the method isn't limited to numbers.

Start with:

languages = ["Python", "Java", "Python", "C++", "Python", "Java"]

Find how many times "Python" appears.

Expected output:

3
"""

print()

languages = ["Python", "Java", "Python", "C++", "Python", "Java"]

print(languages.count("Python"))       # Output: 3

# ==================================

"""
List Problem 48 — index()

Now we're moving to the next List Method: index().

Start with:

numbers = [10, 20, 30, 40, 50]

Find the index of 30.

Expected output:

2
"""

print()

numbers = [10, 20, 30, 40, 50]

print(numbers.index(30))    # Output: 2

"""
🧠 Key rule

index(value) → returns the index of the first occurrence of that value.
"""

# ==================================

"""
List Problem 49 — index() with Duplicate Values

Start with:

numbers = [10, 20, 30, 20, 40]

Find the index of 20.

Expected output:

1
"""

print()

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))         # Output: 1 --> Reason is the 1st 20 is coming in index position of 1 so its considering 1st 20

"""
index() returns the index of the first occurrence of the value.
"""

# ==============================

"""
List Problem 50 — index() with a Missing Value

Start with:

numbers = [10, 20, 30, 40, 50]

Try to find the index of 100.

Your task

Use:

index()

and run the code.
"""

# print()

# numbers = [10, 20, 30, 40, 50]

# print(numbers.index(100))

"""
print(numbers.index(100))
          ^^^^^^^^^^^^^^^^^^
ValueError: 100 is not in list
"""

"""
🧠 This gives us an important comparison
| Method          | If value exists                  | If value doesn't exist |
| --------------- | -------------------------------- | ---------------------- |
| `remove(value)` | Removes first occurrence         | `ValueError`           |
| `index(value)`  | Returns first occurrence's index | `ValueError`           |
| `count(value)`  | Returns occurrence count         | Returns `0`            |

"""

# ======================================

"""
List Problem 51 — index() + Duplicate Values

Let's make this a little more practical.

Start with:

numbers = [10, 20, 30, 20, 40, 20]

You need to find:

How many times 20 appears.
The index of the first 20.
Expected output
Count: 3
First index: 1
"""

print()

numbers = [10, 20, 30, 20, 40, 20]

print(f"Count: {numbers.count(20)}")
print(f"First Index: {numbers.index(20)}")

"""
Output:
Count: 3
First Index: 1
"""

# ==========================================

"""
🟢 List Problem 52 — sort() Basics

Now we move to ordering/sorting.

Start with:

numbers = [40, 10, 50, 20, 30]

Sort the list in ascending order.

Expected output:

[10, 20, 30, 40, 50]
"""

print()

numbers = [40, 10, 50, 20, 30]

numbers.sort()
print(numbers)       # Output: [10, 20, 30, 40, 50]

# ================================

"""
List Problem 53 — sort() with Strings

Start with:

languages = ["Python", "Java", "C", "JavaScript", "Go"]

Sort the list in ascending/alphabetical order.

Expected output:

['C', 'Go', 'Java', 'JavaScript', 'Python']
"""

print()

languages = ["Python", "Java", "C", "JavaScript", "Go"]

languages.sort()

print(languages)     # Output: ['C', 'Go', 'Java', 'JavaScript', 'Python']

# ===========================================

"""
List Problem 54 — reverse() Basics

Now let's learn the second ordering method.

Start with:

numbers = [10, 20, 30, 40, 50]

Reverse the original list using the appropriate list method.

Expected output:

[50, 40, 30, 20, 10]
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.reverse()
print(numbers)              # Output: [50, 40, 30, 20, 10]

"""
🧠 Important distinction

two ordering methods:

sort() → reorders elements according to ascending order by default.
reverse() → reverses the current order of the list.
"""

# ====================================

"""
🟢 List Problem 55 — sort() + reverse()

Now let's combine the two methods you've just learned.

Start with:

numbers = [40, 10, 50, 20, 30]

Sort the list in descending order.

Expected output:

[50, 40, 30, 20, 10]
"""

print()

numbers = [40, 10, 50, 20, 30]

numbers.sort()
numbers.reverse()
print(numbers)        # Output: [50, 40, 30, 20, 10]

# ====================================

"""
List Problem 56 — sort() with Duplicate Values

Start with:

numbers = [30, 10, 20, 30, 50, 20, 40]

Sort the list in ascending order.

Expected output:

[10, 20, 20, 30, 30, 40, 50]
"""

print()

numbers = [30, 10, 20, 30, 50, 20, 40]

numbers.sort()
print(numbers)          # Output: [10, 20, 20, 30, 30, 40, 50]

"""
🧠 Small concept confirmed

sort() does not remove duplicates. It only changes the order.
"""

# ===========================

"""
List Problem 57 — reverse() After sort()

Let's do one slightly more practical combination.

Start with:

numbers = [15, 40, 10, 30, 20]

Your task is to make the list:

[40, 30, 20, 15, 10]
🎯 Requirement

Use the two list methods we've learned:

sort()
reverse()
"""

print()

numbers = [15, 40, 10, 30, 20]

numbers.sort()
numbers.reverse()
print(numbers)      # output: [40, 30, 20, 15, 10]

# =============================

"""
🟢 List Problem 58 — Traversal + sort()

Start with:

numbers = [50, 20, 40, 10, 30]
🎯 Task
Sort the list in ascending order using sort().
Traverse the sorted list using a for loop.
Print each number on a separate line.
Expected output
10
20
30
40
50
Requirements
✅ Use sort()
✅ Use a for loop
❌ Don't use sorted() yet
❌ Don't manually create the sorted list
"""

print()

numbers = [50, 20, 40, 10, 30]

numbers.sort()

for number in numbers:
   print(number)

"""
Output:
10
20
30
40
50
"""

# ==========================================

"""
🟢 List Problem 59 — Traversal + reverse()

Start with:

numbers = [10, 20, 30, 40, 50]
🎯 Task
Reverse the original list using reverse().
Traverse the reversed list using a for loop.
Print each number on a separate line.
Expected output
50
40
30
20
10
Requirements
✅ Use reverse()
✅ Use a for loop
❌ Don't use slicing [::-1]
❌ Don't use reversed()
"""

print()

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

for number in numbers:
   print(number)

"""
Output:
50
40
30
20
10
"""

# ==================================

"""
🟢 List Problem 60 — sort() + reverse() + Traversal

Let's combine everything you've learned about ordering and traversal.

Start with:

numbers = [25, 5, 40, 15, 30]
🎯 Task
Sort the list in ascending order using sort().
Reverse the sorted list using reverse().
Traverse the final list using a for loop.
Print each number on a separate line.
Expected output
40
30
25
15
5
Requirements
✅ Use sort()
✅ Use reverse()
✅ Use for loop
❌ Don't use sorted()
❌ Don't use slicing
❌ Don't manually arrange the numbers
"""

print()

numbers = [25, 5, 40, 15, 30]

numbers.sort()
numbers.reverse()

for number in numbers:
   print(number)

"""
Output:
40
30
25
15
5
"""

# =======================================

"""
🟢 List Problem 61 — Practical List Processing

Start with:

numbers = [10, 25, 5, 40, 15, 30]
🎯 Task

Create a program that:

Sorts the list in ascending order using sort().
Prints the first element of the sorted list.
Prints the last element of the sorted list.
Expected output
First: 5
Last: 40
Requirements
✅ Use sort()
✅ Use list indexing
❌ Don't use min()
❌ Don't use max()
❌ Don't use sorted()
"""

print()

numbers = [10, 25, 5, 40, 15, 30]

numbers.sort()
print(f"First: {numbers[0]}")
print(f"Last: {numbers[5]}")

"""
First: 5
Last: 40
"""

# =======================================

"""
🟢 Problem 62 — Last Element

Start with:

numbers = [15, 30, 5, 40, 25]

Sort the list in ascending order and print the last element.

Expected:

Last: 40

Requirement: Use sort() and list indexing.
"""

print()

numbers = [15, 30, 5, 40, 25]

numbers.sort()
print(numbers[4])

"""
output:
40
"""

# ===============================

"""
🟢 Problem 63 — Quick One
numbers = [20, 5, 35, 10, 25]

Sort the list in ascending order and print the first element.

Expected:

First: 5

Use: sort() + list indexing.
"""

print()

numbers = [20, 5, 35, 10, 25]

numbers.sort()
print(f"First: {numbers[0]}")

"""
Output:
First: 5
"""

# ================================

"""
🟢 Problem 64 — Last Quick One

Start with:

numbers = [45, 10, 30, 5, 20]
🎯 Task
Sort the list in ascending order.
Print the first and last elements using indexing.
Match this output exactly:
First: 5
Last: 45

Use only: sort() + list indexing.
"""

print()

numbers = [45, 10, 30, 5, 20]

numbers.sort()
print(f"First: {numbers[0]}")
print(f"Last: {numbers[4]}")

"""
Output:
First: 5
Last: 45
"""

# ==========================================

"""
Problem 65

Start with:

numbers = [10, 20, 30, 40, 50]

Write a program that:

Traverses the list using a for loop.
Checks whether each number is greater than 25.
Prints only the numbers greater than 25.

Expected output:

30
40
50
🎯 Requirements
Use a for loop
Use an if condition
Work directly with the list
Don't manually print 30, 40, 50
"""

print()

numbers = [10, 20, 30, 40, 50]

for number in numbers:
   if number > 25:
      print(number)

"""
Output:
30
40
50
"""

# ======================================

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

"""
🟢 Problem 67 — Filter Numbers by a Condition

Start with:

numbers = [12, 7, 25, 40, 18, 5, 30]
🎯 Task

Traverse the list and print only the numbers greater than 20.

Expected output:

25
40
30
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Work directly with the list
❌ Don't manually print the answers
❌ Don't use filter() yet
"""

print()

numbers = [12, 7, 25, 40, 18, 5, 30]

for number in numbers:
   if number > 20:
      print(number)

"""
Output:
25
40
30
"""

# ===================================================

"""
🟢 Problem 68 — Filter + Calculation

Now let's make it one step more practical.

Start with:

numbers = [10, 15, 20, 25, 30, 35]
🎯 Task

Traverse the list and print only the numbers greater than 20, multiplied by 2.

Expected output:

50
60
70
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Use the condition number > 20
✅ Multiply the matching number by 2
❌ Don't manually print the answers
❌ Don't use filter()
"""

print()

numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
   if number > 20:
      print(number * 2)

"""
Output:
50
60
70
"""

# =============================================

"""
🟢 Problem 69 — Filter + Store Results

Now let's take the next small step.

Start with:

numbers = [5, 12, 25, 8, 30, 17, 40]
🎯 Task

Traverse the list and create a new list containing only the numbers greater than 20.

Expected result:

[25, 30, 40]
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Create a new list
❌ Don't modify the original numbers list
❌ Don't use filter() yet
❌ Don't use list comprehension yet
"""

print()

numbers = [5, 12, 25, 8, 30, 17, 40]

result = []

for number in numbers:
   if number > 20:
      result.append(number)

print(result)

"""
Output:
[25, 30, 40]
"""

# ============================================

"""
🟢 Problem 70 — Filter + Store Even Numbers

Start with:

numbers = [7, 12, 19, 24, 31, 40, 45, 18]
🎯 Task

Create a new list containing only the even numbers from numbers.

Expected result:

[12, 24, 40, 18]
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Create a new empty list
✅ Use append() to store matching numbers
❌ Don't modify the original numbers list
❌ Don't use filter()
❌ Don't use list comprehension yet
"""

print()

numbers = [7, 12, 19, 24, 31, 40, 45, 18]

result = []

for number in numbers:
   if number % 2 == 0:
      result.append(number)

print(result)

"""
Output:
[12, 24, 40, 18]
"""

# ============================================

"""
🟢 Problem 71 — sorted() vs sort()

This is an important distinction before we move ahead.

Start with:

numbers = [40, 10, 30, 20, 50]
🎯 Task

Use sorted() to create a new sorted list.

Then print:

The original numbers list
The new sorted list
Expected output
Original: [40, 10, 30, 20, 50]
Sorted: [10, 20, 30, 40, 50]
Requirements
✅ Use sorted()
✅ Store the returned result in a new variable
✅ Print both lists
❌ Don't use sort()
❌ Don't manually arrange the values
"""

print()

numbers = [40, 10, 30, 20, 50]

print(f"Original: {numbers}")              

new_list = sorted(numbers)
print(f"Sorted: {new_list}")

"""
Output:
Original: [40, 10, 30, 20, 50]
Sorted: [10, 20, 30, 40, 50]
"""

# ============================================

"""
🟢 Problem 72 — sorted() in Descending Order

Start with:

numbers = [15, 40, 10, 30, 25]
🎯 Task

Use sorted() to create a new list in descending order.

Print:

Original: [15, 40, 10, 30, 25]
Descending: [40, 30, 25, 15, 10]
Requirements
✅ Use sorted()
✅ Store the result in a new variable
✅ Use the appropriate option to get descending order
✅ Keep the original list unchanged
❌ Don't use sort()
❌ Don't use reverse()
"""

print()

numbers = [15, 40, 10, 30, 25]

print(f"Original: {numbers}")

new_list_desc = sorted(numbers, reverse = True)
print(f"Descending: {new_list_desc}")

"""
Output:
Original: [15, 40, 10, 30, 25]
Descending: [40, 30, 25, 15, 10]
"""

# =================================================

"""
🟢 Problem 73 — sorted() + Original List

Start with:

numbers = [50, 20, 40, 10, 30]
🎯 Task

Use sorted() to create a new list in ascending order, then:

Print the original list.
Print the new sorted list.
Print the original list again to prove it was not changed.
Expected Output
Original: [50, 20, 40, 10, 30]
Sorted: [10, 20, 30, 40, 50]
Original After: [50, 20, 40, 10, 30]
"""

print()

numbers = [50, 20, 40, 10, 30]

print(f"Original: {numbers}")

new_list = sorted(numbers)
print(f"Sorted: {new_list}")

print(f"Original After: {numbers}")

"""
Output:
Original: [50, 20, 40, 10, 30]
Sorted: [10, 20, 30, 40, 50]
Original After: [50, 20, 40, 10, 30]
"""

# ================================================

"""
🟢 Problem 74 — sorted() with Strings

Start with:

languages = ["Python", "Java", "C", "JavaScript", "Go"]
🎯 Task

Use sorted() to create a new list of languages in alphabetical order.

Print:

Original: ['Python', 'Java', 'C', 'JavaScript', 'Go']
Sorted: ['C', 'Go', 'Java', 'JavaScript', 'Python']
Requirements
✅ Use sorted()
✅ Store the result in a new variable
✅ Keep the original list unchanged
❌ Don't use sort()
"""

print()

languages = ["Python", "Java", "C", "JavaScript", "Go"]

print(f"Original: {languages}")

new_list = sorted(languages)
print(f"Sorted: {new_list}")

"""
Output:
Original: ['Python', 'Java', 'C', 'JavaScript', 'Go']
Sorted: ['C', 'Go', 'Java', 'JavaScript', 'Python']
"""

# ==================================

"""
🟢 Problem 75 — sorted() + Descending Strings

Start with:

languages = ["Python", "Java", "C", "JavaScript", "Go"]
🎯 Task

Use sorted() to create a new list in reverse alphabetical order.

Expected output:

Original: ['Python', 'Java', 'C', 'JavaScript', 'Go']
Descending: ['Python', 'JavaScript', 'Java', 'Go', 'C']
Requirements
✅ Use sorted()
✅ Store the result in a new variable
✅ Use the appropriate sorted() option for descending order
✅ Keep the original list unchanged
❌ Don't use sort()
❌ Don't use slicing/reverse
"""

print()

languages = ["Python", "Java", "C", "JavaScript", "Go"]

print(f"Original: {languages}")

new_list_desc = sorted(languages, reverse = True)
print(f"Descending: {new_list_desc}")

"""
Output:
Original: ['Python', 'Java', 'C', 'JavaScript', 'Go']
Descending: ['Python', 'JavaScript', 'Java', 'Go', 'C']
"""

# =========================================

"""
🟢 Problem 76 — List + sorted() + Condition

Start with:

numbers = [45, 12, 30, 8, 25, 50, 18]
🎯 Task

Use sorted() to create a new ascending list, then use a loop to print only the numbers greater than 20.

Expected output:

Sorted: [8, 12, 18, 25, 30, 45, 50]
Numbers Greater Than 20:
25
30
45
50
Requirements
✅ Use sorted()
✅ Store the sorted result in a new variable
✅ Keep the original list unchanged
✅ Use a for loop
✅ Use if
❌ Don't use sort()
"""

print()

numbers = [45, 12, 30, 8, 25, 50, 18]

new_list = sorted(numbers)
print(f"Sorted: {new_list}")

print("Numbers Greater Than 20:")
for num in new_list:
   if num > 20:
      print(num)

"""
Output:
Sorted: [8, 12, 18, 25, 30, 45, 50]
Numbers Greater Than 20:
25
30
45
50
"""

# =================================================

"""
Problem 77 — List Processing Challenge

Start with:

numbers = [35, 10, 50, 20, 45, 15, 30]
🎯 Task

Write a program that:

Creates a new sorted list in ascending order using sorted().
Prints the sorted list.
Uses a for loop to go through the sorted list.
Prints only the numbers that are greater than 20.
Expected Output
Sorted: [10, 15, 20, 30, 35, 45, 50]
Numbers Greater Than 20:
30
35
45
50
Requirements
✅ sorted()
✅ New variable
✅ for loop
✅ if
❌ Don't use sort()
❌ Don't use list comprehension yet
"""
print()
numbers = [35, 10, 50, 20, 45, 15, 30]

new_list = sorted(numbers)
print(f"Sorted: {new_list}")

print("Numbers Greater Than 20:")
for num in new_list:
   if num > 20:
      print(num)

"""
Output:
Sorted: [10, 15, 20, 30, 35, 45, 50]
Numbers Greater Than 20:
30
35
45
50
"""

# ==========================================

"""
🟢 Problem 78 — Mixed List Challenge

Now let's remove one piece of guidance.

Start with:

numbers = [12, 45, 20, 8, 35, 50, 15, 30]
🎯 Task

Create a new list containing only the numbers that are:

greater than 20 AND even

Then print the resulting list.

Expected Output
Result: [30, 50]
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Store matching numbers in a new list
❌ Don't modify the original numbers list
❌ Don't use list comprehension yet
"""

print()

numbers = [12, 45, 20, 8, 35, 50, 15, 30]

result = []

for num in numbers:
   if num > 20 and num % 2 == 0:
      result.append(num)
      
new_result = sorted(result)
print(f"Result: {new_result}")

"""
Output:
Result: [30, 50]
"""

# ================================

"""
🟢 Problem 79 — Mixed List Challenge

Start with:

numbers = [10, 25, 40, 15, 30, 50, 20]
🎯 Task

Create a new list containing the numbers that are:

greater than 20 and less than 50

Expected output:

Result: [25, 40, 30]
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Store matching values in a new list
❌ Don't modify numbers
❌ Don't use list comprehension
"""

print()

numbers = [10, 25, 40, 15, 30, 50, 20]

result = []

for num in numbers:
   if num > 20 and num < 50:
      result.append(num)

print(f"Result: {result}")

"""
Result: [25, 40, 30]
"""

# ==============================================

"""
Problem 80 — Mixed List Challenge

Start with:

numbers = [25, 10, 40, 15, 30, 5, 50, 20]
🎯 Task

Create a new list containing only the numbers that satisfy both conditions:

Greater than 15 AND even

Then print the result.

Expected Output
Result: [40, 30, 50, 20]
Requirements
✅ Use a for loop
✅ Use an if condition
✅ Use and
✅ Use % to check whether a number is even
✅ Store matching numbers in a new list
❌ Don't modify the original list
❌ Don't use list comprehension
❌ Don't sort the result
"""

print()

numbers = [25, 10, 40, 15, 30, 5, 50, 20]

result = []

for num in numbers:
   if num > 15 and num % 2 == 0:
      result.append(num)

print(f"Result: {result}")

"""
Output:
Result: [40, 30, 50, 20]
"""

# ====================================

"""
🟢 Problem 81 — Mixed List Challenge

Let's increase the difficulty just one small step.

Start with:

numbers = [12, 45, 22, 18, 35, 40, 27, 50, 14]
🎯 Task

Create a new list containing numbers that satisfy all three conditions:

Greater than 20 AND less than 50 AND even

Expected output:

Result: [22, 40, 50?]
"""

print()

numbers = [12, 45, 22, 18, 35, 40, 27, 50, 14]

result = []

for num in numbers:
   if num > 20 and num < 50 and num % 2 == 0:
      result.append(num)

print(f"Result: {result}")

"""
Output:
Result: [22, 40]
"""

# =====================================

"""
🟢 Problem 82 — Mixed List Challenge

Let's make this slightly more practical.

Start with:

numbers = [10, 35, 22, 48, 15, 60, 27, 42, 18]
🎯 Task

Create a new list containing numbers that are:

Even AND greater than 20

But this time, after creating the list, print both the result and its length.

Expected output:

Result: [22, 48, 60, 42]
Count: 4
"""

print()

numbers = [10, 35, 22, 48, 15, 60, 27, 42, 18]

result = []

for num in numbers:
   if num % 2 == 0 and num > 20:
      result.append(num)

print(f"Result: {result}")
print(f"Length: {len(result)}")

"""
Output:
Result: [22, 48, 60, 42]
Length: 4
"""

# =========================================

"""
🟢 Problem 83 — One step harder

Now let's test whether you can calculate while filtering, which you've already practiced earlier.

Start with:

numbers = [10, 25, 30, 15, 40, 5, 50]
🎯 Task

Create a new list containing double the value of every number that is:

greater than 20 AND even

Expected output:

Result: [60, 80, 100]
Requirements
✅ for
✅ if
✅ and
✅ % 2 == 0
✅ append()
✅ New list
❌ Don't modify original
❌ No list comprehension
❌ Don't sort
"""

print()

numbers = [10, 25, 30, 15, 40, 5, 50]

result = []

for num in numbers:
   if num > 20 and num % 2 == 0:
      result.append(num + num)

print(f"Result: {result}")

"""
Output:
Result: [60, 80, 100]
"""

# ============================================

"""
🟢 Problem 84 — Strings + Lists Mixed Challenge

Start with:

names = ["muskan", "doraemon", "python", "swt club", "django"]
🎯 Task

Create a new list containing only the names whose length is greater than 6 characters.

Then print the result.

Expected Output
Result: ['doraemon', 'swt club']

⚠️ Important: Treat the space in "swt club" as a character because Python's len() counts spaces too.

Requirements
✅ Use a for loop
✅ Use an if condition
✅ Use len()
✅ Store matching values in a new list
❌ Don't modify the original list
❌ Don't use list comprehension
❌ Don't manually count the characters
"""

print()

names = ["muskan", "doraemon", "python", "swt club", "django"]

result = []

for name in names:
   if len(name) > 6:
      result.append(name)

print(f"Result: {result}")

"""
Output:
Result: ['doraemon', 'swt club']
"""

# =====================================

"""
🟢 Problem 85 — Strings + Lists

Let's make it slightly harder.

Start with:

names = ["Muskan", "Doraemon", "python", "SWT CLUB", "django", "AI"]
🎯 Task

Create a new list containing only the names that:

Have more than 4 characters AND start with an uppercase letter

Expected output:

Result: ['Muskan', 'Doraemon', 'SWT CLUB']
Requirements
✅ Use a for loop
✅ Use an if
✅ Use len()
✅ Use a string method you've already learned
✅ Use and
✅ Store matches in a new list
❌ No list comprehension
❌ Don't manually select the names
"""

print()

names = ["Muskan", "Doraemon", "python", "SWT CLUB", "django", "AI"]

result = []

for name in names:
   if len(name) > 4 and name[0].isupper():
      result.append(name)

print(f"Result: {result}")

"""
Output:
Result: ['Muskan', 'Doraemon', 'SWT CLUB']
"""

# =======================================

"""
🟢 Problem 86 — Strings + Lists Mixed

Now we'll make the test a little more interesting.

Start with:

names = ["Muskan", "doraemon", "PYTHON", "SWT Club", "django", "AI", "Developer"]
🎯 Task

Create a new list containing names that satisfy both:

Length greater than 5 AND contains the letter "o"

Expected output:

Result: ['doraemon', 'django', 'Developer']
Requirements
✅ for
✅ if
✅ len()
✅ String membership using in
✅ and
✅ New list + append()
❌ No list comprehension
❌ Don't manually select names
"""

print()

names = ["Muskan", "doraemon", "PYTHON", "SWT Club", "django", "AI", "Developer"]

result = []

for name in names:
   if len(name) > 5 and "o" in name:
      result.append(name)

print(f"Result: {result}")

"""
Output:
Result: ['doraemon', 'django', 'Developer']
"""

# ==================================

"""
🟢 Problem 87 — Strings + Lists Mixed

Start with:

words = ["Python", "Django", "AI", "Developer", "Code", "Automation"]
🎯 Task

Create a new list containing words that satisfy both conditions:

Length greater than 4 AND the word starts with "D"

Expected output:

Result: ['Django', 'Developer']
Requirements
✅ Use a for loop
✅ Use if
✅ Use len()
✅ Use a string method you've already learned
✅ Use and
✅ Store matches in a new list
❌ No list comprehension
❌ Don't manually select the words
"""

print()

words = ["Python", "Django", "AI", "Developer", "Code", "Automation"]

result = []

for word in words:
   if len(word) > 4 and word.startswith("D"):
      result.append(word)

print(f"Result: {result}")

"""
Output:
Result: ['Django', 'Developer']
"""

# =====================================

"""
🟢 Problem 88 — Strings + Lists Mixed

Let's remove some of the guidance now.

Start with:

words = ["python", "Django", "developer", "AI", "automation", "Code", "database"]
🎯 Task

Create a new list containing words that:

Have more than 6 characters AND contain the letter "a"

Expected output:

Result: ['automation', 'database']
Requirements
✅ for
✅ if
✅ len()
✅ in
✅ and
✅ append()
❌ No list comprehension
❌ Don't manually select words
"""

print()

words = ["python", "Django", "developer", "AI", "automation", "Code", "database"]

result = []

for word in words:
   if len(word) > 6 and "a" in word:
      result.append(word)

print(f"Result: {result}")

"""
Output:
Result: ['automation', 'database']
"""

# ===============================

"""
Problem 89 — Strings + Lists + Transformation

Start with:

names = ["muskan", "DORAEMON", "python", "SWT CLUB", "django"]

🎯 Task

Create a new list containing the names converted to lowercase, but only if the original name has more than 5 characters.

Expected output:

Result: ['muskan', 'doraemon', 'python', 'swt club', 'django']

Requirements

✅ for
✅ if
✅ len()
✅ .lower()
✅ append()
✅ New list

❌ Don't modify the original list
❌ No list comprehension
"""

print()

names = ["muskan", "DORAEMON", "python", "SWT CLUB", "django"]

result = []

for name in names:
   if len(name) > 5:
      result.append(name.lower())

print(f"Result: {result}")

"""
Output:
Result: ['muskan', 'doraemon', 'python', 'swt club', 'django']
"""

# ================================

"""
🐍 Problem 90 — Strings + Lists + Filtering & Transformation

Start with:

words = ["Python", "Django", "AI", "Developer", "Code", "Automation", "API"]
🎯 Task

Create a new list containing the words that:

Have more than 4 characters, AND
Contain the letter "o".

Before adding a word to the new list, convert it to lowercase.

Expected output
Result: ['python', 'django', 'developer', 'automation']
Requirements

✅ for
✅ if
✅ len()
✅ and
✅ "o" in word
✅ .lower()
✅ append()
✅ New list

❌ Don't modify the original list
❌ No list comprehension
❌ Don't use methods/functions we haven't learned
"""

print()

words = ["Python", "Django", "AI", "Developer", "Code", "Automation", "API"]

result = []

for word in words:
   if len(word) > 4 and "o" in word:
      result.append(word.lower())

print(f"Result:{result}") 

"""
Output:
Result:['python', 'django', 'developer', 'automation']
"""

# =======================================

"""
🐍 Problem 91 — Lists + Strings + Multiple Conditions
Start with:

names = ["Muskan", "doraemon", "Python", "SWT CLUB", "django", "AI", "Developer"]

🎯 Task

Create a new list containing the names that:

1. Have more than 5 characters
2. Start with an uppercase letter
3. Contain the letter "o"

Before adding a name to the new list, convert it to lowercase.

Expected output:

Result: ['doraemon', 'developer']

Requirements

✅ for
✅ if
✅ len()
✅ and
✅ .isupper()
✅ "o" in name
✅ .lower()
✅ append()
✅ New list

❌ Don't modify the original list
❌ No list comprehension
"""

print()

names = ["Muskan", "doraemon", "Python", "SWT CLUB", "django", "AI", "Developer"]

result = []

for name in names:
   if len(name) > 5 and name[0].isupper() and "o" in name:
      result.append(name.lower())

print(f"Result: {result}")

"""
Output:
Result: ['Python', 'Developer']
"""

# ==================================

"""
# Notes:

🐍 List Comprehension

List comprehension is a short and clean way to create a new list from an existing iterable such as a list or string.

1. Basic Syntax
[expression for item in iterable]

Example:

numbers = [1, 2, 3, 4, 5]

result = [num * 2 for num in numbers]

print(result)

Output:

[2, 4, 6, 8, 10]

2. List Comprehension with if

Used when we want to filter values.

Syntax
[expression for item in iterable if condition]

Example:

numbers = [10, 15, 20, 25, 30]

result = [num for num in numbers if num > 20]

print(result)

Output:

[25, 30]

3. List Comprehension with Transformation

We can filter and transform values at the same time.

numbers = [10, 15, 20, 25, 30]

result = [num * 2 for num in numbers if num > 20]

print(result)

Output:

[50, 60]

4. Strings with List Comprehension

List comprehension can also be used with strings.

names = ["Muskan", "Doraemon", "Python"]

result = [name.lower() for name in names]

print(result)

Output:

['muskan', 'doraemon', 'python']

5. Important Things to Remember
List comprehension creates a new list.
It is an alternative to a normal for loop when creating a list.
expression → tells Python what to store.
for → goes through each item.
if → optionally filters items.
The if condition comes after the for part.
The expression can perform transformations such as:
num * 2
num + 10
name.lower()
name.upper()
Multiple conditions can be combined using and / or.
The original list is not modified unless we deliberately modify its elements/objects.
No append() is required because list comprehension automatically builds the new list.

6. Normal for Loop vs List Comprehension
Normal approach
result = []

for num in numbers:
    if num > 20:
        result.append(num)
List comprehension
result = [num for num in numbers if num > 20]

Both produce the same type of result.

🧠 Easy Way to Read It

For:

result = [num * 2 for num in numbers if num > 20]

Read it as:

"For every num in numbers, if num is greater than 20, store num * 2 in the new list."

Remember:
WHAT TO STORE
      ↓
[ expression for item in iterable if condition ]
              ↑                    ↑
             LOOP                FILTER
⭐ Two Main Patterns to Remember
Without condition
[expression for item in iterable]
With condition
[expression for item in iterable if condition]

"""

# ===============================

"""
🐍 Problem 92 — Basic List Comprehension

Start with:

numbers = [5, 10, 15, 20, 25]
Task

Create a new list containing each number multiplied by 2 using list comprehension.

Expected output:

Result: [10, 20, 30, 40, 50]
Requirements

✅ List comprehension
✅ Multiplication
✅ New list

❌ No normal for loop
❌ No append()
"""

print()

numbers = [5, 10, 15, 20, 25]

result = [num * 2 for num in numbers]

print(f"Result: {result}")

"""
Ouitput:
Result: [10, 20, 30, 40, 50]
"""

# =================================

"""
🐍 Problem 93 — List Comprehension + Condition

Start with:

numbers = [10, 15, 20, 25, 30, 35, 40]
Task

Create a new list containing only the even numbers greater than 20 using list comprehension.

Expected output:

Result: [30, 40]
Requirements

✅ List comprehension
✅ for
✅ if
✅ and
✅ % operator
✅ New list

❌ No normal for loop
❌ No append()
"""

print()

numbers = [10, 15, 20, 25, 30, 35, 40]

result = [num for num in numbers if num % 2 == 0 and num > 20]

print(f"Result: {result}")

"""
Output:
Result: [30, 40]
"""

# =================================================

"""
🐍 Problem 94 — List Comprehension + Transformation

Start with:

numbers = [5, 10, 15, 20, 25, 30]
🎯 Task

Create a new list containing only the numbers greater than 15, but store their double value in the new list.

Expected output
Result: [40, 50, 60]
Requirements

✅ List comprehension
✅ for
✅ if
✅ >
✅ Multiplication
✅ New list

❌ No normal for loop
❌ No append()
"""

print()

numbers = [5, 10, 15, 20, 25, 30]

result = [num * 2 for num in numbers if num > 15]
print(f"Result: {result}")

"""
Output:
Result: [40, 50, 60]
"""

# =======================================

"""
🐍 Problem 95 — List Comprehension + Strings

Now let's connect List Comprehension with the String concepts you've already learned.

Start with:

names = ["Muskan", "Doraemon", "Python", "Django", "AI", "Developer"]
🎯 Task

Create a new list containing the names that:

Have more than 5 characters
Convert each matching name to lowercase
Expected output
Result: ['muskan', 'doraemon', 'python', 'developer']
Requirements

✅ List comprehension
✅ for
✅ if
✅ len()
✅ > 5
✅ .lower()
✅ New list

❌ No normal for loop
❌ No append()
❌ Don't modify the original list
"""

print()

names = ["Muskan", "Doraemon", "Python", "Django", "AI", "Developer"]

result = [name.lower() for name in names if len(name) > 5]

print(f"Result: {result}")

"""
Output:
Result: ['muskan', 'doraemon', 'python', 'django', 'developer']
"""

# ================================

"""
⭐ Key rule

Length = number of characters
Last index = length - 1
"""

# ===============================================

"""
🐍 Problem 96 — List Comprehension + Strings + Multiple Conditions

Start with:

words = ["Python", "Django", "AI", "Developer", "Code", "Automation", "API"]
🎯 Task

Create a new list containing the words that:

Have more than 4 characters
Start with an uppercase letter
Contain the letter "o"

Before adding each matching word to the new list, convert it to lowercase.

Expected output
Result: ['python', 'django', 'developer', 'automation']
Requirements

✅ List comprehension
✅ for
✅ if
✅ len()
✅ and
✅ .isupper() on the first character
✅ "o" in word
✅ .lower()
✅ New list

❌ No normal for loop
❌ No append()
❌ Don't modify the original list
"""

print()

words = ["Python", "Django", "AI", "Developer", "Code", "Automation", "API"]

result = [word.lower() for word in words if len(word) > 4 and word[0].isupper() and "o" in word]
print(f"Result: {result}")

"""
Output:
Result: ['python', 'django', 'developer', 'automation']
"""

# ================================

"""
🐍 Problem 97 — List Comprehension + if/else

Start with:

numbers = [5, 10, 15, 20, 25, 30]
🎯 Task

Create a new list using list comprehension where:

If the number is even, store "Even"
Otherwise, store "Odd"
Expected output
Result: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
Requirements

✅ List comprehension
✅ for
✅ if
✅ else
✅ % operator
✅ New list

❌ No normal for loop
❌ No append()
❌ No regular if/else block outside the comprehension
"""

print()

numbers = [5, 10, 15, 20, 25, 30]

result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(f"Result: {result}")

"""
Output:
Result: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
"""

# ===============================

"""
🐍 Problem 98 — List Comprehension + Strings + if/else

Start with:

names = ["Muskan", "AI", "Python", "Go", "Developer"]
🎯 Task

Create a new list where:

If the length of the name is greater than 5, store the name in uppercase
Otherwise, store the name in lowercase
Expected output
Result: ['MUSKAN', 'ai', 'PYTHON', 'go', 'DEVELOPER']
Requirements

✅ List comprehension
✅ if/else
✅ len()
✅ .upper()
✅ .lower()

❌ No normal for loop
❌ No append()
"""

print()

names = ["Muskan", "AI", "Python", "Go", "Developer"]

result = [name.upper() if len(name) > 5 else name.lower() for name in names]
print(f"Result: {result}")

"""
Output:
Result: ['MUSKAN', 'ai', 'PYTHON', 'go', 'DEVELOPER']
"""

# ======================================

"""
🐍 Problem 99 — Practical List Comprehension — Student Results

Start with:

students = ["Muskan", "Aarav", "Riya", "Doraemon", "Sam"]
marks = [85, 42, 76, 95, 38]
🎯 Task

Create a new list containing a result message for each student:

If the student's marks are 50 or more, store:

"Name: Pass"

Otherwise, store:

"Name: Fail"

The student's name should remain exactly as it appears in the original students list.

Expected output
Result: ['Muskan: Pass', 'Aarav: Fail', 'Riya: Pass', 'Doraemon: Pass', 'Sam: Fail']
Requirements

✅ List comprehension
✅ if/else
✅ >=
✅ for
✅ f-string
✅ New list

❌ No normal for loop
❌ No append()
❌ No modification of the original lists
❌ Don't use any new concept
"""

print()

students = ["Muskan", "Aarav", "Riya", "Doraemon", "Sam"]
marks = [85, 42, 76, 95, 38]

result = [
   f"{students[i]}: Pass" if marks[i] >= 50 else f"{students[i]}: Fail"
   for i in range(len(students))
]
print(f"Result: {result}")

"""
Output:
Result: ['Muskan: Pass', 'Aarav: Fail', 'Riya: Pass', 'Doraemon: Pass', 'Sam: Fail']
"""

# =================================