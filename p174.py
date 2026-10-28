# 174. Write a Python Program to reverse a set.
# Sets are unordered, so we convert to a list to reverse the order.
my_set = {1, 2, 3, 4, 5}
print("Original set =", my_set)
reversed_list = list(my_set)[::-1]
print("Reversed elements =", reversed_list)