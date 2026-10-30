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

"""
Problem 16 — Subset and Superset (Practice 2)

Given these sets:
set_a = {5, 10}
set_b = {5, 10, 15, 20}
set_c = {5, 10, 15, 20}

Write a program that:
1. Prints all three original sets.
2. Checks whether set_a is a subset of set_b.
3. Checks whether set_b is a subset of set_c.
4. Checks whether set_c is a superset of set_a.
5. Checks whether set_a is a superset of set_c.
6. Prints every result using f-strings.

Expected results:
- set_a.issubset(set_b) → True
- set_b.issubset(set_c) → True
- set_c.issuperset(set_a) → True
- set_a.issuperset(set_c) → False
"""

print()

set_a = {5, 10}
set_b = {5, 10, 15, 20}
set_c = {5, 10, 15, 20}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")
print(f"Original set of set_c: {set_c}")

print(f"set_a.issubset(set_b) → {set_a.issubset(set_b)}")
print(f"set_b.issubset(set_c) → {set_b.issubset(set_c)}")
print(f"set_c.issuperset(set_a) → {set_c.issuperset(set_a)}")
print(f"set_a.issuperset(set_c) → {set_a.issuperset(set_c)}")

"""
Output of all:
Original set of set_a: {10, 5}
Original set of set_b: {10, 20, 5, 15}
Original set of set_c: {10, 20, 5, 15}
set_a.issubset(set_b) → True
set_b.issubset(set_c) → True
set_c.issuperset(set_a) → True
set_a.issuperset(set_c) → False
"""

# ================================

# Disjoint Sets

"""

What are disjoint sets?
Two sets are called disjoint when they have no common elements.
In simple words, if two sets don't share even a single element, they are disjoint.

Examples
Example 1 — Disjoint sets
set_a = {10, 20, 30}
set_b = {40, 50, 60}
print(set_a.isdisjoint(set_b))

Output: True

There are no common elements.

Example 2 — Not disjoint
set_a = {10, 20, 30}
set_b = {30, 40, 50}
print(set_a.isdisjoint(set_b))

Output: False

Both sets contain the element 30.

Example 3 — Empty set
set_a = {10, 20, 30}
set_b = set()
print(set_a.isdisjoint(set_b))

Output: True

An empty set has no elements, so it cannot share any with another set.

Points to Remember:
1. Two sets are disjoint if they have no common elements.
2. Use set_a.isdisjoint(set_b) to check whether two sets are disjoint.
3. The method returns a Boolean value: True or False.
4. True means there are no common elements.
5. False means at least one common element exists.
6. An empty set is disjoint from every set, including another empty set.
7. The method checks the sets without modifying them.

"""
# -----------------------------------
"""
Problem 17 
Given these sets:
set_a = {10, 20, 30, 40}
set_b = {50, 60, 70, 80}
set_c = {30, 40, 90, 100}

Write a program that:
1. Prints all three original sets.
2. Checks whether set_a and set_b are disjoint.
3. Checks whether set_a and set_c are disjoint.
4. Checks whether set_b and set_c are disjoint.
5. Prints every result using f-strings.
Expected results:
Check	Expected result
set_a.isdisjoint(set_b)	True
set_a.isdisjoint(set_c)	False
set_b.isdisjoint(set_c)	True
"""

print()

set_a = {10, 20, 30, 40}
set_b = {50, 60, 70, 80}
set_c = {30, 40, 90, 100}

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")
print(f"Original set of set_c: {set_c}")

print(f"set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}")
print(f"set_a.isdisjoint(set_c): {set_a.isdisjoint(set_c)}")
print(f"set_b.isdisjoint(set_c): {set_b.isdisjoint(set_c)}")

"""
Output of all:
Original set of set_a: {40, 10, 20, 30}
Original set of set_b: {80, 50, 60, 70}
Original set of set_c: {40, 90, 100, 30}
set_a.isdisjoint(set_b): True
set_a.isdisjoint(set_c): False
set_b.isdisjoint(set_c): True
"""

# ========================================

"""
Problem 18 — Disjoint Sets (Practice 2)

Given these sets:
set_a = {5, 10, 15, 20}
set_b = {25, 30, 35, 40}
set_c = {15, 20, 25, 30}
set_d = set()

Write a program that:
1. Prints all four original sets.
2. Checks whether set_a and set_b are disjoint.
3. Checks whether set_a and set_c are disjoint.
4. Checks whether set_b and set_c are disjoint.
5. Checks whether set_a and set_d are disjoint.
6. Prints every result using f-strings.
Expected results:
Check	Result
set_a.isdisjoint(set_b)	True
set_a.isdisjoint(set_c)	False
set_b.isdisjoint(set_c)	False
set_a.isdisjoint(set_d)	True
"""

print()

set_a = {5, 10, 15, 20}
set_b = {25, 30, 35, 40}
set_c = {15, 20, 25, 30}
set_d = set()

print(f"Original set of set_a: {set_a}")
print(f"Original set of set_b: {set_b}")
print(f"Original set of set_c: {set_c}")
print(f"Original set of set_d: {set_d}")

print(f"set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}")
print(f"set_a.isdisjoint(set_c): {set_a.isdisjoint(set_c)}")
print(f"set_b.isdisjoint(set_c): {set_b.isdisjoint(set_c)}")
print(f"set_a.isdisjoint(set_d): {set_a.isdisjoint(set_d)}")

"""
Output of all:
Original set of set_a: {10, 20, 5, 15}
Original set of set_b: {40, 25, 35, 30}
Original set of set_c: {25, 20, 30, 15}
Original set of set_d: set()
set_a.isdisjoint(set_b): True
set_a.isdisjoint(set_c): False
set_b.isdisjoint(set_c): False
set_a.isdisjoint(set_d): True
"""

# =============================================

# Modifying Sets with update()

