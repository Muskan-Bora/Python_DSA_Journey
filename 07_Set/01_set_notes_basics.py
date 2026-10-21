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

