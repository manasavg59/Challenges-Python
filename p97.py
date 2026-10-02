# Program 97: Count Frequency of Words in a Sentence Using Dictionary

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)