"""
What does update() do?
The update() method adds multiple elements to an existing set from another iterable, such as a list, tuple, or another set.

Remember:
- It modifies the original set.
- Duplicate elements are automatically ignored.
- It can accept multiple iterables.
- It returns None, not the updated set.

Examples
Example 1 — Update with another set

set_a = {10, 20, 30}
set_b = {30, 40, 50}

set_a.update(set_b)
print(set_a)

Output: {10, 20, 30, 40, 50}

The duplicate 30 is included only once.

# ----------

Example 2 — Update with a list

numbers = {1, 2, 3}
new_numbers = [3, 4, 5, 6]

numbers.update(new_numbers)
print(numbers)

Output: {1, 2, 3, 4, 5, 6}

The set accepts elements from the list and ignores the repeated 3.

# -------------

Example 3 — Update with multiple iterables

numbers = {1, 2}
numbers.update([3, 4], (4, 5))
print(numbers)

Output: {1, 2, 3, 4, 5}

Both the list and tuple contribute elements to the set.
"""

"""
1. update() adds elements from one or more iterables to an existing set.
2. Syntax: set_a.update(iterable).
3. It can accept sets, lists, tuples, and other iterables.
4. Duplicate elements are automatically ignored.
5. It modifies the original set instead of creating a new set.
6. It can accept multiple iterables: set_a.update(list_a, tuple_a).
7. update() returns None, so don't assign its return value expecting the updated set.

add() vs update()

Method	    Purpose	                        Example
add()	    Add one element	                numbers.add(10)
update()	Add elements from an iterable	numbers.update([10, 20])

"""

# ====================

"""
Problem 19 — 
Focus: using update() with a list and handling duplicates.

Given:
numbers = {10, 20, 30, 40}
new_numbers = [30, 40, 50, 60, 70]

Write a program that:
1. Prints the original numbers set.
2. Prints the new_numbers list.
3. Uses update() to add the list's elements to the set.
4. Prints the updated set.
5. Prints the total number of unique elements using len().
6. Uses f-strings for every output statement.
Expected results:
- Updated set: {10, 20, 30, 40, 50, 60, 70}
- Total unique elements: 7
"""

print()

numbers = {10, 20, 30, 40}
new_numbers = [30, 40, 50, 60, 70]

print(f"Original numbers: {numbers}")
print(f"Original new_numbers: {new_numbers}")

numbers.update(new_numbers)

print(f"Updated set: {numbers}")
print(f"Total unique elements: {len(numbers)}")

"""
Output of all:
Original numbers: {40, 10, 20, 30}
Original new_numbers: [30, 40, 50, 60, 70]
Updated set: {70, 40, 10, 50, 20, 60, 30}
Total unique elements: 7
"""

# ====================================

"""
Problem 20 — Practise update() with a tuple

Given:
fruits = {"apple", "banana", "mango"}
new_fruits = ("mango", "orange", "grapes", "apple")

Write a program that:
1. Prints the original fruits set.
2. Prints the new_fruits tuple.
3. Uses update() to add the tuple's elements to the set.
4. Prints the updated set.
5. Prints the total number of unique fruits using len().
6. Prints the original tuple again to confirm it remains unchanged.
7. Uses f-strings for every output statement.

Expected results:
- Updated set contains: apple, banana, mango, orange, grapes
- Total unique fruits: 5
- Original tuple remains unchanged.
"""

print()

fruits = {"apple", "banana", "mango"}
new_fruits = ("mango", "orange", "grapes", "apple")

print(f"Original fruits: {fruits}")
print(f"Original new_fruits: {new_fruits}")

fruits.update(new_fruits)
print(f"Updated set contains: {fruits}")

print(f"Total unique fruits: {len(fruits)}")

print(f"Original fruits: {fruits}")
print(f"Original new_fruits: {new_fruits}")

"""
Output of all:
Original fruits: {'mango', 'banana', 'apple'}
Original new_fruits: ('mango', 'orange', 'grapes', 'apple')
Updated set contains: {'banana', 'apple', 'mango', 'orange', 'grapes'}
Total unique fruits: 5
Original fruits: {'banana', 'apple', 'mango', 'orange', 'grapes'}
Original new_fruits: ('mango', 'orange', 'grapes', 'apple')
"""

# =======================================

"""
Problem 21 — Set Operations Revision

Given:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Write a program that:
1. Prints both original sets.
2. Finds the common elements in both sets.
3. Finds all unique elements from both sets combined.
4. Finds elements present in set_a but not in set_b.
5. Counts the number of common elements.
6. Uses f-strings for every output statement.

Expected results (set display order may vary):
- Common elements: {30, 40, 50}
- Combined unique elements: {10, 20, 30, 40, 50, 60, 70}
- Elements in set_a but not set_b: {10, 20}
- Number of common elements: 3
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

print(f"Common elements: {set_a.intersection(set_b)}")
print(f"Combined unique elements: {set_a.union(set_b)}")
print(f"Elements in set_a but not set_b: {set_a.difference(set_b)}")
print(f"Number of common elements: {len(set_a.intersection(set_b))}")

"""
Output of all:
Original set_a: {50, 20, 40, 10, 30}
Original set_b: {50, 70, 40, 60, 30}
Common elements: {40, 50, 30}
Combined unique elements: {70, 40, 10, 50, 20, 60, 30}
Elements in set_a but not set_b: {10, 20}
Number of common elements: 3
"""

# ======================================

"""
Problem 22 — Set Relationships Revision

Given:
set_a = {10, 20}
set_b = {10, 20, 30, 40}
set_c = {50, 60}

Write a program that:
1. Prints all three original sets.
2. Checks whether set_a is a subset of set_b.
3. Checks whether set_b is a superset of set_a.
4. Checks whether set_a and set_c are disjoint.
5. Checks whether set_b is a subset of set_a.
6. Uses f-strings for every output statement.

