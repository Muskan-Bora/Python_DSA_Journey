# ================================================================

"""
🧩 Function Composition in Python

1. What is Function Composition?

Function Composition means using the result returned by one function as the input to another function.

In simple words:

Function A
    ↓
returns a value
    ↓
Function B receives that value
    ↓
returns another value

Instead of doing everything inside one function, we can divide the work into small, reusable
functions and connect them together.

2. Basic Example

def add(a, b):
    return a + b


def multiply(number):
    return number * 2


result = multiply(add(10, 20))

print(result)
Execution

First Python evaluates:

add(10, 20)

Inside add():

10 + 20 = 30

So:

add(10, 20)

returns:

30

That returned value becomes the argument for multiply():

multiply(30)

Inside multiply():

30 x 2 = 60

Therefore:

result = 60

Output:

60
Flow
add(10, 20)
     ↓
    30
     ↓
multiply(30)
     ↓
    60
"""

# =============================================

"""
3. Why return is Important

Function composition depends heavily on return.

For example:

def add(a, b):
    return a + b

The returned value can be passed to another function:

multiply(add(10, 20))

But if we use print() instead:

def add(a, b):
    print(a + b)

then:

result = add(10, 20)
print(result)

Output:

30
None

Why?

Because print() only displays the value. It doesn't send that value back to the caller.

So remember:

print()
   ↓
Displays a value

return
   ↓
Sends a value back
   ↓
Can be used by another function

4. Composition Using Two Functions

Consider:

def square(number):
    return number * number


def add_five(number):
    return number + 5


result = add_five(square(4))

print(result)
Execution

First:

square(4)
4 x 4 = 16

Then:

add_five(16)
16 + 5 = 21

Therefore:

21

Flow:

square(4)
   ↓
  16
   ↓
add_five(16)
   ↓
  21
"""

# ==========================================

"""
5. Composition Using Three Functions

We can also connect more than two functions.

def add(a, b):
    return a + b


def multiply(number):
    return number * 2


def subtract(number):
    return number - 5


result = subtract(multiply(add(10, 20)))

print(result)
Execution

Python works from the innermost function call outward.

Step 1
add(10, 20)
30
Step 2
multiply(30)
60
Step 3
subtract(60)
55

Final:

55
Complete flow
add(10, 20)
      ↓
     30
      ↓
multiply(30)
      ↓
     60
      ↓
subtract(60)
      ↓
     55

6. Another Way to Write the Same Logic

The previous example can also be written step-by-step:

def add(a, b):
    return a + b


def multiply(number):
    return number * 2


def subtract(number):
    return number - 5


step1 = add(10, 20)
step2 = multiply(step1)
result = subtract(step2)

print(result)

Output:

55

This is doing exactly the same thing.

Nested version
result = subtract(multiply(add(10, 20)))
Step-by-step version
step1 = add(10, 20)
step2 = multiply(step1)
result = subtract(step2)

Both are valid.
"""

# ===============================================