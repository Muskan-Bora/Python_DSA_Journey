# =========================================================

# Python Functions — Return Statement

"""

Topic:
return statement

The return statement is one of the most important concepts in Python functions because it allows a function to send a
value/result back to the place where the function was called.

---

1. What is return?

---

Definition:

The `return` statement is used inside a function to send a value back to the caller of that function.

When Python reaches `return`, the function immediately stops executing and sends the specified value back.

Syntax:

def function_name():
return value

---

2. Simple Example

---

Example:

def add():
return 10 + 20

result = add()

print(result)

Output:

30

Explanation:

Step 1:
The function `add()` is created.

Step 2:
`add()` is called:

result = add()

Step 3:
The function calculates:

10 + 20 = 30

Step 4:
`return 30` sends the value 30 back to the caller.

Step 5:
The returned value is stored in:

result

Therefore:

result = 30

---

3. return vs print()

---

This is a VERY important difference.

Using print():

def add():
print(10 + 20)

add()

Output:

30

Here, `print()` only displays the result on the screen.

The function does NOT give the result back to the caller
for further use.

Using return:

def add():
return 10 + 20

result = add()

print(result)

Output:

30

Here, `return` sends the value 30 back to the caller.

The returned value can then be:

```
- stored in a variable
- printed
- used in another calculation
- passed to another function
- used inside a condition
- used elsewhere in the program
```

---

4. Why do we use return?

---

We use `return` when a function needs to produce a result
that another part of the program can use.

Example:

def multiply(a, b):
return a * b

result = multiply(5, 4)

print(result)

Output:

20

Here:

a = 5
b = 4

The function calculates:

5 * 4 = 20

Then:

return 20

sends the result back.

Therefore:

result = 20

---

5. return with Parameters

---

A function can accept parameters and return a result.

Example:

def square(number):
return number * number

result = square(5)

print(result)

Output:

25

Explanation:

When we call:

square(5)

Python maps:

number = 5

Then the function calculates:

5 * 5 = 25

The function returns:

25

Therefore:

result = 25

---

6. return Stops Function Execution

---

When Python reaches a `return` statement, the function
immediately stops executing.

Example:

def test():
print("Start")
return 100
print("End")

result = test()

print(result)

Output:

Start
100

"End" is never printed because the function stopped when
Python reached:

return 100

---

7. Returning Different Types of Values

---

A function can return many types of values.

Integer:

def get_number():
return 10

String:

def get_name():
return "Muskan"

Boolean:

def is_active():
return True

List:

def get_numbers():
return [1, 2, 3, 4, 5]

The returned value can then be stored and used.

Example:

name = get_name()

print(name)

Output:

Muskan

---

8. Function with Calculation and return

---

Example:

def calculate_total(price, quantity):
return price * quantity

total = calculate_total(500, 3)

print(total)

Output:

1500

Parameter mapping:

price = 500
quantity = 3

Calculation:

500 * 3 = 1500

Returned value:

1500

Stored in:

total

---

9. Important Concept

---

A function does not have to print something.

A function can calculate something and return the result.

Example:

def add(a, b):
return a + b

result = add(10, 20)

print(result)

Output:

30

The function's job is:

```
Take input
    ↓
Process the input
    ↓
Return the result
```

This pattern is extremely common in real Python programs.

---

10. Quick Comparison

---

print():

```
Function
    ↓
Display result
    ↓
Nothing is returned automatically
```

return:

```
Function
    ↓
Produce result
    ↓
Send result back to caller
    ↓
Result can be stored and reused
```

---

11. Key Points to Remember

---

1. `return` sends a value back to the caller.

2. `return` can be used inside a function.

3. When Python reaches `return`, the function stops
   executing immediately.

4. The returned value can be stored in a variable.

5. The returned value can be used in calculations,
   conditions, other functions, etc.

6. `print()` displays a value.

7. `return` gives a value back to the caller.

8. A function can use parameters and return a result.

9. A function can return different data types such as
   integers, strings, lists, booleans, etc.

10. `return` is different from `print()`.

===========================================================
Mental Model
============

Think of a function like a machine:

```
    Input
      ↓
┌─────────────┐
│   FUNCTION  │
│             │
│  Processing │
└─────────────┘
      ↓
   return
      ↓
    Result
```

Example:

```
5 ─────→ square() ─────→ 25

        5 x 5
          ↓
      return 25
```

===========================================================
End of Notes
============

"""

# ============================================================

"""
Problem 1 — Basic return

Write a function named:

get_number()
Requirements

The function should:

Return the number 100.
Store the returned value in a variable called result.
Print result.
Expected output
100
"""

def get_number():
    return 100

result = get_number()

print(result)

"""
Output:
100
"""

# =================================

"""
Problem 2 — return + Parameter

Problem Statement

Create a function:
def double(number):

The function should:
Take one parameter called number 
Return double the number

Then:

Call the function with 5
Store the returned value in result
Print result
Expected output
10
"""

def double(number):
    return(number * 2)

number = 5

result = double(number)
print(result)

"""
Output:
10
"""

# ==================================================