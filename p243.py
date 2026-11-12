# 243. Write a Python Program to calculate variance of a list.
arr = list(map(float, input("Enter numbers separated by space: ").split()))
mean = sum(arr) / len(arr)

total = 0
for x in arr:
    total += (x - mean) ** 2
variance = total / len(arr)

print("Variance =", variance)