Expected results:
- set_a is a subset of set_b: True
- set_b is a superset of set_a: True
- set_a and set_c are disjoint: True
- set_b is a subset of set_a: False
"""

print()

set_a = {10, 20}
set_b = {10, 20, 30, 40}
set_c = {50, 60}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")
print(f"Original set_c: {set_c}")

print(f"set_a is a subset of set_b: {set_a.issubset(set_b)}")
print(f"set_b is a superset of set_a: {set_b.issuperset(set_a)}")
print(f"set_a and set_c are disjoint: {set_a.isdisjoint(set_c)}")
print(f"set_b is a subset of set_a: {set_b.issubset(set_a)}")

"""
Output of all:
Original set_a: {10, 20}
Original set_b: {40, 10, 20, 30}
Original set_c: {50, 60}
set_a is a subset of set_b: True
set_b is a superset of set_a: True
set_a and set_c are disjoint: True
set_b is a subset of set_a: False
"""

# ===========================================

"""
Problem 23 — Mixed Set Operations Revision

Given:
set_a = {5, 10, 15, 20, 25}
set_b = {15, 20, 25, 30, 35}
set_c = {10, 30, 40}

Write a program that:
1. Prints all three original sets.
2. Finds the common elements between set_a and set_b.
3. Finds the elements present in set_a but not in set_c.
4. Finds the elements that are in either set_b or set_c,
   but not in both.
5. Checks whether set_a and set_c are disjoint.
6. Prints the total number of unique elements in the union
   of all three sets.
7. Uses f-strings for every output statement.
"""

print()

set_a = {5, 10, 15, 20, 25}
set_b = {15, 20, 25, 30, 35}
set_c = {10, 30, 40}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")
print(f"Original set_c: {set_c}")

print(f"Common elements of set_a and set_b: {set_a.intersection(set_b)}")
print(f"set_a but not set_c: {set_a.difference(set_c)}")
print(f"Symmetric difference of set_b and set_c: {set_b ^ set_c}")
print(f"Are set_a and set_c disjoint? {set_a.isdisjoint(set_c)}")
print(f"Total unique elements across all three sets: {len(set_a.union(set_b).union(set_c))}")

"""
Output of all:
Original set_a: {20, 5, 25, 10, 15}
Original set_b: {35, 20, 25, 30, 15}
Original set_c: {40, 10, 30}
Common elements of set_a and set_b: {25, 20, 15}
set_a but not set_c: {25, 20, 5, 15}
Symmetric difference of set_b and set_c: {35, 40, 10, 15, 20, 25}
Are set_a and set_c disjoint? False
Total unique elements across all three sets: 8
"""

# ===============================================

# Assignment vs. Copying

# Assignement example:

"""

set_a = {10, 20, 30}
set_b = set_a

set_b.add(40)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

Output:
Set A: {10, 20, 30, 40}
Set B: {10, 20, 30, 40}

Why did set_a change when we added 40 through set_b? Because both variables refer to the same set object.
set_a and set_b

Two variable names

One set object
{10, 20, 30, 40}

Changing the set through either variable affects the same object.

# ==================

2. How do we create a genuinely separate set?
Use the copy() method.

set_a = {10, 20, 30}

set_b = set_a.copy()
set_b.add(40)

print(f"Set A: {set_a}")print(f"Set B: {set_b}")

Output:
Set A: {10, 20, 30}
Set B: {10, 20, 30, 40}

Now set_b is a separate set, so adding an element to it doesn't change set_a.

"""

# Imp Notes:

"""
- set_b = set_a → Both variables refer to the same set.
- set_b = set_a.copy() → Creates a separate, shallow copy of the set.
- Changing the membership of one copied set doesn't change the membership of the other.
- copy() does not modify the original set.

Important: copy() is a shallow copy. If a set contains mutable objects indirectly through its elements,
their shared references may matter. In ordinary sets of numbers or strings, the distinction above is straightforward.
"""

# ==============================

"""
Problem 24 — Assignment vs. Copying Sets

Given:
set_a = {10, 20, 30}

Write a program that:
1. Prints set_a.
2. Assigns set_a to set_b and adds 40 to set_b.
3. Prints both sets.
4. Creates set_c using set_a.copy().
5. Adds 50 to set_c.
6. Prints set_a and set_c.
7. Uses f-strings for every output statement.
"""

print()

set_a = {10, 20, 30}

print(f"Original set_a: {set_a}")                     # {10, 20, 30}

set_b = set_a                                         # Assigning set

set_b.add(40)

print(f"After updating set_b, set_a: {set_a}")                        # {40, 10, 20, 30}
print(f"After updating set_b, set_b: {set_b}")                       # {40, 10, 20, 30}

set_c = set_a.copy()                # copy set 
set_c.add(50)

print(f"After updating set_c, set_a: {set_a}")                       # {40, 10, 20, 30}
print(f"After updating set_c, set_c: {set_c}")                      # {40, 10, 50, 20, 30}

"""
Out of all:
Original set_a: {10, 20, 30}
After updating set_b, set_a: {40, 10, 20, 30}
After updating set_b, set_b: {40, 10, 20, 30}
After updating set_c, set_a: {40, 10, 20, 30}
After updating set_c, set_c: {40, 10, 50, 20, 30}
"""

# =========================================

"""
Problem 25 — Copying and Modifying Sets

Given:
numbers = {5, 10, 15, 20}

