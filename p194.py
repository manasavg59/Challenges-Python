# 194. Write a Python Program to check if a string contains only special characters.
text = input("Enter a string: ")
only_special = len(text) > 0
for ch in text:
    if ch.isalnum() or ch.isspace():
        only_special = False
        break

if only_special:
    print("The string contains only special characters")
else:
    print("The string does not contain only special characters")