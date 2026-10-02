# Program Name: Rotate a List by K Positions

numbers = [1, 2, 3, 4, 5]
k = 2

rotated = numbers[-k:] + numbers[:-k]

print("Rotated list:", rotated)