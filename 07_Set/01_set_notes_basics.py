# ==========================================

# Python Sets

"""
1. What is a set?
A set is a Python data structure that stores unique elements.

Look at this list:
numbers = [10, 20, 10, 30, 20, 40]
print(numbers)

Output:
[10, 20, 10, 30, 20, 40]

The list keeps the duplicate values. 
Now let's use a set:
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

Output (the order may vary):
{10, 20, 30, 40}

See the difference? 😊 The set keeps only one copy of each value.
- 10 appears twice in the original data, but only once in the set.
- 20 also appears twice, but only once in the set.
- The duplicate values are automatically eliminated.

Important: Sets are unordered, so don't rely on their printed order or on accessing elements by position.

2. How to create a set

A. Using curly braces {}
fruits = {"apple", "banana", "mango"}print(fruits)

This creates a set of three unique strings.

B. Creating an empty set
This is a very important Python detail!
empty_set = set()empty_dictionary = {}print(type(empty_set))print(type(empty_dictionary))

Output:
<class 'set'>
<class 'dict'>

Remember:
- set() creates an empty set.
- {} creates an empty dictionary, not an empty set.

C. A set automatically removes duplicates

numbers = {5, 5, 10, 10, 15, 15}print(len(numbers))

Output:
3

The set contains only three unique values: 5, 10, and 15.

3. The four important properties of sets

1. Unique elements
Duplicate values are automatically removed.
values = {1, 2, 2, 3}# {1, 2, 3}

2. Unordered
Sets don't guarantee a particular iteration or display order. Don't depend on the order of elements.

3. No indexing or slicing
This works with lists and tuples:
numbers = [10, 20, 30]print(numbers[0])  # 10

But this doesn't work with sets:
numbers = {10, 20, 30}# numbers[0]  -> TypeError

4. Mutable

You can add or remove elements after creating a set. However, individual set elements must be hashable, so you can't put a list or another
ordinary set directly inside a set.

4. List vs tuple vs set
This comparison is worth saving in your notes.

Feature	                List	Tuple	Set
Syntax	                [ ]	    ( )	    { }
Ordered	                Yes	    Yes	    No
Duplicates allowed	    Yes	    Yes	    No
Indexing and slicing	Yes	    Yes	    No
Mutable	                Yes	    No	    Yes
Empty structure	        []	    ()	    set()

Example to remember:
my_list = [10, 20, 10]
my_tuple = (10, 20, 10)
my_set = {10, 20, 10}
print(my_list)   
# [10, 20, 10]

print(my_tuple)  
# (10, 20, 10)

print(my_set)    
# {10, 20}

5. What are sets useful for?
Sets are particularly useful when you need to:
- Remove duplicate values from data.
- Check whether an element exists.
- Find common elements between two collections.
- Find elements that exist in one collection but not another.
- Compare groups of values, such as registered users across two lists.
"""

# ==================================

"""
Python Sets — Quick Revision
1. A set is a collection of unique elements.
2. Use {1, 2, 3} to create a non-empty set.
3. Use set() to create an empty set; {} creates an empty dictionary.
4. Duplicate values are automatically removed.
5. Sets are unordered; don't rely on element positions.
6. Sets do not support indexing or slicing.
7. Sets are mutable, so elements can be added and removed.
8. Set elements must be hashable.
9. Use len(my_set) to count unique elements.
10. Use for loops to iterate through a set.
"""

# ----------------------

"""
Problem 1 — Create and analyse a set

Given the following values:
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

Write a Python program that:
1. Converts the list into a set.
2. Prints the resulting set.
3. Prints the number of unique elements using len().
4. Uses an f-string for each output statement.
Expected result: The set contains 10, 20, 30, 40, 50, and the number of unique elements is 5. The displayed order of the set may vary.
"""

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = set(numbers)
print(f"The set contains {result}, and the number of unique elements is {len(result)}.")

"""
Output:
The set contains {40, 10, 50, 20, 30}, and the number of unique elements is 5.
"""

# ======================================

