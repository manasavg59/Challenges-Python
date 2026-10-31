# 186. Write a Python Program to check if a string is anagram using function.
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

first = input("Enter first string: ")
second = input("Enter second string: ")
if is_anagram(first, second):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")