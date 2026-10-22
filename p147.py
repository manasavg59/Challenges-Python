# 147. Write a Python Program to generate random integers between two numbers.
import random

low = int(input("Enter first number: "))
high = int(input("Enter second number: "))
print("Random integer =", random.randint(low, high))