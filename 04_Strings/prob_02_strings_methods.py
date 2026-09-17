# ==============================================

# String - Methods

# ===========================

"""
🧩 Problem 1 — lower() + upper()

Given:

text = "PyThOn"

Print:

The entire string in lowercase
The entire string in uppercase

Expected:

python
PYTHON
Rules
Use .lower()
Use .upper()
"""

text = "PyThOn"

print(text.lower())   # Output: python
print(text.upper())   # Output: PYTHON

# =================================

"""
🧩 Problem 2 — strip() + replace()

Given:

text = "   Hello Python   "

Write code to:

Remove the extra spaces from the beginning and end using strip().
Replace "Python" with "Django" using replace().

Expected output:

Hello Python
Hello Django
Rules 🎯
Use .strip()
Use .replace()
Don't manually remove or replace the text.
You can use two print statements.
"""

print()

text = "   Hello Python   "

print(text.strip())  # Output: Hello Python

new_text = text.replace("Python", "Django")
print(new_text.strip())   # Output: Hello Django

# ========================================

"""
🧩 Problem 3 — count() + find()

Given:

text = "BANANA"

Write code to:

1 Count how many times "A" appears.

Expected:
3

2 Find the position of the first "N".

Expected:

2
Rules 🎯
Use .count()
Use .find()
Don't use a loop.
Don't manually count the characters.
"""

print()

text = "BANANA"

print(text.count("A"))  # output: 3
print(text.find("N"))  # output: 2

# ==================================

"""
🧩 Problem 4 — startswith() + endswith()

Given:

text = "python_django"

Write code to check:

Does the string start with "python"?
Does the string end with "django"?

Expected output:

True
True
Rules 🎯
Use .startswith()
Use .endswith()
No loops.
"""
print()

text = "python_django"

print(text.startswith("python"))  # Output: True
print(text.startswith("django"))  # Output: False

print(text.endswith("python"))    # Output: False
print(text.endswith("django"))    # Output: True

# ===============================================

"""
🧩 Problem 5 — split()

Now let's learn a very important one because split() is used all the time in real Python code.

Given:

text = "Python Django REST API"

Write code to split this string into individual words.

Expected output
['Python', 'Django', 'REST', 'API']
Rules 🎯
Use .split()
Don't use a loop.
Don't manually create the list.
Print the result.

💡 Remember from your notes:

split() converts a string into a list.
"""

print()
text = "Python Django REST API"

print(text.split())   # OUTPUT: ['Python', 'Django', 'REST', 'API']

"""
NOTE: split() converts a string into a list.
"""

# =========================================

"""
🧩 Problem 6 — join()

Now let's learn the opposite direction. 😎

Given:

words = ["Python", "Django", "REST", "API"]

Use join() to produce this string:

Python-Django-REST-API
Rules 🎯
Use .join()
Don't use a loop.
Don't manually concatenate using +.
Print the final string.
"""

print()

words = ["Python", "Django", "REST", "API"]

new_word = "-".join(words)
print(new_word)         # Output: Python-Django-REST-API

# =================================================================

"""
🧩 Problem 7 — isalpha() + isdigit() + isalnum()

We're down to the final 3 methods in our current list. 💪

Given:

text1 = "Python"
text2 = "12345"
text3 = "Python123"

Write code to check:

Is text1 made only of alphabetic characters?
Is text2 made only of digits?
Is text3 made only of alphabetic or numeric characters?
Expected output
True
True
True
Rules 🎯

Use:

.isalpha()
.isdigit()
.isalnum()

No loops.

💡 Remember:

isalpha() → letters only
isdigit() → digits only
isalnum() → letters or digits
"""

print()

text1 = "Python"
text2 = "12345"
text3 = "Python123"

print(text1.isalpha())   # Output: True --> because letters only - condition satisfied
print(text1.isdigit())   # Output: False --> because it contains no digit - condition not satisfied
print(text1.isalnum())   # Output: True --> because it conatins letter and it requires letter or digits - condition satisfied

print(text2.isalpha())   # Output: False --> because it contains only digit - condition not satisfied
print(text2.isdigit())   # Output: True --> because it contains digit - condition satisfied
print(text2.isalnum())   # Output: True --> because it conatins letter and it requires letter or digits - condition satisfied

print(text3.isalpha())   # Output: False --> because letters and digit both are there - condition not satisfied
print(text3.isdigit())   # Output: False --> because letters and digit both are there -- condition not satisfied
print(text3.isalnum())   # Output: True --> because it conatins letter and it requires letter or digits - condition satisfied

"""
NOTE:
isalpha() → letters only
isdigit() → digits only
isalnum() → letters or digits
"""

# ==============================