# Program 82: Find Minimum Element in a Tuple

numbers = (10, 25, 7, 45, 18)

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum element:", minimum)