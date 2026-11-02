# 200. Write a Python Program to check if a string contains all vowels.
text = input("Enter a string: ").lower()
contains_all = True
for vowel in "aeiou":
    if vowel not in text:
        contains_all = False
        break

if contains_all:
    print("The string contains all vowels")
else:
    print("The string does not contain all vowels")