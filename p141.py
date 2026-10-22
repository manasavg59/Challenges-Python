# 141. Write a Python Program to check if a number is divisible by another.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if b != 0 and a % b == 0:
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", b)