# 241. Write a Python Program to find the mean of a list.
arr = list(map(float, input("Enter numbers separated by space: ").split()))
mean = sum(arr) / len(arr)
print("Mean =", mean)