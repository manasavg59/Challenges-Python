# 180. Write a Python Program to reverse elements of a nested dictionary.
def reverse_nested_dict(d):
    result = {}
    for key in reversed(list(d.keys())):
        value = d[key]
        if isinstance(value, dict):
            result[key] = reverse_nested_dict(value)
        else:
            result[key] = value
    return result

nested = {"a": 1, "b": {"x": 10, "y": 20, "z": 30}, "c": 3}
print("Original nested dictionary =", nested)
print("Reversed nested dictionary =", reverse_nested_dict(nested))