Write a program that:
1. Prints the original numbers set.
2. Assigns numbers to another variable called alias_numbers.
3. Adds 25 to alias_numbers.
4. Prints both numbers and alias_numbers.
5. Creates an independent copy called copied_numbers.
6. Adds 30 to copied_numbers.
7. Removes 5 from copied_numbers.
8. Prints numbers and copied_numbers.
9. Prints the length of both sets.
10. Uses f-strings for every output statement.
"""

print()

numbers = {5, 10, 15, 20}

print(f"Original numbers set: {numbers}")

alias_numbers = numbers

alias_numbers.add(25)

print(f"After updating alias_numbers, numbers: {numbers}")
print(f"After updating alias_numbers, alias_numbers: {alias_numbers}")

copied_numbers = numbers.copy()

copied_numbers.add(30)

copied_numbers.remove(5)

print(f"After updating copied_numbers, numbers: {numbers}")
print(f"After updating copied_numbers, copied_numbers: {copied_numbers}")

print(f"The length of numbers: {len(numbers)}")
print(f"The length of copied_numbers: {len(copied_numbers)}")

"""
Output of all:
Original numbers set: {10, 20, 5, 15}
After updating alias_numbers, numbers: {5, 10, 15, 20, 25}
After updating alias_numbers, alias_numbers: {5, 10, 15, 20, 25}
After updating copied_numbers, numbers: {5, 10, 15, 20, 25}
After updating copied_numbers, copied_numbers: {20, 25, 10, 30, 15}
The length of numbers: 5
The length of copied_numbers: 5
"""

# =================================================

# Problem : 26 to 34 - Set Comprehension:

# ================================================

# Remaining set methods and special cases

# In-place set operations - intersection_update()

"""
intersection_update()
We already know that intersection() finds the common elements between sets and returns a new set.

But intersection_update() behaves differently:
 it modifies the original set, keeping only the elements that are common to both sets.

Example:

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

set_a.intersection_update(set_b)

print(set_a)

Output:
{30, 40}

Notice that set_a itself has changed. The values 10 and 20 were removed because they weren't present in set_b.
The original set_b remains unchanged.

Remember the difference
Method	                                    What happens?
set_a.intersection(set_b)	                Returns a new set; set_a stays unchanged.
set_a.intersection_update(set_b)	        Modifies set_a directly.

The same general distinction applies to other in-place operations, such as difference_update() and symmetric_difference_update().
"""

# ==============================

"""
Problem 35 — Intersection Update

Given the following sets:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Write a program that:
1. Prints both original sets.
2. Uses intersection_update() on set_a with set_b.
3. Prints the modified set_a.
4. Prints set_b to show that it remains unchanged.
5. Uses f-strings for every output statement.
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

set_a.intersection_update(set_b)

print(f"The modified set_a: {set_a}")
print(f"{set_b} - set_b remains unchanged")

"""
Output of all:
Original set_a: {50, 20, 40, 10, 30}
Original set_b: {50, 70, 40, 60, 30}
The modified set_a: {40, 50, 30}
{50, 70, 40, 60, 30} - set_b remains unchanged
"""

# ======================================

"""
Problem 36 — Difference Update

Given the following sets:
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

Write a program that:
1. Prints both original sets.
2. Uses difference_update() on set_a with set_b.
3. Prints the modified set_a.
4. Prints set_b to show that it remains unchanged.
5. Uses f-strings for every output statement.
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

set_a.difference_update(set_b)

print(f"The modified set_a: {set_a}")

print(f"set_b remains unchanged - {set_b}")

"""
Output:
Original set_a: {50, 20, 40, 10, 30}
Original set_b: {50, 70, 40, 60, 30}
The modified set_a: {20, 10}
set_b remains unchanged - {50, 70, 40, 60, 30}
"""

# ======================================

# symmetric_difference_update()

"""
- symmetric_difference() returns a new set containing elements that exist in either set, but not in both.
- symmetric_difference_update() performs the same operation but modifies the original set.
In simple words, it keeps the elements that are unique to either set and removes the elements common to both.

Example 1 - Understand the result

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

set_a.symmetric_difference_update(set_b)

print(set_a)
print(set_b)

Final result
- set_a becomes {10, 20, 50, 60}
- set_b remains {30, 40, 50, 60}

Notice that only set_a changes. The second set is used for comparison but remains unchanged.

# --------------------

Example 2 — Compare the two methods

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)

print(f"Original set_a: {set_a}")
print(f"New result: {result}")

Original set_a: {1, 2, 3, 4}
New result: {1, 2, 5, 6}

set_a.symmetric_difference_update(set_b)

Here, set_a itself becomes {1, 2, 5, 6}. There is no need to assign the method's return value to a variable;
the update method modifies the set in place and returns None.

# ---------------------

Important notes 📝
Remember these four points:
1. Common elements are removed from the resulting set.
2. Unique elements from both sets are kept.
3. symmetric_difference_update() modifies the set before the dot, not the argument set.
4. Set display order is not guaranteed, so don't worry if your output order differs.
"""

# ===========================================

"""
Problem 37 🐍
Now it's your turn! Write the code yourself, just as you've been doing in our previous exercises.

Problem statement:

Given the two sets below:
set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

Write a Python program that:
1. Prints both original sets.
2. Applies symmetric_difference_update() to set_a using set_b.
3. Prints the modified set_a.
4. Prints set_b to demonstrate that it remains unchanged.
"""

print()

set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

set_a.symmetric_difference_update(set_b)

print(f"The modified set_a: {set_a}")
print(f"The set_b remains unchanged: {set_b}")

"""
Output:
Original set_a: {50, 20, 40, 10, 30}
Original set_b: {80, 50, 70, 40, 60}
The modified set_a: {80, 20, 70, 10, 60, 30}
The set_b remains unchanged: {80, 50, 70, 40, 60}
"""

# =========================================

"""
Problem 38

Given the following sets:
set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 30, 35, 40}

Write a Python program that:
1. Prints both original sets.
2. Applies symmetric_difference_update() to set_a using set_b.
3. Prints the modified set_a.
4. Prints set_b to confirm it remains unchanged.
5. Prints the length of the modified set_a using len().
"""

print()

set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 30, 35, 40}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

set_a.symmetric_difference_update(set_b)
# In this the element which is the commom elements will get removed from both and the remaining elements of both will come in set_a

"""
In set_a = {5, 10, 15, 20, 25, 30}  - This are original elements of set_a
In set_b = {35, 20, 40, 30, 15} - This are the original elements of set_b

