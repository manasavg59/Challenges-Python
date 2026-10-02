# Program 77: Find LCM of Two Numbers Using Recursion

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = (a * b) // gcd(a, b)

print("LCM:", lcm)