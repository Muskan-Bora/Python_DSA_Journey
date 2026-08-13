# ============================================================================

"""

# Python Functions — Default Parameters

Topic:
Default Parameters in Functions

---

1. What is a Default Parameter?

---

Definition:

A default parameter is a parameter that already has a default value assigned to it when the function is defined.

If the caller does not provide a value for that parameter, Python automatically uses the default value.

Syntax:

def function_name(parameter="default_value"):
# function body

---

2. Simple Example

---

Example:

def greet(name="Muskan"):
print(f"Hello {name}")

greet()

Output:

Hello Muskan

Explanation:

The function is defined with:

name = "Muskan"

Because we called:

greet()

without providing a value for `name`, Python uses the
default value:

name = "Muskan"

---

3. Providing a Value

---

A default parameter does NOT mean the value can never change.

We can provide another value when calling the function.

Example:

def greet(name="Muskan"):
print(f"Hello {name}")

greet("Doraemon")

Output:

Hello Doraemon

Here, we provided:

"Doraemon"

So Python uses the provided value instead of the default value.

Therefore:

name = "Doraemon"

---

4. Default Value vs Provided Value

---

Example:

def greet(name="Muskan"):
print(f"Hello {name}")

greet()
greet("Doraemon")

Output:

Hello Muskan
Hello Doraemon

First call:

greet()

No argument is provided.

Therefore:

name = "Muskan"

Second call:

greet("Doraemon")

An argument is provided.

Therefore:

name = "Doraemon"

---

5. Why Do We Use Default Parameters?

---

Default parameters are useful when a parameter usually has a common or standard value, but we still want the
option to provide a different value.

Example:

def welcome(name="Guest"):
print(f"Welcome, {name}")

welcome()
welcome("Muskan")

Output:

Welcome, Guest
Welcome, Muskan

This is useful because the caller does not always need
to provide a value.

---

6. Default Parameter with Multiple Parameters

---

A function can have multiple parameters where one or
more parameters have default values.

Example:

def employee(name, company="SWT Club"):
print(f"Employee: {name}")
print(f"Company: {company}")

employee("Muskan")

Output:

Employee: Muskan
Company: SWT Club

Here:

name = "Muskan"

company = "SWT Club"

The company value was not provided, so Python used the
default value.

---

7. Overriding the Default Value

---

We can provide a different value for a default parameter.

Example:

def employee(name, company="SWT Club"):
print(f"Employee: {name}")
print(f"Company: {company}")

employee("Muskan", "Google")

Output:

Employee: Muskan
Company: Google

Here, the provided argument:

"Google"

replaces the default value:

"SWT Club"

So:

name = "Muskan"
company = "Google"

---

8. Default Parameters + return

---

Default parameters can also be used with `return`.

Example:

def calculate_price(price, tax=10):
return price + tax

result = calculate_price(100)

print(result)

Output:

110

Explanation:

price = 100
tax = 10

Because no value was provided for `tax`, Python used:

tax = 10

Calculation:

100 + 10 = 110

The function returns:

110

Therefore:

result = 110

---

9. Important Rule — Parameter Order

---

A parameter with a default value should come AFTER parameters that do not have default values.

Correct:

def employee(name, company="SWT Club"):
print(name)
print(company)

Incorrect:

def employee(company="SWT Club", name):
print(name)
print(company)

Python will raise a SyntaxError because a required parameter cannot come after a default parameter.

Correct structure:

def function(required_parameter, default_parameter="value"):
...

---

10. How Python Thinks About a Default Parameter

---

Example:

def greet(name="Guest"):
print(f"Hello {name}")

When we call:

greet()

Python thinks:

"Was a value provided for name?"

No.

Therefore:

name = "Guest"

But when we call:

greet("Muskan")

Python thinks:

"Was a value provided for name?"

Yes.

Therefore:

name = "Muskan"

The provided argument always takes priority over the
default value.

---

11. Mental Model

---

Think of a default parameter as a FALLBACK value.

Example:

def greet(name="Guest"):
...

No value provided:
↓
Use default
↓
name = "Guest"

Value provided:
↓
Use provided value
↓
name = provided value

---

12. Quick Comparison

---

Normal parameter:

def greet(name):
print(name)

greet()

This causes an error because `name` is required.

Default parameter:

def greet(name="Guest"):
print(name)

greet()

Output:

Guest

The default parameter allows the function to work even
when the caller does not provide that argument.

---

13. Key Points to Remember

---

1. A default parameter has a value assigned when the function is defined.

2. If the caller does not provide a value, Python uses the default value.

3. If the caller provides a value, the provided value replaces the default value.

4. Default parameters are useful for common or fallback values.

5. A function can have multiple default parameters.

6. Required parameters should come before default parameters.

7. Default parameters can be used with `return`.

8. Think of a default parameter as a FALLBACK value.

===========================================================
Quick Example
=============

def greet(name="Guest"):
return f"Hello, {name}"

message1 = greet()

message2 = greet("Muskan")

print(message1)
print(message2)

Output:

Hello, Guest
Hello, Muskan

===========================================================
End of Notes
============

"""

# ===================================================

"""
Problem 1 — Default Parameter
Problem Statement

Create a function named:

def welcome(name="Guest"):
The function should print:

Welcome, <name>!
Requirements
Call the function three times:
Without an argument
With "Muskan"
With "Doraemon"
"""

def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()
welcome("Muskan")
welcome("Doraemon")

"""
Output:
Welcome, Guest!
Welcome, Muskan!
Welcome, Doraemon!
"""

# ===========================================

"""
🔄 Functions Revision — Problem 1
🧩 Problem: calculate_discount()

Create a function named:

def calculate_discount(price, discount):
Requirements

The function should:

Accept price as a parameter.
Accept discount as a parameter.
Calculate the discount amount:
price × discount / 100
Return the discount amount.

Then:

Call the function with:
price = 1000
discount = 20
Store the returned value in a variable named discount_amount
Print discount_amount
Expected output
200.0
"""

def calculate_discount(price, discount):
    return price * discount / 100

price = 1000
discount = 20

discount_amount = calculate_discount(price, discount)

print(discount_amount)

"""
Output:
200.0
"""

# ==================================

"""
Functions Revision — Problem 2

Create:

def welcome(name="Guest"):

The function should return:

Welcome, <name>!

Then:

Call 1
message1 = welcome()
Call 2
message2 = welcome("Muskan")

Print both messages.
"""

def welcome(name="Guest"):
    return f"Welcome, {name}!"


message1 = welcome()
message2 = welcome("Muskan")

print(message1)
print(message2)

"""
Output:
Welcome Guest!
Welcome Muskan!
"""

# ================================================