# 123. Write a Python Program to calculate volume of a cylinder.
import math

radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
volume = math.pi * radius ** 2 * height
print("Volume of cylinder =", volume)