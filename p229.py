# 229. Write a Python Program to implement counting sort.
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1

    result = []
    for value in range(len(count)):
        result.extend([value] * count[value])
    return result

# Works for non-negative integers
arr = list(map(int, input("Enter non-negative numbers separated by space: ").split()))
print("Sorted list =", counting_sort(arr))