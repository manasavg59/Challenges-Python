# 239. Write a Python Program to find the median of a list.
arr = list(map(float, input("Enter numbers separated by space: ").split()))
arr.sort()
n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print("Median =", median)