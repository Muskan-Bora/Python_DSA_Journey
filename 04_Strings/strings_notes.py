"""
🐍 Python Strings — Complete Notes
1. What is a String?

A string is a sequence of characters enclosed inside quotes.

Python supports:

name = "Muskan"
city = 'Mumbai'
message = "Hello World"

Both single quotes ' ' and double quotes " " can be used.

name1 = "Muskan"
name2 = 'Muskan'

Both are strings.

We can verify the type:

name = "Muskan"

print(type(name))

Output:

<class 'str'>

str is Python's data type for strings.

2. Creating Strings
Single quotes
name = 'Muskan'
Double quotes
name = "Muskan"
Triple quotes

Triple quotes are useful for multi-line strings.

message = """Hello
My name is Muskan
I am learning Python"""

You can also use triple single quotes:

message = '''Hello
My name is Muskan
I am learning Python'''
3. Strings Can Contain Different Characters

A string can contain:

Letters
text = "Python"
Numbers
text = "12345"

⚠️ "12345" is still a string, not an integer.

print(type("12345"))

Output:

<class 'str'>
Symbols
text = "@#$%"
Spaces
text = "Hello World"
Combination
text = "Muskan@123"
4. Empty String

A string can contain zero characters.

text = ""

This is called an empty string.

Its length is:

print(len(text))

Output:

0
5. String Indexing ⭐

A string is a sequence of characters.

For example:

text = "PYTHON"

Each character has a position called an index.

Character:   P   Y   T   H   O   N
Index:       0   1   2   3   4   5

Python uses zero-based indexing, meaning the first character is at index 0.

text = "PYTHON"

print(text[0])
print(text[1])
print(text[2])

Output:

P
Y
T
Important rule
First character → index 0
Second character → index 1
Third character → index 2

So:

text[0]

means:

Give me the character at index 0.

6. Negative Indexing ⭐

Python also allows indexing from the end of the string.

text = "PYTHON"

Positions from the end:

Character:    P    Y    T    H    O    N
Positive:     0    1    2    3    4    5
Negative:    -6   -5   -4   -3   -2   -1

Therefore:

print(text[-1])

Output:

N

And:

print(text[-2])

Output:

O
⭐ Remember
text[0]   → first character
text[-1]  → last character

This is extremely useful in problem solving.

7. String Length — len()

The len() function returns the number of characters in a string.

text = "PYTHON"

print(len(text))

Output:

6

Spaces are also counted.

text = "Hello World"

print(len(text))

Hello = 5
space = 1
World = 5

Total:

11
8. Indexing + len()

A common relationship:

text = "PYTHON"

print(len(text))
print(text[len(text) - 1])

Output:

6
N

Why?

The length is 6, but indexes go:

0 1 2 3 4 5

Therefore:

len(text) - 1

gives the last valid index.

So:

text[len(text) - 1]

gets the last character.

Although in normal code, this is simpler:

text[-1]
9. Accessing Individual Characters
text = "PYTHON"

first = text[0]
second = text[1]
last = text[-1]

print(first)
print(second)
print(last)

Output:

P
Y
N
10. String Slicing ⭐

Indexing gets one character.

Slicing gets multiple characters.

Syntax:

string[start:end]

Example:

text = "PYTHON"

print(text[0:3])

Output:

PYT

Why?

P Y T H O N
0 1 2 3 4 5

0:3 means:

Start at index 0 and stop before index 3.

So indexes 0, 1, 2 are included.

11. Slicing Rule

This is very important:

[start : end]

means:

start → included
end   → excluded

For example:

text = "PYTHON"

print(text[1:4])

Output:

YTH

Indexes:

1 → Y
2 → T
3 → H
4 → excluded
12. Omitting Start

You can leave the start empty.

text = "PYTHON"

print(text[:3])

Output:

PYT

This means:

Start from the beginning and stop before index 3.

13. Omitting End

You can leave the end empty.

text = "PYTHON"

print(text[2:])

Output:

THON

This means:

Start at index 2 and continue until the end.
"""