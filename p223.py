# 223. Write a Python Program to implement bubble sort.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = list(map(int, input("Enter numbers separated by space: ").split()))
bubble_sort(arr)
print("Sorted list =", arr)