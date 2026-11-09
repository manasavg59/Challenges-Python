# 227. Write a Python Program to implement quick sort.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sorted list =", quick_sort(arr))