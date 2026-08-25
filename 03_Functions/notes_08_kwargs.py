# ===========================================================

# **kwargs (Keyword Arguments)

# ===================================================

"""
**kwargs (Keyword Arguments):
Allows a function to accept any number of keyword arguments.
Python collects them into a dictionary.

**kwargs collects multiple keyword arguments into a dictionary.
"""

"""
🐍 Python Functions — **kwargs
1. What is **kwargs?

**kwargs stands for keyword arguments.

It allows a function to accept any number of keyword arguments.

Python collects all those keyword arguments into a dictionary.

Basic syntax
def function_name(**kwargs):
    # function body

For example:

def employee(**kwargs):
    print(kwargs)

Calling:

employee(
    name="Muskan",
    company="SWT Club",
    role="Full Stack Developer"
)

produces:

{
    "name": "Muskan",
    "company": "SWT Club",
    "role": "Full Stack Developer"
}
🔑 Important

**kwargs collects multiple keyword arguments into a dictionary.

2. Why do we use **kwargs?

Normally, if we know exactly which parameters a function needs, we can write:

def employee(name, company, role):
    print(name)
    print(company)
    print(role)

But what if we want to allow the caller to provide any number of additional keyword arguments?

For example:

employee(
    name="Muskan",
    company="SWT Club",
    role="Full Stack Developer",
    experience=2,
    location="Mumbai"
)

Instead of defining:

def employee(name, company, role, experience, location):

we can use:

def employee(**kwargs):
    print(kwargs)

Now the function can accept different numbers of keyword arguments.

3. **kwargs stores data as a dictionary

This is one of the most important things to remember.

def employee(**kwargs):
    print(kwargs)

Calling:

employee(
    name="Muskan",
    company="SWT Club",
    role="Developer"
)

Inside the function, Python effectively gives us:

kwargs = {
    "name": "Muskan",
    "company": "SWT Club",
    "role": "Developer"
}

Therefore:

type(kwargs)

would be:

<class 'dict'>
4. Accessing individual values

Because kwargs is a dictionary, we can access values using their keys.

def employee(**kwargs):
    print(kwargs["name"])
    print(kwargs["company"])
    print(kwargs["role"])

Calling:

employee(
    name="Muskan",
    company="SWT Club",
    role="Developer"
)

Output:

Muskan
SWT Club
Developer
Remember:
kwargs["name"]

means:

Get the value associated with the "name" key.

5. Printing formatted information

We can also use f-string formatting:

def employee(**kwargs):
    print(f"Name: {kwargs['name']}")
    print(f"Company: {kwargs['company']}")
    print(f"Role: {kwargs['role']}")

Call:

employee(
    name="Muskan",
    company="SWT Club",
    role="Full Stack Developer"
)

Output:

Name: Muskan
Company: SWT Club
Role: Full Stack Developer

This is very similar to the problem you're going to solve today. 😉

6. *args vs **kwargs

This comparison is very important.

Feature      	*args	                            **kwargs
Full meaning	Variable positional arguments	   Variable keyword arguments
Accepts	        Positional arguments	           Keyword arguments
Stored as	    Tuple	                           Dictionary
Example	        10, 20, 30	                       name="Muskan"
Access	        Index / loop	                   Dictionary key / loop

# -----------------

*args
def numbers(*args):
    print(args)

Call:

numbers(10, 20, 30)

Result:

(10, 20, 30)

# --------------

**kwargs
def employee(**kwargs):
    print(kwargs)

Call:

employee(
    name="Muskan",
    role="Developer"
)

Result:

{
    "name": "Muskan",
    "role": "Developer"
}

# --------------------------------

🧠 Easy memory trick
*args
   ↓
positional
   ↓
tuple

# -------------

**kwargs
   ↓
keyword
   ↓
dictionary

7. Why are there two * symbols?

This is worth understanding now.

One *
def numbers(*args):

means:

Collect multiple positional arguments.

Two **
def employee(**kwargs):

means:

Collect multiple keyword arguments.

So:

*args     → tuple
**kwargs  → dictionary


8. kwargs is a conventional name

Python doesn't require the variable to literally be called kwargs.

This works:

def employee(**data):
    print(data)

Calling:

employee(name="Muskan")

works perfectly.

However, the standard Python convention is:

def employee(**kwargs):

So in your learning and professional code, you'll normally see:

*args
**kwargs

Use those names unless there is a good reason not to.

9. **kwargs can accept different numbers of arguments

For example:

def show_info(**kwargs):
    print(kwargs)

We can call:

show_info(name="Muskan")

or:

show_info(
    name="Muskan",
    role="Developer"
)

or:

show_info(
    name="Muskan",
    role="Developer",
    company="SWT Club",
    experience=2
)

All are valid because the function isn't restricted to a fixed number of keyword arguments.

10. Important rule ⚠️

The arguments passed to **kwargs must be keyword arguments.

This is correct:

employee(
    name="Muskan",
    company="SWT Club"
)

This is not what **kwargs is designed to collect:

employee("Muskan", "SWT Club")

Those are positional arguments, which belong to *args
"""

