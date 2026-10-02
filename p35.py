# Program Name: Find the LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = a * b

while b != 0:
    remainder = a % b
    a = b
    b = remainder

gcd = a

lcm = lcm // gcd

print("LCM:", lcm)