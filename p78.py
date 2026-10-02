# Program 78: Find Sum of Digits Using Recursion

def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)

n = int(input("Enter a number: "))

result = sum_digits(n)

print("Sum of digits:", result)