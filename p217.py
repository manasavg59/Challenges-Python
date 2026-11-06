# 217. Write a Python Program to check if a string contains both vowels and consonants using recursion.
def has_vowel_and_consonant(text, has_vowel=False, has_consonant=False):
    if text == "":
        return has_vowel and has_consonant
    if text[0] in "aeiou":
        has_vowel = True
    elif text[0].isalpha():
        has_consonant = True
    return has_vowel_and_consonant(text[1:], has_vowel, has_consonant)

text = input("Enter a string: ").lower()
if has_vowel_and_consonant(text):
    print("The string contains both vowels and consonants")
else:
    print("The string does not contain both vowels and consonants")