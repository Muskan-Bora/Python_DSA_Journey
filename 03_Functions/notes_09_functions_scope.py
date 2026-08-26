# ==============================================================

"""
Python Function Scope

# ==========================================

What is Scope?

Scope defines the part of a program where a variable can be accessed.

Python mainly has:

Local Scope
Global Scope

1. Local Scope
A variable created inside a function is normally local to that function.

Syntax
def function_name():
    variable = value
Example
def calculate():
    total = 100
    print(total)

calculate()

Output:

100

total is a local variable and cannot normally be accessed outside the function.

def calculate():
    total = 100

calculate()

print(total)  # NameError

# ---------------------------------

2. Global Scope

A variable created outside a function has global scope.

Example
name = "Muskan"

def greet():
    print(name)

greet()

Output:

Muskan

The function can read the global variable.

# --------------------------------------------------

3. Local Variable with Same Name as Global Variable

A local variable can have the same name as a global variable.

name = "Muskan"

def greet():
    name = "Rahul"
    print(name)

greet()

print(name)

Output:

Rahul
Muskan

The local variable affects only the function.

The global variable remains unchanged.

# --------------------------------------------

4. global Keyword

The global keyword allows a function to modify a global variable.

Example
count = 0

def increase():
    global count
    count += 1

increase()

print(count)

Output:

1
Syntax
global variable_name

# ------------------------------

⭐ Key Points

Local variable
→ Created inside a function
→ Normally accessible only inside that function

Global variable
→ Created outside a function
→ Can be read inside functions

global keyword
→ Allows a function to modify a global variable
One-line definition

Scope determines where a variable can be accessed in a Python program.

🧠 Small Examples to Remember
Local
def test():
    x = 10

x → local variable.

Global
x = 10

def test():
    print(x)

x → global variable.

Same name
x = 10

def test():
    x = 20

The function's x → local.
Outside x → global.

Modify global
x = 10

def test():
    global x
    x = 20

Now the global x becomes 20.
"""

# =====================================================