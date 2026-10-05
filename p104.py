# Program 104: Check if an Element Exists in a Tuple

numbers = (10, 20, 30, 40, 50)

num = int(input("Enter a number: "))

if num in numbers:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")