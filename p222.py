# 222. Write a Python Program to implement binary search.
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter numbers separated by space: ").split()))
arr.sort()   # binary search needs a sorted list
print("Sorted list =", arr)
key = int(input("Enter the number to search: "))
index = binary_search(arr, key)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")