# Program Name: Function to Return the Sum of Digits of a Number

def sum_digits(n):

    total = 0

    while n > 0:

        digit = n % 10
        total = total + digit
        n = n // 10

    return total


n = int(input("Enter a number: "))

print("Sum of digits:", sum_digits(n))