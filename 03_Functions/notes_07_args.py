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