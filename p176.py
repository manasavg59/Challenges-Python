# 176. Write a Python Program to reverse characters in each word of a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
result = " ".join(word[::-1] for word in words)
print("Result =", result)