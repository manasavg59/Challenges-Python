# Program Name: Append Text to a File

file = open("sample.txt", "a")

file.write("\nThis is appended text.")

file.close()

print("Text appended successfully.\n")