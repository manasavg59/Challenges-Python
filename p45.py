# Program Name: Copy Contents from One File to Another

source = open("sample.txt", "r")

destination = open("copy.txt", "w")

content = source.read()

destination.write(content)

source.close()
destination.close()

print("File copied successfully.\n")