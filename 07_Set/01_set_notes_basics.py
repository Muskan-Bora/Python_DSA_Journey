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

"""
Problem 6 — Add and remove set elements
Problem statement
Start with this set:
numbers = {10, 20, 30, 40}

Write a program that:
1. Adds 50 to the set.
2. Removes 20 using remove().
3. Discards 100 using discard().
4. Prints the set after each operation using f-strings.
5. Prints the final number of elements using len().
Expected final result: {10, 30, 40, 50} — the order may vary.

Expected final count: 4
"""

print()

numbers = {10, 20, 30, 40}

numbers.add(50)
print(f"Added 50: {numbers}")

numbers.remove(20)
print(f"Removed 20: {numbers}")

numbers.discard(100)
print(f"Discarded 100: {numbers}")

final_result = numbers
print(f"final result: {final_result}")
print(f"final count: {len(final_result)}")

"""
Output of all:
Added 50: {40, 10, 50, 20, 30}
Removed 20: {40, 10, 50, 30}
Discarded 100: {40, 10, 50, 30}
final result: {40, 10, 50, 30}
final count: 4
"""

# =========================================

# Python Sets — Intersection (Common Elements)

"""
1. Intersection finds elements common to both sets.
2. Use set1.intersection(set2) to create a new set containing common elements.
3. The & operator is a shortcut for intersection.
4. If there are no common elements, Python returns set().
5. Intersection does not modify the original sets.
6. Use len() to count how many common elements exist.

Quick Revision Table
# Operation	                # Syntax	                    # Result
Intersection	            set1.intersection(set2)	        Common elements
Intersection (shortcut)	    set1 & set2	                    Common elements
Count common elements	    len(set1.intersection(set2))	Number of common elements

Remember this example
set_a = {5, 10, 15, 20}
set_b = {15, 20, 25, 30}

common = set_a.intersection(set_b)

print(common)


Output:
{15, 20}
"""

# ===================================

"""
Problem 7
Given these two sets:
set_a = {5, 10, 15, 20, 25}
set_b = {15, 20, 25, 30, 35}

Write a program that:
1. Prints both original sets.
2. Finds their common elements using .intersection().
3. Prints the common elements.
4. Prints the number of common elements using len().
5. Uses f-strings for every output statement.

Expected common elements: {15, 20, 25}
Expected count: 3
"""

print()

set_a = {5, 10, 15, 20, 25}
set_b = {15, 20, 25, 30, 35}

print(f"Original Set of set_a: {set_a}")

print(f"Original Set of set_b: {set_b}")

common_elements = set_a.intersection(set_b)

print(f"common elements: {common_elements}")

print(f"Count of common elements: {len(common_elements)}")

"""
Output of all:
Original Set of set_a: {20, 5, 25, 10, 15}
Original Set of set_b: {35, 20, 25, 30, 15}
common elements: {25, 20, 15}
Count of common elements: 3
"""

# ==========================================

# Python Sets: Union

"""
Quick revision notes
1. Union combines all unique elements from two or more sets.
2. Use set_a.union(set_b) to calculate the union.
3. The | operator is a shortcut for union.
4. Duplicate elements appear only once.
5. Union returns a new set and doesn't modify the original sets.
6. Use len() to count the unique elements in the resulting set.

Operation	                        Syntax	                    Purpose
Union	                            set_a.union(set_b)	        Combines unique elements
Union shortcut	                    set_a \| set_b	            Same result
Count unique combined elements	    len(set_a.union(set_b))	    Counts the result
"""

# ==========================

"""
Problem 8 — Combine two sets

Given these two sets:
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

Write a program that:
1. Prints both original sets.
2. Combines them using .union().
3. Prints the resulting set.
4. Prints the number of unique elements using len().
5. Uses f-strings for every output statement.

Expected result: The union contains {10, 20, 30, 40, 50, 60}.
Expected count: 6
"""

print()

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

combined = set_a.union(set_b)
print(f"The union contains: {combined}")

print(f"The count of number of unique elements: {len(combined)}")

"""
Output of all:
Original set of set_a: {40, 10, 20, 30}
Original set of set_b: {40, 50, 60, 30}
The union contains: {40, 10, 50, 20, 60, 30}
The count of number of unique elements: 6
"""

# ==============================================

