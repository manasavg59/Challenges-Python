# 230. Write a Python Program to implement radix sort.
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if len(arr) == 0:
        return
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

# Works for non-negative integers
arr = list(map(int, input("Enter non-negative numbers separated by space: ").split()))
radix_sort(arr)
print("Sorted list =", arr)