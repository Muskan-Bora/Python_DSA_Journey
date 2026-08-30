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

"""
7. Function Composition with Real-World Logic

Suppose we want to calculate the final price after applying a discount.

We could separate the responsibilities:

def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount


def add_tax(price, tax):
    tax_amount = price * tax / 100
    return price + tax_amount


final_price = add_tax(calculate_discount(1000, 10), 18)

print(final_price)
Execution

First:

calculate_discount(1000, 10)

10% discount:

1000 - 100 = 900

Then:

add_tax(900, 18)

18% tax:

900 + 162 = 1062

Output:

1062.0

This is much closer to how functions are used in real applications.

Instead of one giant function:

calculate everything

we create:

calculate_discount()
        ↓
     result
        ↓
add_tax()
        ↓
   final result
 
8. Important Rule

For composition to work:

The output of one function must be suitable as the input of the next function.

Example:

def get_number():
    return 10


def double(number):
    return number * 2


result = double(get_number())

print(result)

Execution:

get_number()
     ↓
    10
     ↓
double(10)
     ↓
    20

Output:

20
"""

# ===============================================

"""
9. Common Mistake ❌

Don't confuse print() with return.

Wrong for composition:

def get_number():
    print(10)


def double(number):
    return number * 2


result = double(get_number())

get_number() prints 10, but returns None.

So effectively Python tries:

double(None)

which causes an error because you cannot multiply None by 2.

10. Nested Function Calls

When functions are written inside one another like:

result = function_b(function_a(value))

Python evaluates the innermost function first.

For:

result = subtract(multiply(add(10, 20)))

Think:

1. add(10, 20)
       ↓
      30

2. multiply(30)
       ↓
      60

3. subtract(60)
       ↓
      55

This is one of the most important things to remember.

11. Function Composition vs Calling Functions Separately
Separate calls
step1 = add(10, 20)
step2 = multiply(step1)
result = subtract(step2)
Composed call
result = subtract(multiply(add(10, 20)))

The second version is more compact, while the first version can sometimes be easier to debug.

Both are valid.

As your programs become larger, you'll often choose whichever makes the data flow easiest to understand.

# =================================

🧠 Quick Summary

Function Composition
        ↓
Use the returned result of one function
        ↓
as the argument of another function

Remember:
return → sends value back
       ↓
another function can receive it

Basic pattern:
def function_a(value):
    return something


def function_b(value):
    return something_else


result = function_b(function_a(value))
Execution rule:
Python evaluates
the innermost function first
        ↓
then moves outward

🎯 Imp Point:

Function composition allows us to combine small, reusable functions by passing the returned value of
one function into another function. It helps break complex operations into smaller, manageable steps and
is an important concept for writing clean and reusable Python code.
"""

# ===================================================