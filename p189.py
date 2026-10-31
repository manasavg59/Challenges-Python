# 189. Write a Python Program to check if a string contains only alphabets.
def contains_only_alphabets(text):
    return text.isalpha()

text = input("Enter a string: ")
if contains_only_alphabets(text):
    print("The string contains only alphabets")
else:
    print("The string does not contain only alphabets")