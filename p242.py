# 242. Write a Python Program to calculate standard deviation of a list.
import math

arr = list(map(float, input("Enter numbers separated by space: ").split()))
mean = sum(arr) / len(arr)

total = 0
for x in arr:
    total += (x - mean) ** 2
variance = total / len(arr)

std_dev = math.sqrt(variance)
print("Standard deviation =", std_dev)