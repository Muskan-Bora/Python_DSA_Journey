# ================================================

"""
print() vs return in Functions

# --------------------------

print()

print() displays a value on the screen.

def greet(name):
    print(f"Hello {name}")

The function displays the result but does not return it.

return

return sends a value back to the place where the function was called.

def add(a, b):
    return a + b

The returned value can be stored:

result = add(10, 20)

print(result)

Output:

30
Important Difference
def add(a, b):
    print(a + b)

Here the function prints the result.

But:

def add(a, b):
    return a + b

Here the function returns the result.

Using the Returned Value

A returned value can be used in another calculation:

def add(a, b):
    return a + b

result = add(10, 20)

final_result = result * 2

print(final_result)

Output:

60

Because:

10 + 20 = 30
30 x 2 = 60
What happens when there is no return?

If a function doesn't explicitly return a value, Python returns:

None

Example:

def greet():
    print("Hello")

result = greet()

print(result)

Output:

Hello
None

# --------------------------

⭐ One-Line Rule
print() is for displaying a value; return is for sending a value back from a function so the program can use it.
"""

# =======================================================

"""
🧩 Problem 1 — calculate_square()

Create:

def calculate_square(number):

The function should:

Calculate the square of number.
Return the result.
Do not use print() inside the function.

Then:

result = calculate_square(8)
print(result)
Expected output
64
🚨 Rules

✅ Use a function
✅ Accept number as a parameter
✅ Use return
✅ Store the returned value in result
✅ Print result outside the function
❌ Don't use print() inside the function
❌ Don't hardcode 64
"""
def calculate_square(number):
    return number * number

result = calculate_square(8)
print(result)

"""
Final Output:
64
"""

# ===========================================

"""
🧩 Practical Revision Problem — calculate_discount()

Create:

def calculate_discount(price, discount):
Requirements

The function should:

Calculate the discount amount.
Calculate the final price.
Return the final price.
Do not use print() inside the function.

Then:

result = calculate_discount(1000, 10)
print(result)
Expected output
900.0
🚨 Rules

✅ Use parameters
✅ Use return
✅ Store the returned value in result
✅ Print result outside the function
❌ Don't use print() inside the function
❌ Don't hardcode 900
"""

print()

def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

result = calculate_discount(1000, 10)
print(result)

"""
Output:
900.0
"""

# ==================================================