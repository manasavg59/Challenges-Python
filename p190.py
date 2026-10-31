# 190. Write a Python Program to check if a string contains only alphanumeric characters.
def contains_only_alphanumeric(text):
    return text.isalnum()

text = input("Enter a string: ")
if contains_only_alphanumeric(text):
    print("The string contains only alphanumeric characters")
else:
    print("The string does not contain only alphanumeric characters")