# 178. Write a Python Program to reverse digits of a number.
number = int(input("Enter a number: "))
reversed_number = int(str(abs(number))[::-1])
if number < 0:
    reversed_number = -reversed_number
print("Reversed number =", reversed_number)