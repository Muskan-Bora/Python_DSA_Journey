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

"""

🧩 Problem — show_score()

Given:

score = 50

Create:

def show_score():

Inside the function:

Create a local variable called score.
Give it the value 100.
Print the local score.

Then:

show_score()
print(score)
Expected output
100
50
🚨 Rules

✅ Create a global score = 50
✅ Create a local score = 100 inside the function
✅ Print both
❌ Don't use global
❌ Don't change the global variable directly
"""

score = 50    # Global 

def show_score():
    score = 100   # local
    print(score)  # It prints local

show_score()
print(score)      # It prints global

"""
Output:
100    --> 1st local scope will come becoz its inside the function 
50     --> than global scope outside the function will execute
"""

# =================================================

"""
NOTE: A local variable can have the same name as a global variable, and changing/creating the local
variable does not change the global variable.
"""

# ============================================================

"""
🔄 Prob 2 - Local & Global Variable Revision
🧩 Problem — show_name()

Given:
name = "Muskan"

Create:
def show_name():

Inside the function:

Create a local variable called name.
Set it to "Doraemon".
Print the local name.

Then:

show_name()
print(name)
🎯 Expected Output
Doraemon
Muskan
🚨 Rules

✅ Use a global name = "Muskan"
✅ Create a local name = "Doraemon" inside the function
✅ Print both values
❌ Don't use global
❌ Don't change the global variable
"""
print()

name = "Muskan"   # Global Variable

def show_name():
    name = "Doraemon"       # Local Variable
    print(name)

show_name()
print(name)

"""
Output:
Doraemon
Muskan
"""

# ============================================================

"""
🧩 global Keyword — Practice Problem #1

Given:

score = 50

Create:

def update_score():

Inside the function:

Use the global keyword with score.
Change score to 100.
Print score.

Then:

update_score()
print(score)
Expected output
100
100
🚨 Rules

✅ Must use global score
✅ Change the global variable to 100
✅ Print inside and outside the function
❌ Don't create another local score
"""

print()

score = 50

def update_score():
    global score        
    score = 100       # This modifies global variable 
    print(score)

update_score()
print(score)

"""
Output:
100
100
"""

# =========================================

"""
🧩 Problem 2 — increase_balance()

Given:

balance = 1000

Create:

def increase_balance():

Inside the function:

Use global balance.
Increase the balance by 500.
Print the updated balance.

Then call:

increase_balance()
print(balance)
Expected output
1500
1500
🚨 Rules

✅ Must use global balance
✅ Use the existing value of balance
✅ Increase it by 500
✅ Print inside and outside
❌ Don't create another local balance
"""

print()

balance = 1000

def increase_balance():
    global balance
    balance = balance + 500    # Here 500 increased from the global variable: 1000 + 500 = 1500
    print(balance)             # 1500

increase_balance()
print(balance)      # The global balance was modified inside the function, so its updated value remains available after the function finishes.

"""
Output:
1500
1500
"""

# ================================