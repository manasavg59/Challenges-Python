# 202. Write a Python Program to check if a string is palindrome using recursion.
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

text = input("Enter a string: ").lower()
if is_palindrome(text):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")