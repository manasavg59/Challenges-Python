# 232. Write a Python Program to find the smallest element using linear search.
arr = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = arr[0]
for i in range(1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element =", smallest)