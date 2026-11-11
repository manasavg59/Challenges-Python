# 238. Write a Python Program to delete an element at a specific position in a list.
arr = list(map(int, input("Enter numbers separated by space: ").split()))
index = int(input("Enter the index of the element to delete: "))

if 0 <= index < len(arr):
    deleted = arr.pop(index)
    print("Deleted element =", deleted)
    print("List after deleting =", arr)
else:
    print("Invalid index")