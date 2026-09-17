# ============================================

# Strings - Slicing

"""
🧩 Problem 3 — String Slicing

We already covered indexing yesterday. Now let's test slicing.

Given:

text = "PYTHON"

Write code to print:

1 First three characters

Expected:
PYT

2 Last three characters

Expected:

HON
3 Characters from index 1 to index 4

Expected:

YTH

Rules 🎯
Don't use a loop.
Don't use len().
Use slicing only.
Remember:
start → included
end   → excluded

So think carefully about the indexes.
"""

text = "PYTHON"
print(text[:3])    # Output: PYT
print(text[3:])    # Output: HON
print(text[1:4])   # Outpiut: YTH

# ============================

"""
🧩 Problem 4 — Slicing with Step

Now let's introduce the third part of slicing:

text[start:end:step]

Given:

text = "PYTHON"

Write code to print:

1 Every second character

Expected:
PTO

2 Every second character starting from index 1

Expected:
YHN

3 Reverse the entire string using slicing

Expected:

NOHTYP
Rules 🎯
No loop
No len()
Use slicing
Try to figure out the step yourself.
"""

print()

text = "PYTHON"

print(text[::2])          # Output: PTO
print(text[1::2])         # Output: YHN
print(text[::-1])         # Output: NOHTYP

# ===============================================

"""
🧩 Problem 5 — String Immutability

Now let's move to the next concept from your notes: immutability.

Consider:

text = "PYTHON"

Try to change the first character from P to J so that the final string becomes:

JYTHON
Your task

Write Python code that achieves this.

Rules 🎯

You cannot do:

text[0] = "J"
Don't use a loop.
Don't use .replace() yet.
Try to create the new string using slicing and concatenation.

💡 Think about how you can take:

"PYTHON"

and combine "J" with everything after the first character.
"""
print()

text = "PYTHON"

text = "J" + text[1:]

print(text) # Output: JYTHON

# =========================================

"""
🧩 Problem 6 — String Traversal

Now let's move to the next concept: traversing a string.

Given:

text = "PYTHON"

Write a program that prints each character on a separate line.

Expected output
P
Y
T
H
O
N
Rules 🎯
Use a for loop.
Don't use indexing like text[i].
Don't use len().
Don't use split().

💡 Think about the fact that a string itself is iterable.
"""

print()

text = "PYTHON"

for character in text:
    print(character)

"""
Output:
P
Y
T
H
O
N
"""

# =====================================

"""
Next: Problem 7 — Traversal + Condition

Let's make it slightly more practical.

Given:

text = "PYTHON"

Write a program that traverses the string and prints only the vowels.

Expected output
O
Rules
Use a for loop.
Don't use indexing.
Don't use count().
Don't use .lower() / .upper() yet.
Use a condition.

💡 Hint: You can check whether each character exists inside:

"AEIOU"

Try it yourself. 😎🐍
"""

print()

text = "PYTHON"
vowel = "AEIOU"

for character in text:
    if character in vowel:
        print(character)

"""
Output:
O
"""

# ==================================

"""
🧩 Problem 8 — Count Vowels

Given:

text = "BANANA"

Write a program that counts how many vowels are present in the string.

Expected output:

3

Because:

B → ❌
A → ✅ 1
N → ❌
A → ✅ 2
N → ❌
A → ✅ 3
Rules 🎯
Use a for loop.
Use a condition.
Use a counter variable.
Don't use .count().
Don't use any built-in method that directly counts vowels.

💡 Start with something like:

count = 0

Then think about when the counter should increase.
"""

print()

count = 0
text = "BANANA"
vowel = "AEIOU"

for character in text:
    if character in vowel:
        count += 1

print(count) # Output: 3

# ================================================