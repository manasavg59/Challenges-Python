# 140. Write a Python Program to join words into a sentence.
words = input("Enter words separated by comma: ").split(",")
sentence = " ".join(word.strip() for word in words)
print("Sentence =", sentence)