"""
Quick revision
- Intersection (.intersection()): finds common elements.
- Union (.union()): combines all unique elements.
"""

# =========================

# Python Sets: Difference

"""

1. Difference finds elements present in the first set but absent from the second.
2. Use set_a.difference(set_b).
3. The - operator is a shortcut: set_a - set_b.
4. Difference is directional; reversing the sets may change the result.
5. It returns a new set and doesn't modify the original sets.

Operation	                Meaning
A.difference(B)	            Elements in A but not B
A - B	                    Same as A.difference(B)
B - A	                    Elements in B but not A

"""

# ======================================

"""
Problem 9 — Find elements in one set only
Given these sets:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Write a program that:
1. Prints both original sets.
2. Finds elements in set_a but not in set_b using .difference().
3. Prints the result.
4. Finds elements in set_b but not in set_a.
5. Prints that result.
6. Uses f-strings for every output statement.

Expected results:
- set_a - set_b → {10, 20}
- set_b - set_a → {60, 70}
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

result = set_a.difference(set_b)

print(f"set_a - set_b → {result}")

results = set_b - set_a

print(f"set_b - set_a → {results}")

"""
Output of all:
Original set of set_a: {50, 20, 40, 10, 30}
Original set of set_b: {50, 70, 40, 60, 30}
set_a - set_b → {10, 20}
set_b - set_a → {60, 70}
"""

# =======================================

"""
Problem 10 — Intersection (Practice 2)
Focus: finding common elements using .intersection()

Given these sets:
set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 25, 35, 40, 45}

Write a program that:
1. Prints both original sets.
2. Finds the common elements using .intersection().
3. Prints the common elements.
4. Prints the total number of common elements using len().
5. Uses f-strings for every output statement.
Expected results:
- Common elements → {15, 20, 25}
- Total common elements → 3
"""

print()

set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 25, 35, 40, 45}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

common_elements = set_a.intersection(set_b)

print(f"Common elements → {common_elements}")
print(f"Total common elements → {len(common_elements)}")

"""
Output:
Original set of set_a: {20, 5, 25, 10, 30, 15}
Original set of set_b: {35, 20, 40, 25, 45, 15}
Common elements → {25, 20, 15}
Total common elements → 3
"""

# ========================================

"""
Problem 11 — Union (Practice 2)

Given these sets:
set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

Write a program that:
1. Prints both original sets.
2. Combines all unique elements using .union().
3. Prints the combined set.
4. Prints the total number of unique elements using len().
5. Uses f-strings for every output statement.
Expected results:
- Union: {10, 20, 30, 40, 50, 60, 70, 80}
- Total unique elements: 8
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

combined = set_a.union(set_b)

print(f"Union: {combined}")
print(f"Total unique elements: {len(combined)}")

"""
Output of all:
Original set of set_a: {50, 20, 40, 10, 30}
Original set of set_b: {80, 50, 70, 40, 60}
Union: {70, 40, 10, 80, 50, 20, 60, 30}
Total unique elements: 8
"""

# ===========================================

"""
Problem 12 — Difference (Practice 2)

Given these sets:
set_a = {10, 20, 30, 40, 50, 60}
set_b = {20, 40, 60, 70, 80}

Write a program that:
1. Prints both original sets.
2. Finds elements present in set_a but absent from set_b, using .difference().
3. Prints that result.
4. Finds elements present in set_b but absent from set_a, using .difference() as well.
5. Prints that result.
6. Prints the number of elements in each difference result using len().
7. Uses f-strings for every output statement.
Expected results:
- set_a.difference(set_b) → {10, 30, 50}; count: 3
- set_b.difference(set_a) → {70, 80}; count: 2
"""

print()

set_a = {10, 20, 30, 40, 50, 60}
set_b = {20, 40, 60, 70, 80}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

result = set_a.difference(set_b)

print(f"set_a.difference(set_b) → {result}; count: {len(result)}")

results = set_b - set_a

print(f"set_b.difference(set_a) → {results}; count: {len(results)}")

"""
Output of all:
Original set of set_a: {50, 20, 40, 10, 60, 30}
Original set of set_b: {80, 20, 70, 40, 60}
set_a.difference(set_b) → {50, 10, 30}; count: 3
set_b.difference(set_a) → {80, 70}; count: 2
"""

