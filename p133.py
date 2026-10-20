# 133. Write a Python Program to count uppercase letters in a string.
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Number of uppercase letters =", count)