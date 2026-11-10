# 231. Write a Python Program to find the largest element using linear search.
arr = list(map(int, input("Enter numbers separated by space: ").split()))

largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element =", largest)