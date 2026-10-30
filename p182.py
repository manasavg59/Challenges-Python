# 182. Write a Python Program to check if a string is palindrome using function.
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")