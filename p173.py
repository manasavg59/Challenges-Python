# 173. Write a Python Program to reverse a dictionary.
my_dict = {"a": 1, "b": 2, "c": 3}
print("Original dictionary =", my_dict)

# Reverse the order of items
reversed_dict = dict(reversed(list(my_dict.items())))
print("Reversed dictionary (order) =", reversed_dict)

# Swap keys and values
swapped_dict = {value: key for key, value in my_dict.items()}
print("Reversed dictionary (keys <-> values) =", swapped_dict)