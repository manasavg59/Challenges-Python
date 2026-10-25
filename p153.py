# 153. Write a Python Program to generate a random OTP.
import random

otp = ""
for i in range(6):
    otp += str(random.randint(0, 9))
print("Your OTP is:", otp)