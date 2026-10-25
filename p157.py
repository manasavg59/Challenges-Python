# 157. Write a Python Program to generate a random string of given length.
import random
import string

length = int(input("Enter length of string: "))
result = ""
for i in range(length):
    result += random.choice(string.ascii_letters)
print("Random string =", result)