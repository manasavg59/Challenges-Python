# 219. Write a Python Program to check if a string contains unique characters using recursion.
def all_unique(text):
    if len(text) <= 1:
        return True
    if text[0] in text[1:]:
        return False
    return all_unique(text[1:])

text = input("Enter a string: ")
if all_unique(text):
    print("The string contains all unique characters")
else:
    print("The string does not contain all unique characters")