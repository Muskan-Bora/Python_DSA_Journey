# =======================================

"""
🐍 Problem 1 — Mixed List + String Revision

Given:

names = ["Muskan", "Aarav", "Doraemon", "Python", "AI", "Developer"]

Task:

Create a new list containing names that:

1. Have more than 5 characters
2. Start with an uppercase letter
3. Contain the letter "o"

Store the matching names in lowercase.

Expected output:

["doraemon", "python", "developer"]

Requirements:

✅ Use a list
✅ Use a for loop
✅ Use an if condition
✅ Use len()
✅ Use string methods
✅ Use "in"
✅ Create a new result list

❌ Do not use zip()
❌ No list comprehension for this problem
"""

names = ["Muskan", "Aarav", "Doraemon", "Python", "AI", "Developer"]

result  = []

for name in names:
    if len(name) > 5 and name[0].isupper() and "o" in name:
        result.append(name.lower())

print(result)

"""
Output:
['doraemon', 'python', 'developer']
"""

# ============================================
