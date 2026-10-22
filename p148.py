# 148. Write a Python Program to shuffle elements of a list.
import random

items = [1, 2, 3, 4, 5, 6]
print("Original list =", items)
random.shuffle(items)
print("Shuffled list =", items)