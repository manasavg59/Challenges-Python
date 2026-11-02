# 199. Write a Python Program to check if a string contains unique characters.
text = input("Enter a string: ")
if len(set(text)) == len(text):
    print("The string contains all unique characters")
else:
    print("The string does not contain all unique characters")