# ==================================================

# Symmetric Difference

"""

1. Symmetric difference returns elements present in either set but not in both.
2. Use set_a.symmetric_difference(set_b).
3. The ^ operator is a shortcut: set_a ^ set_b.
4. Common elements are excluded from the result.
5. It returns a new set and leaves the original sets unchanged.
6. If both sets contain exactly the same elements, the result is an empty set: set().

Quick comparison
Operation	                    What it returns
Intersection A & B	            Common elements
Union A \| B	                All unique elements from both sets
Difference A - B	            Elements in A but not B
Symmetric difference A ^ B	    Elements in either set, excluding common elements

"""

# ------------------

"""
Problem 13 

Given these sets:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Write a program that:
1. Prints both original sets.
2. Finds the symmetric difference using .symmetric_difference().
3. Prints the result using an f-string.
4. Prints the total number of elements in the result using len() and an f-string.
Expected results:
- Symmetric difference: {10, 20, 60, 70}
- Total elements: 4
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

result = set_a.symmetric_difference(set_b)

print(f"Symmetric difference: {result}")

print(f"Total elements: {len(result)}")

"""
Output of all:
Original set of set_a: {50, 20, 40, 10, 30}
Original set of set_b: {50, 70, 40, 60, 30}
Symmetric difference: {20, 70, 10, 60}
Total elements: 4
"""

# ==================================================

"""
Problem 14 — Symmetric Difference (Practice 2)

Given these sets:
set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 35, 40, 45}

Write a program that:
1. Prints both original sets.
2. Finds the symmetric difference using the ^ operator this time.
3. Prints the result using an f-string.
4. Prints the total number of elements using len() and an f-string.
5. Prints the original sets again to confirm they haven't changed.
Expected results:
- Symmetric difference: {5, 10, 25, 30, 35, 40, 45}
- Total elements: 7
- Original sets remain unchanged.
"""

print()

set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 35, 40, 45}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

results = set_a ^ set_b

print(f"Symmetric difference: {results}")

print(f"Total elements: {len(results)}")

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")

"""
Output of all:
Original set of set_a: {20, 5, 25, 10, 30, 15}
Original set of set_b: {35, 20, 40, 45, 15}
Symmetric difference: {5, 10, 25, 30, 35, 40, 45}
Total elements: 7
Original set of set_a: {20, 5, 25, 10, 30, 15}
Original set of set_b: {35, 20, 40, 45, 15}
"""

# =========================================

# Subset and Superset

"""

1. A subset contains only elements found in another set.
2. Use set_a.issubset(set_b) to check whether A is a subset of B.
3. A superset contains all elements of another set, possibly with additional elements.
4. Use set_a.issuperset(set_b) to check whether A is a superset of B.
5. Both methods return a Boolean value: True or False.
6. A set is also considered a subset and superset of itself.

Method	                Meaning
A.issubset(B)	        Every element of A is in B
A.issuperset(B)	        Every element of B is in A

"""

# =======================================

"""
Problem 15 — 
Given these sets:
set_a = {10, 20, 30}
set_b = {10, 20, 30, 40, 50}
set_c = {10, 20, 60}

Write a program that:
1. Prints all three original sets.
2. Checks whether set_a is a subset of set_b.
3. Checks whether set_b is a superset of set_a.
4. Checks whether set_c is a subset of set_b.
5. Prints every result using f-strings.

Expected results:
- set_a.issubset(set_b) → True
- set_b.issuperset(set_a) → True
- set_c.issubset(set_b) → False
"""

print()

set_a = {10, 20, 30}
set_b = {10, 20, 30, 40, 50}
set_c = {10, 20, 60}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")
print(f"Original set of set_c: {set_c}")

print(f"set_a.issubset(set_b) → {set_a.issubset(set_b)}")
print(f"set_b.issuperset(set_a) → {set_b.issuperset(set_a)}")
print(f"set_c.issubset(set_b) → {set_c.issubset(set_b)}")

"""
Output of all:
Original set of set_a: {10, 20, 30}
Original set of set_b: {50, 20, 40, 10, 30}
Original set of set_c: {10, 20, 60}
set_a.issubset(set_b) → True
set_b.issuperset(set_a) → True
set_c.issubset(set_b) → False
"""

# =========================================