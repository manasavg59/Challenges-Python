# Program 99: Sort a Dictionary by Values

students = {
    "Rahul": 85,
    "Priya": 95,
    "Arun": 78,
    "Sneha": 90
}

sorted_students = dict(sorted(students.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:", sorted_students)