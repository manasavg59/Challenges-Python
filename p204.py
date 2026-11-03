# 204. Write a Python Program to check if a number is perfect using recursion.
def divisor_sum(n, i=1):
    if i >= n:
        return 0
    if n % i == 0:
        return i + divisor_sum(n, i + 1)
    return divisor_sum(n, i + 1)

number = int(input("Enter a number: "))
if number > 1 and divisor_sum(number) == number:
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")