# 152. Write a Python Program to generate a random password.
import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(characters)
print("Random password =", password)