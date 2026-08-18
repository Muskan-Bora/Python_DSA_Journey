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