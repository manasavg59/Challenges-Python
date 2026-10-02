# Program 100: Check if a Key Exists in a Dictionary

students = {
    "Rahul": 85,
    "Priya": 90,
    "Arun": 78
}

key = input("Enter student name: ")

if key in students:
    print("Key exists")
else:
    print("Key does not exist")