# Program Name: Function to Check Whether a Number is Prime

def is_prime(n):

    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")


print("\n")    