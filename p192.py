# 192. Write a Python Program to check if a string contains only lowercase letters.
text = input("Enter a string: ")
if text.isalpha() and text.islower():
    print("The string contains only lowercase letters")
else:
    print("The string does not contain only lowercase letters")