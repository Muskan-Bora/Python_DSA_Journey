# =================================================================================

"""

===========================================================
Python Functions — Returning Multiple Values
===========================================================

A function can return more than one value.

Example:

def get_user():
    return "Muskan", "Developer"

name, role = get_user()

print(name)
print(role)

Output:

Muskan
Developer


The returned values can be stored in multiple variables.

The returned values are internally represented as a tuple:

("Muskan", "Developer")


Example:

def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference

total, difference = calculate(20, 5)

Output:

total = 25
difference = 15


Key Point:

return value1, value2

can be received as:

variable1, variable2 = function_call()


This is commonly called tuple unpacking.


Mental Model:

Function
    ↓
returns multiple values
    ↓
(value1, value2)
    ↓
variable1, variable2

"""