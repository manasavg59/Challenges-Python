# 160. Write a Python Program to generate random numbers within a range.
import random

low = int(input("Enter start of range: "))
high = int(input("Enter end of range: "))
print("Random number within range =", random.randrange(low, high + 1))