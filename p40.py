# Program Name: Calculate the Power of a Number Without Using **

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * base

print("Result:", result)