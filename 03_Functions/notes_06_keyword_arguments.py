# ==========================================================

"""

# Python Functions — Keyword Arguments

1. What is a Keyword Argument?

---

A keyword argument is an argument passed to a function by explicitly specifying the parameter name.

Example:

def employee(name, company):
print(name)
print(company)

employee(name="Muskan", company="SWT Club")

Here Python knows:

name = "Muskan"
company = "SWT Club"

---

2. Positional Arguments

---

Example:

employee("Muskan", "SWT Club")

Python maps values according to their position:

1st argument → 1st parameter
2nd argument → 2nd parameter

Therefore:

name = "Muskan"
company = "SWT Club"

---

3. Keyword Arguments

---

Example:

employee(name="Muskan", company="SWT Club")

Here we explicitly specify which parameter receives
which value.

name = "Muskan"
company = "SWT Club"

---

4. Main Difference

---

Positional:

employee("Muskan", "SWT Club")

Mapping depends on position.

Keyword:

employee(name="Muskan", company="SWT Club")

Mapping depends on the parameter name.

---

5. Keyword Arguments Can Change Order

---

Example:

def employee(name, company, role):
print(name)
print(company)
print(role)

employee(
role="Developer",
company="SWT Club",
name="Muskan"
)

Python still understands:

name = "Muskan"
company = "SWT Club"
role = "Developer"

The order does not matter when using keyword arguments.

---

6. Keyword Arguments + Default Parameters

---

Example:

def welcome(name="Guest"):
print(f"Welcome, {name}!")

welcome()

Output:

Welcome, Guest!

We can also use a keyword argument:

welcome(name="Muskan")

Output:

Welcome, Muskan!

The provided keyword argument replaces the default value.

---

7. Keyword Arguments + Multiple Parameters

---

Example:

def student(name, marks, bonus=0):
return name, marks + bonus

student(
name="Muskan",
marks=85,
bonus=5
)

The mapping is:

name = "Muskan"
marks = 85
bonus = 5

---

8. Important Rule

---

Positional arguments should come BEFORE keyword arguments.

Correct:

employee("Muskan", company="SWT Club")

Incorrect:

employee(name="Muskan", "SWT Club")

General rule:

positional arguments → first
keyword arguments   → after

---

9. Mental Model

---

Positional:

function("A", "B")

```
    ↓
```

1st value → 1st parameter
2nd value → 2nd parameter

Keyword:

function(first="A", second="B")

```
    ↓
```

first  → "A"
second → "B"

Think:

Positional = "You figure it out from the position."

Keyword = "I'm telling you exactly where this value goes."

===========================================================
Key Points
==========

1. Keyword arguments explicitly specify parameter names.

2. Keyword arguments make function calls easier to read.

3. Keyword arguments can be provided in a different order.

4. Keyword arguments work with default parameters.

5. Positional arguments must come before keyword arguments
   when they are mixed in a function call.

===========================================================
End of Notes
============

"""

# ===================================================================

"""
1. Practice Problem

Problem — employee_info()

Create:

def employee_info(name, company, role):

The function should print:

Name: <name>
Company: <company>
Role: <role>

Then call the function using only keyword arguments, but deliberately put them in this order:

role
name
company
"""

def employee_info(name, company, role):
    print(f"Name: {name}")
    print(f"Company: {company}")
    print(f"Role: {role}")

employee_info(
    role = "Full Stack Developer",
    name = "Muskan",
    company = "SWT Club"
)

"""
Output:
Name: Muskan
Company: SWT Club
Role: Full Stack Developer
"""

# =================================