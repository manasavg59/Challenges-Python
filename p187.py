# 187. Write a Python Program to check if a string is pangram using function.
import string

def is_pangram(text):
    text = text.lower()
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
    return True

text = input("Enter a string: ")
if is_pangram(text):
    print("The string is a pangram")
else:
    print("The string is not a pangram")