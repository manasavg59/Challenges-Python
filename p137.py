# 137. Write a Python Program to remove punctuation from a string.
import string

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in string.punctuation:
        result += ch
print("String without punctuation =", result)