so now in this both commom elements are - 20, 30 and 15 so that will get remove from set_a and remaining elements of set_a
as well as the remaining elements of set_b will come 

so the final result will be set_a = {5, 10, 25, 35, 40} 
"""

print(f"The modified set_a: {set_a}")
print(f"The set_b remains unchanged: {set_b}")
print(f"The length of the modified set_a: {len(set_a)}")

"""
Output:
Original set_a: {20, 5, 25, 10, 30, 15}
Original set_b: {35, 20, 40, 30, 15}
The modified set_a: {35, 5, 40, 25, 10}
The set_b remains unchanged: {35, 20, 40, 30, 15}
The length of the modified set_a: 5
"""

# ================================================

print()

set_a = {5, 10, 15, 20, 25, 30}
set_b = {15, 20, 30, 35, 40}

print(f"Original set_a: {set_a}")
print(f"Original set_b: {set_b}")

set_a.difference_update(set_b)
# In this it removes that elements from set_a which is there is set_b and the remaining element will be come in final output.

"""
In set_a = {5, 10, 15, 20, 25, 30}  - This are original elements of set_a
In set_b = {35, 20, 40, 30, 15} - This are the original elements of set_b

so now in this both commom elements are - 20, 30 and 15 so that will get remove from set_a and remaining
elements will come as final output: set_a = {5, 10, 25}
"""

print(f"The modified set_a: {set_a}")     
print(f"The set_b remains unchanged: {set_b}")
print(f"The length of the modified set_a: {len(set_a)}")

"""
Output:
Original set_a: {20, 5, 25, 10, 30, 15}
Original set_b: {35, 20, 40, 30, 15}
The modified set_a: {5, 25, 10}    
The set_b remains unchanged: {35, 20, 40, 30, 15}
The length of the modified set_a: 3
"""

# =======================================================

# Python Set - pop()

"""
What is pop()?
The pop() method removes an arbitrary element from a set and returns the removed element.

Syntax:
set_name.pop()

There are two important actions here:
1. An element is removed from the original set.
2. The removed element is returned, so you can store it in a variable or print it.
Unlike lists, sets are unordered. Therefore, pop() does not guarantee which element it will remove.

Example 1 — Remove and return an element
numbers = {10, 20, 30, 40, 50}

removed_element = numbers.pop()
print(f"Removed element: {removed_element}")
print(f"Remaining set: {numbers}")

One possible output is:
Removed element: 40
Remaining set: {10, 20, 30, 50}

Your output may show a different removed element. That's completely fine!

Notice that the removed element is stored in removed_element.
The remaining set contains every original element except the one removed.

# ----------------------- #

3. Example 2 — Print the returned element directly

fruits = {"apple", "banana", "mango"}
print(f"Removed fruit: {fruits.pop()}")
print(f"Remaining fruits: {fruits}")

Possible output:
Removed fruit: banana
Remaining fruits: {'apple', 'mango'}

Again, banana is just an example.
Python does not promise that it will remove that particular fruit.

# ----------------------- #

4. Example 3 — What happens with an empty set?
numbers = set()numbers.pop()

This raises a KeyError because there is no element to remove.

If you need to handle this situation safely, check whether the set is non-empty before calling pop():
numbers = set() if numbers: print(f"Removed element: {numbers.pop()}") else: print("The set is empty.")

Output:
The set is empty. 

# ----------------------- #

5. Important notes 📝
Method	                        What it does
add()	                        Adds one element
remove(x)	                    Removes a specified element; raises KeyError if absent
discard(x)	                    Removes a specified element if present
pop()	                        Removes and returns an arbitrary element
clear()	                        Removes all elements

Remember these rules:
- pop() modifies the original set.
- It returns the removed element.
- It takes no element argument: numbers.pop() is correct, while numbers.pop(10) is invalid.
- Calling it on an empty set raises KeyError.
- Don't rely on a particular removal order.
"""

# ==============================================

"""
Problem 39:

Given the following set:
numbers = {10, 20, 30, 40, 50, 60}

Write a Python program that:
1. Prints the original set.
2. Uses pop() to remove one element and stores the returned element in a variable called removed_element.
3. Prints the removed element.
4. Prints the remaining set.
5. Prints the length of the remaining set using len().
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string output messages.
- An output comment showing a valid possible result.
- A separator at the end.
"""

print()

numbers = {10, 20, 30, 40, 50, 60}

print(f"The original set of numbers: {numbers}")

removed_element = numbers.pop()

print(f"The removed element: {removed_element}")

print(f"The remaining set: {numbers}")  # Here the removed the element will not come 

print(f"The length of the remaining set: {len(numbers)}")

"""
Final Output:
The original set of numbers: {50, 20, 40, 10, 60, 30}
The removed element: 50
The remaining set: {20, 40, 10, 60, 30}
The length of the remaining set: 5
"""

# ==============================================

"""
Problem 40:

Given the following set:
fruits = {"apple", "banana", "mango", "orange", "grapes"}

Write a Python program that:
1. Prints the original set.
2. Uses pop() to remove one element and stores it in a variable named removed_fruit.
3. Prints the removed fruit.
4. Uses pop() a second time and stores the returned element in a variable named second_removed_fruit.
5. Prints the second removed fruit.
6. Prints the final remaining set.
7. Prints the number of remaining fruits using len().
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string output messages.
- An output comment showing a valid possible result.
- A separator at the end.
"""

print()

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(f"The original set of fruits: {fruits}")

removed_fruit = fruits.pop()

print(f"The removed fruit: {removed_fruit}")

second_removed_fruit = fruits.pop()

print(f"The second removed fruit: {second_removed_fruit}")

print(f"The final remaining set of fruits: {fruits}")

print(f"The number of remaining fruits: {len(fruits)}")

"""
Final Output:
The original set of fruits: {'mango', 'orange', 'apple', 'grapes', 'banana'}
The removed fruit: mango
The second removed fruit: orange
The final remaining set of fruits: {'apple', 'grapes', 'banana'}
The number of remaining fruits: 3
"""

# ==========================================

# clear() in Python Sets

"""
1. What is clear()?
The clear() method removes all elements from an existing set, leaving it empty.
Syntax
set_name.clear()

