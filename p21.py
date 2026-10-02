# Program Name: Find the Largest Element in a List

numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

print("Largest element:", largest)