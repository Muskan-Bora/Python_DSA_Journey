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