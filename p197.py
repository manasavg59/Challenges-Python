# 197. Write a Python Program to check if a string contains both vowels and consonants.
text = input("Enter a string: ").lower()
has_vowel = False
has_consonant = False
for ch in text:
    if ch in "aeiou":
        has_vowel = True
    elif ch.isalpha():
        has_consonant = True

if has_vowel and has_consonant:
    print("The string contains both vowels and consonants")
else:
    print("The string does not contain both vowels and consonants")