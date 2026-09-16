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

"""
14. Copying a String with Slicing
text = "PYTHON"

copy = text[:]

print(copy)

Output:

PYTHON
15. Slicing with Step

There is another form:

string[start:end:step]

Example:

text = "PYTHON"

print(text[0:6:2])

Output:

PTO

Indexes selected:

0 → P
2 → T
4 → O
16. Reversing a String ⭐

One very useful Python technique:

text = "PYTHON"

reverse = text[::-1]

print(reverse)

Output:

NOHTYP

Here:

[::-1]

means:

Take the entire string with a step of -1.

We'll practice this later rather than just memorizing it.

17. Strings Are Immutable ⭐⭐⭐

This is one of the most important Python String concepts.

Immutable means:

Once a string object is created, its individual characters cannot be changed directly.

For example:

text = "PYTHON"

text[0] = "J"

This produces an error.

You cannot directly change P into J.

Instead, you create a new string.

For example:

text = "PYTHON"

text = "J" + text[1:]

print(text)

Output:

JYTHON

The original string wasn't modified character-by-character. A new string value was created and assigned to text.

18. Strings and Variables

Consider:

name = "Muskan"

The variable name refers to a string object.

If we do:

name = "Doraemon"

Python doesn't modify "Muskan" into "Doraemon".

Instead, name is reassigned to another string object.

This distinction becomes useful when you learn memory concepts and mutable vs immutable objects.

19. Traversing a String ⭐

Traversing means visiting each character one by one.

The easiest way is:

text = "PYTHON"

for character in text:
    print(character)

Output:

P
Y
T
H
O
N

Here:

for character in text:

means:

Take each character from text, one at a time, and store it in character.

20. Traversing Using Index

You can also traverse using indexes:

text = "PYTHON"

for i in range(len(text)):
    print(text[i])

Output:

P
Y
T
H
O
N

Here:

range(len(text))

becomes:

range(6)

which produces:

0 1 2 3 4 5

Then:

text[i]

accesses each character.

21. String + Conditions

Strings become powerful when combined with conditions.

Example:

text = "PYTHON"

for character in text:
    if character == "O":
        print("Found O")

Output:

Found O

Another example:

text = "PYTHON"

for character in text:
    if character in "AEIOU":
        print(character)

Output:

O

This kind of logic will become very important in your problem solving.

22. String Concatenation

Concatenation means joining strings together.

first_name = "Muskan"
last_name = "Bora"

full_name = first_name + " " + last_name

print(full_name)

Output:

Muskan Bora

The + operator joins strings.

23. String Repetition

The * operator can repeat a string.

text = "Hi "

print(text * 3)

Output:

Hi Hi Hi 
24. Important String Methods

Python provides many built-in string methods.

We'll learn these properly through practice, but keep this reference in your notes.

lower()

Converts characters to lowercase.

text = "PYTHON"

print(text.lower())

Output:

python
upper()

Converts characters to uppercase.

text = "python"

print(text.upper())

Output:

PYTHON
strip()

Removes leading and trailing whitespace.

text = "  Python  "

print(text.strip())

Output:

Python

Important: it does not remove spaces in the middle.

replace()

Replaces part of a string.

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)

Output:

I like Python
count()

Counts occurrences.

text = "BANANA"

print(text.count("A"))

Output:

3
find()

Returns the index of the first occurrence.

text = "PYTHON"

print(text.find("T"))

Output:

2

If the substring isn't found, find() returns:

-1
startswith()

Checks whether a string starts with something.

text = "Python"

print(text.startswith("Py"))

Output:

True
endswith()

Checks whether a string ends with something.

text = "Python"

print(text.endswith("on"))

Output:

True
split()

Splits a string into parts and returns a list.

text = "Python is powerful"

words = text.split()

print(words)

Output:

['Python', 'is', 'powerful']

⭐ Notice something important:

split() connects our String → List learning.

We'll explore that properly when we reach Lists.

join()

Joins multiple strings together.

words = ["Python", "is", "powerful"]

text = " ".join(words)

print(text)

Output:

Python is powerful

Again, this connects Strings with Lists.

25. Checking String Content

Python provides useful checking methods.

isalpha()

Checks whether all characters are alphabetic.

print("Python".isalpha())

Output:

True
isdigit()

Checks whether all characters are digits.

print("12345".isdigit())

Output:

True
isalnum()

Checks whether all characters are letters or numbers.

print("Python123".isalnum())

Output:

True
26. Important Concept — Strings Are Sequences

A string isn't just "text."

Python treats a string as an ordered sequence of characters.

That's why we can:

text[0]
text[-1]
text[1:4]

and:

for character in text:

This is a very important way of thinking about strings.

27. Common Mistakes ⚠️
Mistake 1 — Forgetting zero-based indexing

Wrong assumption:

P → 1
Y → 2

Correct:

P → 0
Y → 1
Mistake 2 — Thinking "123" is an integer
"123"

→ str

while:

123

→ int

Mistake 3 — Trying to modify a character
text[0] = "J"

❌ Not allowed because strings are immutable.

Mistake 4 — Forgetting that slicing excludes the end
text[0:3]

does not include index 3.

Mistake 5 — Confusing find() with index()

find() returns -1 if the text isn't found.

We'll discuss the difference when we practice string methods.
"""