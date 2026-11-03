# 205. Write a Python Program to check if a number is palindrome using recursion.
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

number = int(input("Enter a number: "))
if number == reverse_number(number):
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")