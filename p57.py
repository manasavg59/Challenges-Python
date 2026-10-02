# Program Name: Print Pascal's Triangle

n = int(input("Enter number of rows: "))

for i in range(n):

    number = 1

    print(" " * (n - i), end="")

    for j in range(i + 1):

        print(number, end=" ")

        number = number * (i - j) // (j + 1)

    print()




print("\n")
