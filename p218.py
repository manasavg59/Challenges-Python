# 218. Write a Python Program to check if a string contains repeated characters using recursion.
def has_repeated(text):
    if len(text) <= 1:
        return False
    if text[0] in text[1:]:
        return True
    return has_repeated(text[1:])

text = input("Enter a string: ")
if has_repeated(text):
    print("The string contains repeated characters")
else:
    print("The string does not contain repeated characters")