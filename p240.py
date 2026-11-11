# 240. Write a Python Program to find the mode of a list.
arr = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}
for item in arr:
    frequency[item] = frequency.get(item, 0) + 1

max_count = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_count]

print("Mode =", modes)