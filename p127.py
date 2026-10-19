# 127. Write a Python Program to calculate surface area of a sphere.
import math

radius = float(input("Enter radius of sphere: "))
surface_area = 4 * math.pi * radius ** 2
print("Surface area of sphere =", surface_area)