# =============================================================

# Python Functions — *args

"""
1. What is *args?

Normally, a function has a fixed number of parameters:

def add(a, b):
    return a + b

This function expects exactly two arguments:

add(10, 20)

But sometimes we don't know beforehand how many positional arguments the function will receive.

For example:

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)

Instead of creating different functions for different numbers of arguments, Python provides:

*args

*args allows a function to accept any number of positional arguments.

2. Basic Syntax
def function_name(*args):
    # function body

Example:

def show_numbers(*args):
    print(args)

Calling:

show_numbers(10, 20, 30, 40)

gives:

(10, 20, 30, 40)
Important:

args becomes a tuple.

So mentally:

Multiple positional arguments
            ↓
          *args
            ↓
         tuple

In this example:

args = (10, 20, 30, 40)


3. Why Does *args Exist?

Without *args:

def add(a, b):
    return a + b

You can only pass two positional arguments.

But with:

def add(*args):

you can pass:

add()
add(10)
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)

The function can accept a variable number of positional arguments.
"""

"""
4. *args Stores Arguments in a Tuple

Consider:

def show_numbers(*args):
    print(args)


show_numbers(10, 20, 30)

Output:

(10, 20, 30)

Therefore:

args is a tuple().

We can verify its type:

def show_numbers(*args):
    print(type(args))


show_numbers(10, 20, 30)

Output:

<class 'tuple'>

5. Using a Loop with *args

Because args is a tuple, we can loop through it.

def show_numbers(*args):
    for number in args:
        print(number)


show_numbers(10, 20, 30, 40)

Output:

10
20
30
40

Here:

args = (10, 20, 30, 40)

and the loop accesses each value one by one.

6. Practical Example — Calculate Total

One of the most useful beginner examples:

def calculate_total(*numbers):
    total = 0


    for number in numbers:
        total += number


    return total




result = calculate_total(10, 20, 30, 40)


print(result)

Output:

100
What happened?

The function received:

numbers = (10, 20, 30, 40)

Then:

10 + 20 + 30 + 40

gave:

100

Notice that we didn't have to define:

def calculate_total(a, b, c, d):

We can accept any number of positional arguments.

7. args Is Just a Conventional Name

This is important.

Python does not require the name args.

These are all valid:

def show(*args):
    print(args)
def show(*numbers):
    print(numbers)
def show(*values):
    print(values)

The * is what tells Python:

"Collect all remaining positional arguments."

However, Python developers conventionally use:

*args

So you should also follow that convention unless there is a good reason not to.
"""

"""
8. *args vs Normal Parameters
Normal parameters
def add(a, b):
    return a + b

Expected:

2 arguments
*args
def add(*args):

Can accept:

0 arguments
1 argument
2 arguments
3 arguments
4 arguments
...

So:

Fixed parameters
       ↓
Known number of arguments


*args
       ↓
Unknown / variable number of positional arguments

9. *args With a Normal Parameter

You can also combine normal parameters with *args.

For example:

def student(name, *marks):
    print(f"Student: {name}")
    print(f"Marks: {marks}")

Calling:

student("Muskan", 80, 85, 90)

gives:

Student: Muskan
Marks: (80, 85, 90)

Here:

name  → "Muskan"
marks → (80, 85, 90)

This is powerful because the first argument has a specific meaning, while the remaining positional
arguments are collected into marks.

10. Important Rule

*args collects positional arguments.

For example:

def show(*args):
    print(args)


show(10, 20, 30)

works.

But *args is not for keyword arguments.

Keyword arguments are handled separately using:

**kwargs

For now:

*args
   ↓
Positional arguments


**kwargs
   ↓
Keyword arguments


11. Common Mistake

Don't confuse:

args

with:

*args
Inside the function:
def show(*args):
    print(args)

We use:

args

to access the collected tuple.

When defining the function:
def show(*args):

The * tells Python to collect the arguments.

12. Real Mental Model 

Whenever you see:

def function(*args):

immediately think:

"This function can receive multiple positional arguments, and Python will collect them into a tuple called args."

For example:

function(10, 20, 30, 40)

Think:

10 ─┐
20 ─┤
30 ─┼──→ args = (10, 20, 30, 40)
40 ─┘

That's the core concept. 🔥

📌 Quick Reference
Concept	Meaning
*args	Variable number of positional arguments
args	Tuple containing those arguments
*	Tells Python to collect positional arguments
for item in args	Iterate through collected arguments
return args	Return the tuple
Example:

def calculate_total(*numbers):
    total = 0


    for number in numbers:
        total += number


    return total




result = calculate_total(100, 200, 300)


print(result)

Output:

600
🧠 One-line definition for your notes

*args allows a Python function to accept a variable number of positional arguments, which are automatically
collected and stored as a tuple.
"""

# ==========================================================

"""
Prob 1 - *args Practice — Calculate Total

Create:

def calculate_total(*numbers):
Requirements

The function should:

Accept any number of numbers using *args.
Add all the numbers.
Return the total.
Store the returned value in result.
Print result.
Call it with:
calculate_total(10, 20, 30, 40)
Expected output:
100
"""

def calculate_total(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total

result = calculate_total(10, 20, 30, 40)

print(result)

"""
Output:
100
"""

# ================================