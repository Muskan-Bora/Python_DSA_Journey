# ====================================================

# Stage 1 — Mixed set methods

"""
Question 1
The student registration scenario

You are given two sets:
python_students = {"Amit", "Riya", "Neha", "Karan", "Priya"}
java_students = {"Riya", "Karan", "Rahul", "Sneha"}

Write a Python program that:
1. Prints both original sets.
2. Finds students enrolled in both Python and Java.
3. Finds students enrolled in Python only.
4. Finds all unique students enrolled in either course.
5. Creates a copy of python_students named updated_python.
6. Adds "Anjali" to updated_python.
7. Removes "Neha" from updated_python using discard().
8. Prints the updated set and verifies that the original python_students remains unchanged.

Your usual coding format:
- Blank print() at the beginning.
- Clear f-string messages.
- Output comment showing a valid possible result.
- Separator at the end.

Concepts being tested: intersection(), difference(), union(), copy(), add(), and discard().
"""

python_students = {"Amit", "Riya", "Neha", "Karan", "Priya"}
java_students = {"Riya", "Karan", "Rahul", "Sneha"}

print(f"Original set of python_students: {python_students}")
print(f"Original set of java_students: {java_students}")

print()

print(f"Students enrolled in both Python and Java: {python_students.intersection(java_students)}")

print(f"Student enrolled in python only: {python_students.difference(java_students)}")

print(f"All unique students enrolled in either course: {python_students | java_students}")

updated_python = python_students.copy()

updated_python.add("Anjali")

print(f"Add Anjali on updated_python: {updated_python}")

updated_python.discard("Neha")

print(f"Removed Neha from updated_python: {updated_python}")

print()

print(f"Verifying the original sets remain unchanged")

print(f"Original set of python_students: {python_students}")
print(f"Original set of java_students: {java_students}")

"""
Final Output:
Original set of python_students: {'Amit', 'Karan', 'Neha', 'Riya', 'Priya'}
Original set of java_students: {'Rahul', 'Riya', 'Sneha', 'Karan'}

Students enrolled in both Python and Java: {'Riya', 'Karan'}
Student enrolled in python only: {'Amit', 'Neha', 'Priya'}
All unique students enrolled in either course: {'Amit', 'Riya', 'Priya', 'Karan', 'Neha', 'Rahul', 'Sneha'}
Add Anjali on updated_python: {'Amit', 'Karan', 'Neha', 'Anjali', 'Riya', 'Priya'}
Removed Neha from updated_python: {'Amit', 'Karan', 'Anjali', 'Riya', 'Priya'}

Verifying the original sets remain unchanged
Original set of python_students: {'Amit', 'Karan', 'Neha', 'Riya', 'Priya'}
Original set of java_students: {'Rahul', 'Riya', 'Sneha', 'Karan'}
"""

# ================================================

"""
Question 2
Inventory management scenario

Imagine you are managing an inventory system.
warehouse_a = {"Laptop", "Mouse", "Keyboard", "Monitor", "Printer"}
warehouse_b = {"Mouse", "Keyboard", "Scanner", "Webcam"}

Write a Python program that:
1. Prints both original warehouse sets.
2. Finds products available in both warehouses.
3. Finds products available only in Warehouse B.
4. Finds products available in Warehouse A but not in Warehouse B.
5. Creates a copy of warehouse_a named final_inventory.
6. Applies symmetric_difference_update() using warehouse_b on final_inventory.
7. Prints the updated final_inventory.
8. Prints both original warehouse sets again to verify they remain unchanged.
9. Prints the length of final_inventory.
Your usual format:
- Blank print() at the beginning.
- Clear f-string messages.
- Output comment showing a valid possible result.
- Separator at the end.
Concepts being tested: intersection(), difference(), copy(), symmetric_difference_update(), and len().
"""

print()

warehouse_a = {"Laptop", "Mouse", "Keyboard", "Monitor", "Printer"}
warehouse_b = {"Mouse", "Keyboard", "Scanner", "Webcam"}

print(f"Original set of warehouse_a: {warehouse_a}")

print(f"Original set of warehouse_b: {warehouse_b}")

print()

print(f"Products available in both warehouses: {warehouse_a & warehouse_b}")

print(f"Products available only in Warehouse B: {warehouse_b.difference(warehouse_a)}")

print(f"Products available in Warehouse A but not in Warehouse B: {warehouse_a.difference(warehouse_b)}")

print()

final_inventory = warehouse_a.copy()

final_inventory.symmetric_difference_update(warehouse_b)

print(f"The updated final_inventory: {final_inventory}")

print()

print("Verifying that both original warehouse sets remain unchanged:")

print(f"Original set of warehouse_a: {warehouse_a}")

print(f"Original set of warehouse_b: {warehouse_b}")

print()

print(f"The length of the final_inventory : {len(final_inventory)}")

"""
Final output:
Original set of warehouse_a: {'Mouse', 'Monitor', 'Printer', 'Laptop', 'Keyboard'}
Original set of warehouse_b: {'Mouse', 'Keyboard', 'Webcam', 'Scanner'}

Products available in both warehouses: {'Mouse', 'Keyboard'}
Products available only in Warehouse B: {'Scanner', 'Webcam'}
Products available in Warehouse A but not in Warehouse B: {'Monitor', 'Printer', 'Laptop'}

The updated final_inventory: {'Monitor', 'Printer', 'Laptop', 'Webcam', 'Scanner'}

Verifying that both original warehouse sets remain unchanged:
Original set of warehouse_a: {'Mouse', 'Monitor', 'Printer', 'Laptop', 'Keyboard'}
Original set of warehouse_b: {'Mouse', 'Keyboard', 'Webcam', 'Scanner'}

The length of the final_inventory : 5
"""

# ==========================================