"""
Problem 2 — Create a set and add elements

Start with this set:
fruits = {"apple", "banana", "mango"}

Write a program that:
1. Prints the original set.
2. Adds "orange" using the add() method.
3. Prints the updated set.
4. Tries to add "apple" again.
5. Prints the set once more.
6. Uses f-strings for every output statement.
Expected behaviour:
- Initially, there are three unique fruits.
- After adding "orange", there are four.
- Adding "apple" again does not create a duplicate.
"""

print()

fruits = {"apple", "banana", "mango"}

print(f"Original Set: {fruits}")

fruits.add("orange")

print(f"Updated Set after adding orange: {fruits}")

fruits.add("apple")

print(f"Updated Set after adding apple again: {fruits}")

"""
Output:
Original Set: {'mango', 'apple', 'banana'}
Updated Set after adding orange: {'mango', 'apple', 'banana', 'orange'}
Updated Set after adding apple again: {'mango', 'apple', 'banana', 'orange'}
"""

# ============================================

"""
IMP NOTES:

remove() deletes the specified element.
If the element doesn't exist, remove() raises a KeyError.

discard() deletes the element if it exists.
If the element doesn't exist, discard() does nothing and doesn't raise an error.
"""

# ----------------------------

"""
Problem 3 — Remove elements from a set
Problem statement
Start with this set:
numbers = {10, 20, 30, 40, 50}

Write a program that:
1. Prints the original set.
2. Removes 30 using remove().
3. Prints the updated set.
4. Removes 40 using discard().
5. Prints the set again.
6. Tries to discard 100, which doesn't exist in the set.
7. Prints the final set.
8. Uses f-strings for every output statement.
"""

print()

numbers = {10, 20, 30, 40, 50}

print(f"The Original Set: {numbers}")
# Output: The Original Set: {50, 20, 40, 10, 30}

numbers.remove(30)

print(f"The updated set after removing 30: {numbers}")
# Output: The updated set after removing 30: {50, 20, 40, 10}

numbers.discard(40)

print(f"The updated set after discard 40: {numbers}")
# Output: The updated set after discard 40: {50, 20, 10}

numbers.discard(100)

print(f"The updated set after discard 100: {numbers}")
# Output: The updated set after discard 100: {50, 20, 10}

print(f"The Final Set: {numbers}")
# Output: The Final Set: {50, 20, 10}

# ===================================

"""
Python provides the in operator to check whether a value exists in a set. It returns a Boolean value: True or False
"""

"""
Your Problem 4 — Check element membership

Given the following set:
fruits = {"apple", "banana", "mango", "orange"}

Write a Python program that:
1. Checks whether "banana" exists in the set.
2. Checks whether "grapes" exists in the set.
3. Stores each result in a Boolean variable.
4. Prints both results using f-strings.
5. Uses the in operator for membership checking.
Expected output:
Is banana present? True
Is grapes present? False
"""

print()

fruits = {"apple", "banana", "mango", "orange"}

found = "banana" in fruits
print(f"Is banana present? {found}")

found = "grapes" in fruits
print(f"Is grapes present? {found}")

"""
Output:
Is banana present? True
Is grapes present? False
"""

# =============================================

"""
Problem 5 — Find the number of unique elements
Problem statement
Given the following list:
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

Write a Python program that:
1. Converts the list into a set.
2. Prints the set of unique numbers.
3. Uses a for loop to print each unique number individually.
4. Counts how many unique numbers exist using a counter and a loop — do not use len() for the count.
5. Prints the total number of unique numbers using an f-string.
Expected result:
- Unique numbers: 10, 20, 30, 40, 50, 60
- Total unique numbers: 6
"""

print()

numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

unique_numbers = set(numbers)

print(f"Unique numbers: {unique_numbers}")

count = 0

for unique_number in unique_numbers:
    count += 1

print(f"Total unique numbers: {count}")

"""
Output:
Unique numbers: {40, 10, 50, 20, 60, 30}
Total unique numbers: 6
"""

# ==================================