# Program 98: Find the Key with Maximum Value in a Dictionary

students = {
    "Rahul": 85,
    "Priya": 95,
    "Arun": 78
}

maximum_key = max(students, key=students.get)

print("Key with maximum value:", maximum_key)
print("Maximum value:", students[maximum_key])