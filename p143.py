# 143. Write a Python Program to find cube root of a number.
number = float(input("Enter a number: "))
if number >= 0:
    root = number ** (1 / 3)
else:
    root = -((-number) ** (1 / 3))
print("Cube root =", round(root, 4))