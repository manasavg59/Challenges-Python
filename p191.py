# 191. Write a Python Program to check if a string contains only uppercase letters.
text = input("Enter a string: ")
if text.isalpha() and text.isupper():
    print("The string contains only uppercase letters")
else:
    print("The string does not contain only uppercase letters")