# Program Name: Find the Smallest Element in a List

numbers = [10, 25, 7, 45, 18]

smallest = numbers[0]

for num in numbers:

    if num < smallest:
        smallest = num

print("Smallest element:", smallest)