Remember: clear() modifies the original set. It does not delete the variable itself.

2. Example 1 — Clear a set
numbers = {10, 20, 30, 40, 50}
print(f"Original set: {numbers}")
numbers.clear()
print(f"After clear(): {numbers}")
print(f"Number of elements: {len(numbers)}")

Output:
Original set: {50, 20, 40, 10, 30}
After clear(): set()
Number of elements: 0

The set becomes set(), and its length becomes 0.

# --------------------

3. Example 2 — The variable still exists
fruits = {"apple", "banana", "mango"}
fruits.clear()
print(f"Fruits after clearing: {fruits}")
fruits.add("orange")
print(f"Fruits after adding an element: {fruits}")

Output:
Fruits after clearing: set()
Fruits after adding an element: {'orange'}

Even after clearing the set, we can use the same variable again and add new elements to it.

# -------------------------

4. Example 3 — clear() versus assigning an empty set
These two approaches both leave numbers empty, but they behave differently when another variable refers to the same set.
numbers = {1, 2, 3}
alias = numbersnumbers.clear()
print(f"numbers: {numbers}")
print(f"alias: {alias}")

Output:
numbers: set()
alias: set()

Why? Both variables refer to the same set object, and clear() modifies that shared object.

Compare this with:
numbers = {1, 2, 3}
alias = numbers
numbers = set()
print(f"numbers: {numbers}")
print(f"alias: {alias}")

Output:
numbers: set()
alias: {1, 2, 3}

Here, numbers = set() reassigns numbers to a new empty set. The original set still exists through alias.

# ----------------------------

5. Important notes 📝
Method or operation	                            Effect
numbers.clear()	                                Removes all elements from the existing set
numbers = set()	                                Assigns a new empty set to numbers
len(numbers) after clearing                 	Returns 0
numbers.clear() return value	                None

Also, clear() does not take an element argument. It empties the whole set, unlike remove(), discard(), and pop().
"""

# ==============================================

"""
Problem 41

Given the following set:
numbers = {10, 20, 30, 40, 50, 60}

Write a Python program that:
1. Prints the original set.
2. Prints its original length using len().
3. Uses clear() to remove all elements.
4. Prints the modified set.
5. Prints the length of the modified set.
6. Adds 100 to the same set using add().
7. Prints the set again to demonstrate that it can be reused.
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string output messages.
- An output comment showing a valid possible result.
- A separator at the end.
"""

print()

numbers = {10, 20, 30, 40, 50, 60}

print(f"The original set of numbers: {numbers}")

print(f"The length of the original set of numbers: {len(numbers)}")

numbers.clear()

print(f"The modified set of numbers: {numbers}")

print(f"The length of the modified set of numbers: {len(numbers)}")

numbers.add(100)

print(f"The set of numbers can be resued: {numbers}")

"""
Final Output:
The original set of numbers: {50, 20, 40, 10, 60, 30}
The length of the original set of numbers: 6
The modified set of numbers: set()
The length of the modified set of numbers: 0
The set of numbers can be resued: {100}
"""

# ============================================

"""
Problem 42

Given the following code setup:
fruits = {"apple", "banana", "mango", "orange"}
alias = fruits

Write a Python program that:
1. Prints the original fruits set.
2. Prints the original alias set.
3. Uses fruits.clear() to empty the set.
4. Prints fruits after clearing.
5. Prints alias after clearing.
6. Adds "grapes" to alias using add().
7. Prints both fruits and alias again.
8. Prints the length of both sets.
"""

print()

fruits = {"apple", "banana", "mango", "orange"}
alias = fruits

print(f"The original set of fruits: {fruits}")

print(f"The original set of alias: {alias}")

fruits.clear()

print(f"fruits after clearing: {fruits}")

print(f"alias after clearing: {alias}")

alias.add("grapes")

print(f"After add element in alias, fruits: {fruits}")

print(f"After add element in alias, alias: {alias}")

print(f"The length of fruits: {len(fruits)}")

print(f"The length of alias: {len(alias)}")

"""
Final Output:
The original set of fruits: {'apple', 'banana', 'mango', 'orange'}
The original set of alias: {'apple', 'banana', 'mango', 'orange'}
fruits after clearing: set()
alias after clearing: set()
After add element in alias, fruits: {'grapes'}
After add element in alias, alias: {'grapes'}
The length of fruits: 1
The length of alias: 1
"""

# ===============================================

# frozenset: Creation and Properties

"""
1. What is a frozenset?
A frozenset is an immutable version of a Python set.

You already know that a normal set is mutable, which means we can add or remove elements after creating it.

But a frozenset cannot be modified after creation.

In simple words:
- set → Mutable (can be changed).
- frozenset → Immutable (cannot be changed).

2. How to create a frozenset

The syntax is:
frozenset(iterable)

We can create a frozenset using a list, tuple, string, or another iterable.

# ------------------------------

Example 1 — Create a frozenset from a list

numbers = [10, 20, 30, 40, 50]
frozen_numbers = frozenset(numbers)
print(f"Original list: {numbers}")
print(f"Frozenset: {frozen_numbers}")
print(f"Type: {type(frozen_numbers)}")

Possible output:
Original list: [10, 20, 30, 40, 50]
Frozenset: frozenset({40, 10, 50, 20, 30})
Type: <class 'frozenset'>

# Notice that the result is a frozenset, not a regular set.

# ------------------------------

Example 2 — Create a frozenset from a tuple

