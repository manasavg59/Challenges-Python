# 142. Write a Python Program to find the square root of a number.
import math

number = float(input("Enter a number: "))
if number >= 0:
    print("Square root =", math.sqrt(number))
else:
    print("Square root of a negative number is not real")