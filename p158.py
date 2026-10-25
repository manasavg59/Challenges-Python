# 158. Write a Python Program to generate random alphanumeric string.
import random
import string

length = int(input("Enter length of string: "))
characters = string.ascii_letters + string.digits
result = ""
for i in range(length):
    result += random.choice(characters)
print("Random alphanumeric string =", result)