# ==================================================

# Recursion — Strings

"""
Definition

Recursion can be used to process a string by repeatedly working with a smaller portion of the string.

Common pattern
def function(text):
    if text == "":
        return

    # work with text[0]

    function(text[1:])

Important concepts
text[0] → first character
text[1:] → remaining string
text == "" → possible base case
Recursive call receives a smaller string
Work can happen before or after the recursive call
The base case prevents infinite recursion

Mental model
HELLO
 ↓
ELLO
 ↓
LLO
 ↓
LO
 ↓
O
 ↓
""
 ↓
STOP
"""

# =============================================

"""
Problem 1 — Print Every Character

Complete this:

def print_string(text):
    # your logic

print_string("HELLO")

Expected output:

H
E
L
L
O
Rules
❌ No for
❌ No while
❌ Don't convert the string into a list
✅ Must use recursion
✅ Must have a base case
✅ Use the first character + smaller string idea
"""

def print_string(text):
    if text == "":
        return 
        
    print(text[0])

    print_string(text[1:])

print_string("HELLO")

"""
Output:
H
E
L
L
O
"""

# ===============================

"""
Problem 2 — Print a String in Reverse

Write:

def reverse_string(text):
    # your logic

reverse_string("HELLO")

Expected output:

O
L
L
E
H
Rules 🧠
❌ No for
❌ No while
❌ No [::-1]
✅ Use recursion
✅ Use a base case
✅ Use text[1:]
"""
print()
def reverse_string(text):
    if text == "":
        return 

    reverse_string(text[1:])
    print(text[0])
reverse_string("HELLO")

"""
Output:
O
L
L
E
H
"""

# ===================================

"""
🔤 Now #2 — Recursion with Strings

Write a recursive function that counts the number of characters in a string.

Example:

count_characters("HELLO") → 5
count_characters("PYTHON") → 6
count_characters("") → 0
Rules
❌ No len()
❌ No loops
✅ Must use recursion
✅ Must have a base case
✅ Must use return

Hint: Think about yesterday:

text[0]
text[1:]
"""
print()

def count_characters(text):
    if text == "":
        return 0
    
    return 1 + count_characters(text[1:])

count = count_characters("HELLO")
print(count)

"""
Output:
5
"""

# ========================================
