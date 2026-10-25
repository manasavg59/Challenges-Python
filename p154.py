# 154. Write a Python Program to generate a random prime number.
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

low = int(input("Enter start of range: "))
high = int(input("Enter end of range: "))
primes = [n for n in range(low, high + 1) if is_prime(n)]
if primes:
    print("Random prime number =", random.choice(primes))
else:
    print("No prime numbers in this range")