# 236. Write a Python Program to remove an element from a list.
arr = list(map(int, input("Enter numbers separated by space: ").split()))
key = int(input("Enter the element to remove: "))

if key in arr:
    arr.remove(key)   # removes the first occurrence
    print("List after removing =", arr)
else:
    print("Element not found in the list")