fruits = ("apple", "banana", "mango", "apple")
frozen_fruits = frozenset(fruits)
print(f"Original tuple: {fruits}")
print(f"Frozenset: {frozen_fruits}")
print(f"Length: {len(frozen_fruits)}")

Possible output:
Original tuple: ('apple', 'banana', 'mango', 'apple')
Frozenset: frozenset({'apple', 'banana', 'mango'})
Length: 3

# Notice something important: the duplicate "apple" is automatically removed.

# Just like normal sets, frozensets contain unique elements.

# ---------------------------------------

Example 3 — Create an empty frozenset

empty_frozen_set = frozenset()
print(f"Empty frozenset: {empty_frozen_set}")
print(f"Type: {type(empty_frozen_set)}")

Output:
Empty frozenset: frozenset()
Type: <class 'frozenset'>

Remember:
empty_set = set()
empty_frozen_set = frozenset()

# These create two different types of empty collections.

# ---------------------------------------

3. Why is frozenset immutable?

Let's compare a regular set and a frozenset.

Example 4 — Regular set versus frozenset

numbers = {10, 20, 30}
numbers.add(40)
print(f"Modified set: {numbers}")

This works because a regular set is mutable.

But:
frozen_numbers = frozenset({10, 20, 30})
frozen_numbers.add(40)

This raises:
AttributeError: 'frozenset' object has no attribute 'add'

Why?

Because a frozenset does not support methods that modify its contents.

Similarly, you cannot use:
- add()
- update()
- remove()
- discard()
- pop()
- clear()
These methods are unavailable for frozensets.

# -----------------------------------------

# Important properties of frozenset 📝

1. Immutable: Cannot add, remove, or modify elements after creation.
2. Unique: Duplicate elements are automatically removed.
3. Unordered: Elements do not have a guaranteed display order.
4. Iterable: You can loop through a frozenset.
5. Hashable: A frozenset can be used as a dictionary key or as an element inside another set, provided its elements are hashable.
6. Supports set operations: Union, intersection, difference, and symmetric difference are supported.

# One important detail: frozenset elements must be hashable, just like regular set elements.
For example, a list cannot be an element of a frozenset.

# -------------------------------------

## Set versus Frozenset

#Feature	        #set	            #frozenset
Mutable	            Yes	                No
Immutable	        No	                Yes
Duplicate elements	Not allowed	        Not allowed
Unordered	        Yes	                Yes
add()	            Yes	                No
remove()	        Yes	                No
clear()	            Yes	                No
Set operations	    Yes	                Yes
Hashable	        No	                Yes, if elements are hashable

"""

# ==========================================

"""
Problem 43

Given the following list:
numbers = [10, 20, 30, 20, 40, 50, 30, 60]

Write a Python program that:
1. Prints the original list.
2. Creates a frozenset from the list and stores it in frozen_numbers.
3. Prints the frozenset.
4. Prints its type using type().
5. Prints its length using len().
6. Prints the original list again to demonstrate that it remains unchanged.
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string output messages.
- Output comment showing a valid possible result.
- Separator at the end.
"""

print()

numbers = [10, 20, 30, 20, 40, 50, 30, 60]

print(f"The original list of numbers: {numbers}")

frozen_numbers = frozenset(numbers)

print(f"The frozenset: {frozen_numbers}")

print(f"The data type of frozen_numbers: {type(frozen_numbers)}")

print(f"The length of frozen_numbers: {len(frozen_numbers)}")

print(f"The original list of numbers remains unchanged: {numbers}")

"""
Final Output:
The original list of numbers: [10, 20, 30, 20, 40, 50, 30, 60]
The frozenset: frozenset({40, 10, 50, 20, 60, 30})
The data type of frozen_numbers: <class 'frozenset'>
The length of frozen_numbers: 6
The original list of numbers remains unchanged: [10, 20, 30, 20, 40, 50, 30, 60]
"""

# ============================================

"""
Problem 44

Given the following tuple:
fruits = ("apple", "banana", "mango", "apple", "orange", "banana")

Write a Python program that:
1. Prints the original tuple.
2. Creates a frozenset from the tuple and stores it in frozen_fruits.
3. Prints the frozenset.
4. Prints its length using len().
5. Iterates through the frozenset using a for loop and prints each fruit.
6. Demonstrates that the original tuple remains unchanged.
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string output messages.
- Output comment showing a valid possible result.
- Separator at the end.
"""

print()

fruits = ("apple", "banana", "mango", "apple", "orange", "banana")

print(f"The original tuple of fruits: {fruits}")

frozen_fruits = frozenset(fruits)

print(f"The frozenset: {frozen_fruits}")

print(f"The length of frozen_fruits: {len(frozen_fruits)}")

print(f"The frozen_fruits:")
for frozen_fruit in frozen_fruits:
    print(frozen_fruit)

print(f"The original tuple of fruits remains unchanged: {fruits}")

"""
Final Output:
The original tuple of fruits: ('apple', 'banana', 'mango', 'apple', 'orange', 'banana')
The frozenset: frozenset({'apple', 'orange', 'banana', 'mango'})
The length of frozen_fruits: 4
The frozen_fruits:
apple
orange
banana
mango
The original tuple of fruits remains unchanged: ('apple', 'banana', 'mango', 'apple', 'orange', 'banana')
"""

# ========================================================

# Operations involving frozensets

"""
Although frozensets are immutable, they still support set operations!

1. Union — .union() or |
Combines all unique elements from both frozensets.
frozen_a = frozenset({10, 20, 30, 40})
frozen_b = frozenset({30, 40, 50, 60})
result = frozen_a.union(frozen_b)
print(result)

Possible output:
frozenset({10, 20, 30, 40, 50, 60})

# -----------------------------

2. Intersection — .intersection() or &
Returns only the elements common to both frozensets.

result = frozen_a.intersection(frozen_b)

Possible output:
frozenset({30, 40})

