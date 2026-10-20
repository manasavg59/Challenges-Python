# 134. Write a Python Program to count lowercase letters in a string.
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.islower():
        count += 1
print("Number of lowercase letters =", count)