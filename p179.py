# 179. Write a Python Program to reverse elements of a nested list.
def reverse_nested(lst):
    result = []
    for item in reversed(lst):
        if isinstance(item, list):
            result.append(reverse_nested(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print("Original nested list =", nested)
print("Reversed nested list =", reverse_nested(nested))