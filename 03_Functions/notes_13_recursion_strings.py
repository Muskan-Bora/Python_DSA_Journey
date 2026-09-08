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