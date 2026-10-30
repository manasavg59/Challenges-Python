# 184. Write a Python Program to check if a number is perfect using function.
def is_perfect(n):
    if n < 2:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

number = int(input("Enter a number: "))
if is_perfect(number):
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")