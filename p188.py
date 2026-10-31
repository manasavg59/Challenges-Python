# 188. Write a Python Program to check if a string contains only digits.
def contains_only_digits(text):
    return text.isdigit()

text = input("Enter a string: ")
if contains_only_digits(text):
    print("The string contains only digits")
else:
    print("The string does not contain only digits")