# Program Name: Check Whether a Number is an Armstrong Number

n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:

    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")