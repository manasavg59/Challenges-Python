# 198. Write a Python Program to check if a string contains repeated characters.
text = input("Enter a string: ")
if len(set(text)) != len(text):
    print("The string contains repeated characters")
else:
    print("The string does not contain repeated characters")