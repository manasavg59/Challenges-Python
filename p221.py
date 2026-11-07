# 221. Write a Python Program to implement linear search.
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = list(map(int, input("Enter numbers separated by space: ").split()))
key = int(input("Enter the number to search: "))
index = linear_search(arr, key)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")