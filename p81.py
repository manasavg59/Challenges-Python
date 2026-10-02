# Program 81: Find Maximum Element in a Tuple

numbers = (10, 25, 7, 45, 18)

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum element:", maximum)