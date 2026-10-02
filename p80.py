# Program 80: Print Numbers from n to 1 Using Recursion

def print_numbers(n):
    if n == 0:
        return

    print(n)

    print_numbers(n - 1)

n = int(input("Enter n: "))

print_numbers(n)