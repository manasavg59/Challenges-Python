# 203. Write a Python Program to check if a number is Armstrong using recursion.
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

def armstrong_sum(n, power):
    if n == 0:
        return 0
    return (n % 10) ** power + armstrong_sum(n // 10, power)

number = int(input("Enter a number: "))
if armstrong_sum(number, count_digits(number)) == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")