# ===========================================================

"""
Quick Summary
                    FUNCTIONS
                        │
             ┌──────────┴──────────┐
             │                     │
          *args                 **kwargs
            │                     │
     Positional arguments    Keyword arguments
            │                     │
           Tuple                Dictionary
            │                     │
       (10, 20, 30)       {"name": "Muskan"}


⭐ Remember these two statements

*args → collects multiple positional arguments into a tuple.

**kwargs → collects multiple keyword arguments into a dictionary.

And because kwargs is a dictionary, you can access individual values using:

kwargs["key"]
"""

# ========================================

"""
🎯 Problem one

Problem — employee_info()

Create:

def employee_info(**kwargs):

The function should print:

Name: Muskan
Company: SWT Club
Role: Full Stack Developer

Call it using:

employee_info(
    name="Muskan",
    company="SWT Club",
    role="Full Stack Developer"
)
Rules

Must use **kwargs
Access the values using dictionary keys
Don't create separate parameters like name, company, role
"""

def employee_info(**kwargs):
    print(f"Name: {kwargs['name']}")
    print(f"Company: {kwargs['company']}")
    print(f"Role: {kwargs['role']}")

employee_info(
    name="Muskan",
    company="SWT Club",
    role="Full Stack Developer"
)

"""
Output:
Name: Muskan
Company: SWT Club
Role: Full Stack Developer
"""

# ====================================

"""
🧩 **kwargs Practice — Problem 2

Create:

def product_info(**kwargs):
Requirements

The function should print:

Product: Laptop
Price: 50000
Brand: Dell
Call the function using:
product_info(
    product="Laptop",
    price=50000,
    brand="Dell"
)
Rules

Must use **kwargs
Access values using dictionary keys
Don't create separate parameters like product, price, brand
Don't use a loop yet — we'll learn that next

🎯 Expected output
Product: Laptop
Price: 50000
Brand: Dell
"""

print()

def product_info(**kwargs):
    print(f"Product: {kwargs['product']}")
    print(f"Price: {kwargs['price']}")
    print(f"Brand: {kwargs['brand']}")

product_info(
    product="Laptop",
    price=50000,
    brand="Dell"
)

"""
Output:
Product: Laptop
Price: 50000
Brand: Dell
"""

# ==========================================

"""
**kwargs Revision — Problem 3
🧩 student_info()

Create:

def student_info(**kwargs):
Requirements

The function should print:

Name: Rahul
Course: Python
Experience: Beginner
Call the function using:
student_info(
    name="Rahul",
    course="Python",
    experience="Beginner"
)
Rules

✅ Must use **kwargs
✅ Access the values using dictionary keys
❌ Don't create separate parameters such as name, course, experience
❌ Don't use a loop yet
"""

print()

def student_info(**kwargs):
    print(f"Name: {kwargs['name']}")
    print(f"Course: {kwargs['course']}")
    print(f"Experience: {kwargs['experience']}")

student_info(
    name="Rahul",
    course="Python",
    experience="Beginner"
)

"""
Output:
Name: Rahul
Course: Python
Experience: Beginner
"""

# ===========================================

# IMP NOTES- .items():

# ==================

"""
Python Dictionary — .items() with **kwargs

1. What is .items()?

.items() is a dictionary method used to access both the key and its corresponding value.

With **kwargs, this is especially useful because kwargs is a dictionary.

def employee(**kwargs):
    print(kwargs)

If we call:

employee(
    name="Muskan",
    company="SWT Club",
    role="Developer"
)

Python stores the arguments as:

{
    "name": "Muskan",
    "company": "SWT Club",
    "role": "Developer"
}

2. Basic Syntax

The common syntax is:

for key, value in dictionary.items():
    # use key and value

With **kwargs:

def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
Example
def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


employee(
    name="Muskan",
    company="SWT Club",
    role="Developer"
)
Output
name Muskan
company SWT Club
role Developer

3. Understanding key and value

For this dictionary:

{
    "name": "Muskan",
    "company": "SWT Club"
}

The pairs are:

key       → value
----------------------
"name"    → "Muskan"
"company" → "SWT Club"

So when we write:

for key, value in kwargs.items():

Python gives us one pair at a time.

First iteration
key = "name"
value = "Muskan"
Second iteration
key = "company"
value = "SWT Club"
4. Why use .items()?

Without .items():

for key in kwargs:
    print(key)

This gives only the keys:

name
company
role

With .items():

for key, value in kwargs.items():
    print(key, value)

we get both:

name Muskan
company SWT Club
role Developer

Therefore:

.items() allows us to iterate through a dictionary's key-value pairs.

5. .keys(), .values(), .items()

Keep this simple table in notes:

Method	                Returns
.keys()                	Keys
.values()	            Values
.items()	            Key-value pairs

Example:

data = {
    "name": "Muskan",
    "role": "Developer"
}
Keys
data.keys()

→ name, role

Values
data.values()

→ Muskan, Developer

Key + Value
data.items()

→ ("name", "Muskan"), ("role", "Developer")

⭐ Most Important Syntax

Remember this:

for key, value in kwargs.items():
    print(key, value)

Think:

kwargs
  ↓
dictionary
  ↓
.items()
  ↓
key + value
  ↓
for loop


Definition:

.items() is a dictionary method that allows us to iterate through both keys and values as key-value pairs.
"""