# -------------------------------

3. Difference — .difference() or -
Returns elements present in the first frozenset but not in the second.
result = frozen_a.difference(frozen_b)

Possible output:
frozenset({10, 20})

Remember: difference is directional. Reversing the operands can produce a different result.

# -------------------------------

4. Symmetric difference — .symmetric_difference() or ^

Returns elements that are in either frozenset, but not in both.

result = frozen_a.symmetric_difference(frozen_b)

Possible output:
frozenset({10, 20, 50, 60})

# ---------------------------------

5. What makes frozenset different?

Operation	                            Supported?
union()	                                Yes
intersection()	                        Yes
difference()	                        Yes
symmetric_difference()	                Yes
issubset() / issuperset()	            Yes
isdisjoint()	                        Yes
add() / update()	                    No
remove() / discard()	                No
pop() / clear()	                        No
intersection_update()	                No
difference_update()	                    No
symmetric_difference_update()	        No

Key point: These operations create a result; they do not modify the original frozensets.
With two frozenset operands, the results are also frozensets.

"""

# ===========================================

"""
Problem 45 — Frozenset mathematical operations
Create two frozensets:
frozen_a = frozenset({10, 20, 30, 40, 50})
frozen_b = frozenset({30, 40, 50, 60, 70})

Write a program that:
1. Prints both original frozensets.
2. Performs union using .union().
3. Performs intersection using &.
4. Performs difference using .difference().
5. Performs symmetric difference using ^.
6. Prints all four results.
7. Prints the type of each result using type().
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string messages.
- Output comment showing a valid possible result.
- Separator at the end.
"""

print()

frozen_a = frozenset({10, 20, 30, 40, 50})
frozen_b = frozenset({30, 40, 50, 60, 70})

print(f"The original frozen set of frozen_a: {frozen_a}")
print(f"The original frozen set of frozen_b: {frozen_b}")

print()

result_union = frozen_a.union(frozen_b)

result_intersection = frozen_a & frozen_b

result_difference = frozen_a.difference(frozen_b)

result_symmetric_difference = frozen_a ^ frozen_b

print(f"Result of union: {result_union}")
print(f"Result of intersection: {result_intersection}")
print(f"Result of difference: {result_difference}")
print(f"Result of symmetric difference: {result_symmetric_difference}")

print()
print(f"The data type of each result:")
print(f"Result of union: {type(result_union)}")
print(f"Result of intersection: {type(result_intersection)}")
print(f"Result of difference: {type(result_difference)}")
print(f"Result of symmetric difference: {type(result_symmetric_difference)}")

"""
Final Output:
The original frozen set of frozen_a: frozenset({50, 20, 40, 10, 30})
The original frozen set of frozen_b: frozenset({50, 70, 40, 60, 30})

Result of union: frozenset({70, 40, 10, 50, 20, 60, 30})
Result of intersection: frozenset({40, 50, 30})
Result of difference: frozenset({10, 20})
Result of symmetric difference: frozenset({20, 70, 10, 60})

The data type of each result:
Result of union: <class 'frozenset'>
Result of intersection: <class 'frozenset'>)
Result of difference: <class 'frozenset'>
Result of symmetric difference: <class 'frozenset'>
"""

# ==========================================

"""
Problem 46 — Frozenset relationships and immutability

Given:
frozen_a = frozenset({10, 20, 30})
frozen_b = frozenset({10, 20, 30, 40, 50})
frozen_c = frozenset({60, 70})

Write a program that:
1. Prints all three original frozensets.
2. Checks whether frozen_a is a subset of frozen_b.
3. Checks whether frozen_b is a superset of frozen_a.
4. Checks whether frozen_a and frozen_c are disjoint.
5. Creates a new frozenset using the union of frozen_a and frozen_c.
6. Prints the new result and its type.
7. Prints all three original frozensets again to demonstrate that they remain unchanged.
Follow your usual format:
- Blank print() at the beginning.
- Clear f-string messages.
- Output comment showing a valid possible result.
- Separator at the end.
"""

print()

frozen_a = frozenset({10, 20, 30})
frozen_b = frozenset({10, 20, 30, 40, 50})
frozen_c = frozenset({60, 70})

print(f"The original frozen set of frozen_a: {frozen_a}")
print(f"The original frozen set of frozen_b: {frozen_b}")
print(f"The original frozen set of frozen_c: {frozen_c}")

print()

print(f"frozen_a is a subset of frozen_b: {frozen_a.issubset(frozen_b)}")
print(f"frozen_b is a superset of frozen_a: {frozen_b.issuperset(frozen_a)}")
print(f"frozen_a and frozen_c are disjoint: {frozen_a.isdisjoint(frozen_c)}")

print()

result_union = frozen_a.union(frozen_c)

print(f"The union of frozen_a and frozen_c: {result_union}")

print(f"The type of result of union: {type(result_union)}")

print()

print(f"The original frozensets remain unchanged:")
print(f"The original frozen set of frozen_a: {frozen_a}")
print(f"The original frozen set of frozen_b: {frozen_b}")
print(f"The original frozen set of frozen_c: {frozen_c}")

"""
Final Output:
The original frozen set of frozen_a: frozenset({10, 20, 30})
The original frozen set of frozen_b: frozenset({50, 20, 40, 10, 30})
The original frozen set of frozen_c: frozenset({60, 70})

frozen_a is a subset of frozen_b: True
frozen_b is a superset of frozen_a: True
frozen_a and frozen_c are disjoint: True

The union of frozen_a and frozen_c: frozenset({20, 70, 10, 60, 30})
The type of result of union: <class 'frozenset'>

The original frozensets remain unchanged:
The original frozen set of frozen_a: frozenset({10, 20, 30})
The original frozen set of frozen_b: frozenset({50, 20, 40, 10, 30})
The original frozen set of frozen_c: frozenset({60, 70})
"""

# ==========================================