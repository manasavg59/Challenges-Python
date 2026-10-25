# 156. Write a Python Program to generate a random odd number.
import random

number = random.randint(0, 49) * 2 + 1
print("Random odd number =", number)