# ==============================================

"""
🧩 **kwargs + .items() — Practice Problem 1

Create:

def show_profile(**kwargs):
Requirements

The function should:

Accept any number of keyword arguments using **kwargs.
Use a for loop.
Use .items() to get both the key and value.
Print each pair in this format:
name: Muskan
role: Full Stack Developer
company: SWT Club
experience: 2 years
Call the function with:
show_profile(
    name="Muskan",
    role="Full Stack Developer",
    company="SWT Club",
    experience="2 years"
)
Rules 🚨

✅ Must use **kwargs
✅ Must use .items()
✅ Must use a for loop
❌ Don't manually write kwargs["name"]
❌ Don't manually write each field
❌ Don't hardcode the output

🎯 Expected output
name: Muskan
role: Full Stack Developer
company: SWT Club
experience: 2 years
"""

print()

def show_profile(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(
    name="Muskan",
    role="Full Stack Developer",
    company="SWT Club",
    experience="2 years"
)

"""
Output:
name: Muskan
role: Full Stack Developer
company: SWT Club
experience: 2 years
"""

# ===========================================

"""
🔄 Problem 4 — **kwargs Revision
🧩 course_info()

Create:

def course_info(**kwargs):

The function should print:

Course: Python
Level: Beginner
Duration: 3 Months

Call it using:

course_info(
    course="Python",
    level="Beginner",
    duration="3 Months"
)
Rules

✅ Use **kwargs
✅ Access values using dictionary keys
❌ Don't use a loop
❌ Don't create separate parameters

Expected output
Course: Python
Level: Beginner
Duration: 3 Months
"""

print()

def course_info(**kwargs):
    print(f"Course: {kwargs['course']}")
    print(f"Level: {kwargs['level']}")
    print(f"Duration: {kwargs['duration']}")

course_info(
    course="Python",
    level="Beginner",
    duration="3 Months"
)

"""
Output:
Course: Python
Level: Beginner
Duration: 3 Months
"""

# =============================================

"""
Problem 2 — **kwargs + .items() Revision

Now reinforce the .items() concept.

🧩 order_details()

Create:

def order_details(**kwargs):

Requirements:

Accept any number of keyword arguments.
Use a for loop.
Use .items().
Print every key-value pair in this format:
item: Keyboard
price: 1500
quantity: 2
brand: Logitech

Call:

order_details(
    item="Keyboard",
    price=1500,
    quantity=2,
    brand="Logitech"
)
Rules 🚨

✅ Use **kwargs
✅ Use .items()
✅ Use a for loop
❌ Don't manually access kwargs["item"] etc.
❌ Don't hardcode the output

Expected output
item: Keyboard
price: 1500
quantity: 2
brand: Logitech
"""

print()

def order_details(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

order_details(
    item="Keyboard",
    price=1500,
    quantity=2,
    brand="Logitech"
) 

"""
Output:
item: Keyboard
price: 1500
quantity: 2
brand: Logitech
"""

# ===============================================================================

"""
**kwargs + Conditions

# ======================================

1. What is **kwargs?

**kwargs allows a function to accept any number of keyword arguments.

Inside the function, kwargs is stored as a dictionary.

Example
def student_info(**kwargs):
    print(kwargs)


student_info(
    name="Muskan",
    age=23,
    course="Python"
)

Output
{'name': 'Muskan', 'age': 23, 'course': 'Python'}

So internally:

kwargs = {
    "name": "Muskan",
    "age": 23,
    "course": "Python"
}

2. Accessing Values from kwargs

Because kwargs is a dictionary, we can access values using their keys.

Example
def student_info(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["course"])


student_info(
    name="Muskan",
    age=23,
    course="Python"
)
Output
Muskan
23
Python

3. Using if with **kwargs

Since kwargs is a dictionary, we can use its values inside conditions.

Example
def student_info(**kwargs):

    if kwargs["age"] >= 18:
        print("Adult")


student_info(
    name="Muskan",
    age=23
)
Output
Adult
How Python understands it

Python gets:

kwargs["age"]

which gives:

23

So the condition becomes:

if 23 >= 18:

Since the condition is True, Python prints:

Adult

4. Using if-else with **kwargs

We can also use else when the condition is false.

Example
def student_info(**kwargs):

    if kwargs["age"] >= 18:
        print("Adult")
    else:
        print("Minor")


student_info(
    name="Rahul",
    age=16
)
Output
Minor

Here:

kwargs["age"]

gives:

16

So Python checks:

if 16 >= 18:

This is False, therefore the else block executes.

5. Comparing a String Value

We can also use a value from kwargs to compare strings.

Example
def course_info(**kwargs):

    if kwargs["level"] == "Beginner":
        print("Starting level")
    else:
        print("Advanced level")


course_info(
    course="Python",
    level="Beginner"
)
Output
Starting level

Here:

kwargs["level"]

gives:

Beginner

So Python checks:

if "Beginner" == "Beginner":

The condition is True.

🧠 Important Concept

Remember this relationship:

**kwargs
    ↓
Dictionary
    ↓
kwargs["key"]
    ↓
Value
    ↓
Use that value in if/else

For example:

def employee_info(**kwargs):

    if kwargs["department"] == "IT":
        print("Technical Department")
    else:
        print("Non-Technical Department")

Here:

kwargs["department"]

gets the value from the dictionary, and that value is used by the if condition.

⚠️ Important Note

For now, we are accessing keys directly:

kwargs["age"]

So the key must exist.

📌 Quick Revision
def function_name(**kwargs):

    if kwargs["key"] == value:
        print("Condition is True")
    else:
        print("Condition is False")
Example
def student_info(**kwargs):

    if kwargs["age"] >= 18:
        print("Student is an adult")
    else:
        print("Student is a minor")

That's the complete concept for **kwargs + Conditions that you need right now. 🐍💪
"""

# ==============================================

"""
Problem 6 — **kwargs + if

Create:

def student_info(**kwargs):

Call it with:

student_info(
    name="Muskan",
    age=23,
    course="Python"
)

Inside the function:

Check whether "course" exists in kwargs.
If it exists, print:
Course: Python
Otherwise print:
Course information not provided
Rules

✅ Must use **kwargs
✅ Must use if
✅ Access the value using the dictionary key
❌ Don't create separate parameters
❌ Don't use a loop
❌ Don't hardcode "Python" inside the if condition
"""

print()

def student_info(**kwargs):
    
    if "course" in kwargs:
        print(kwargs['course'])
    else:
        print("Course information not provided")

student_info(
    name="Muskan",
    age=23,
    course="Python"
)

"""
Output:
Python
"""

# =============================================================

"""
**kwargs Revision — Problem 1
employee_info()

Create:

def employee_info(**kwargs):

The function should print:

Name: Muskan
Role: Full Stack Developer
Company: SWT Club
Experience: 2 years

Call it with:

employee_info(
    name="Muskan",
    role="Full Stack Developer",
    company="SWT Club",
    experience="2 years"
)
Rules

✅ Use **kwargs
✅ Access values using dictionary keys
❌ Don't create separate parameters
❌ Don't use a loop
"""

print()

def employee_info(**kwargs):
    print(f"Name: {kwargs['name']}")
    print(f"Role: {kwargs['role']}")
    print(f"Company: {kwargs['company']}")
    print(f"Experience: {kwargs['experience']}")

employee_info(
    name="Muskan",
    role="Full Stack Developer",
    company="SWT Club",
    experience="2 years"
)

"""
Output:
Name: Muskan
Role: Full Stack Developer
Company: SWT Club
Experience: 2 years
"""

# ==================================================

"""
**kwargs Revision — Problem 2
show_details()

Create:

def show_details(**kwargs):

Call it with:

show_details(
    name="Muskan",
    skill="Python",
    experience=2,
    available=True
)

The function should use:

**kwargs
for loop
.items()

and print every key-value pair like:

name: Muskan
skill: Python
experience: 2
available: True
Rules

✅ Use **kwargs
✅ Use .items()
✅ Use a for loop
❌ Don't manually access individual keys
❌ Don't hardcode the output
"""

print()

def show_details(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(
    name="Muskan",
    skill="Python",
    experience=2,
    available=True
)

"""
Output:
name: Muskan
skill: Python
experience: 2
available: True
"""

# ===================================================