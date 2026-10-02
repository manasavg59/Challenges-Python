# Program Name: Replace Vowels with *

text = input("Enter a string: ")

result = ""

for ch in text:

    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch

print("Result:", result)