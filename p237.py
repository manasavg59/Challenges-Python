# 237. Write a Python Program to insert an element at a specific position in a list.
arr = list(map(int, input("Enter numbers separated by space: ").split()))
element = int(input("Enter the element to insert: "))
index = int(input("Enter the index at which to insert: "))

arr.insert(index, element)
print("List after inserting =", arr)