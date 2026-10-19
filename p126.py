# 126. Write a Python Program to calculate surface area of a cylinder.
import math

radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
surface_area = 2 * math.pi * radius * (radius + height)
print("Surface area of cylinder =", surface_area)