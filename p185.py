# 185. Write a Python Program to check if a number is palindrome using function.
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

number = int(input("Enter a number: "))
if is_palindrome_number(number):
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")