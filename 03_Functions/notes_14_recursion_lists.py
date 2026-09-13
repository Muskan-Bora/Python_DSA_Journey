# ======================================================================

"""
=========================================================
RECURSION WITH LISTS
=========================================================

Recursion can also be used to process elements of a list
one by one.

The basic idea is:

1. Process the current element.
2. Recursively process the remaining list.
3. Stop when there are no elements left.

---------------------------------------------------------
GENERAL STRUCTURE
---------------------------------------------------------

def function(items):

    if len(items) == 0:
        return

    # Process current element

    function(items[1:])


---------------------------------------------------------
BASE CASE
---------------------------------------------------------

The recursion should stop when the list becomes empty.

Example:

if len(items) == 0:
    return

Why?

Because eventually:

[10, 20, 30]
[20, 30]
[30]
[]

At [] there is nothing left to process.


---------------------------------------------------------
CURRENT ELEMENT
---------------------------------------------------------

The first element of the list can be accessed using:

items[0]

Example:

numbers = [10, 20, 30]

numbers[0] -> 10


---------------------------------------------------------
REMAINING LIST
---------------------------------------------------------

The remaining elements can be obtained using:

items[1:]

Example:

numbers = [10, 20, 30]

numbers[1:] -> [20, 30]

Then:

[20, 30]
[30]
[]


---------------------------------------------------------
BASIC FLOW
---------------------------------------------------------

For:

numbers = [10, 20, 30]

The recursive calls become:

function([10, 20, 30])
        ↓
function([20, 30])
        ↓
function([30])
        ↓
function([])
        ↓
STOP


---------------------------------------------------------
PROCESSING BEFORE RECURSION
---------------------------------------------------------

If we process items[0] BEFORE the recursive call,
the list is processed from LEFT TO RIGHT.

Example:

def print_items(items):

    if len(items) == 0:
        return

    print(items[0])
    print_items(items[1:])


Output:

10
20
30


---------------------------------------------------------
PROCESSING AFTER RECURSION
---------------------------------------------------------

If we process items[0] AFTER the recursive call,
the list is processed from RIGHT TO LEFT.

Example:

def print_items(items):

    if len(items) == 0:
        return

    print_items(items[1:])
    print(items[0])


Output:

30
20
10


---------------------------------------------------------
IMPORTANT MENTAL MODEL
---------------------------------------------------------

For every recursive list problem, ask:

1. What is my BASE CASE?
2. What is my CURRENT ELEMENT?
3. What is my SMALLER LIST?
4. What should happen BEFORE recursion?
5. What should happen AFTER recursion?


---------------------------------------------------------
IMPORTANT PATTERN
---------------------------------------------------------

Current element:

items[0]

Remaining list:

items[1:]

Base case:

len(items) == 0


---------------------------------------------------------
KEY IDEA
---------------------------------------------------------

Recursion with lists follows the same fundamental pattern
as recursion with strings.

String:

text[0]
text[1:]

List:

items[0]
items[1:]

The difference is only the data type.
The recursive thinking remains the same.
"""

# ============================================================

"""
Problem 1 — Your Turn
⭐ Count the number of elements in a list using recursion

Write a function:

count_elements(items)

Given:

numbers = [10, 20, 30, 40, 50]

Expected output: 5

Rules
❌ Don't use len(items) to directly get the answer.
❌ Don't use loops.
❌ Don't use a global counter.
✅ Must use recursion.
✅ Use items[1:].
✅ Think about what the empty list should return.
"""

def count_elements(items):
    
    if items == []:
        return 0

    return 1 + count_elements(items[1:])

result = count_elements([10, 20, 30, 40, 50])
print(result)

"""
Output: 5
"""

# =====================================