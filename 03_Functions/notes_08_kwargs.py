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
    print(f"Product: {kwargs["product"]}")
    print(f"Price: {kwargs["price"]}")
    print(f"Brand: {kwargs["brand"]}")

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