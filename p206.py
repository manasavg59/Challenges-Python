# 206. Write a Python Program to check if a string is anagram using recursion.
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True
    ch = s1[0]
    if ch not in s2:
        return False
    index = s2.index(ch)
    return is_anagram(s1[1:], s2[:index] + s2[index + 1:])

first = input("Enter first string: ").replace(" ", "").lower()
second = input("Enter second string: ").replace(" ", "").lower()
if is_anagram(first, second):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")