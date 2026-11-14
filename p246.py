# 246. Write a Python Program to implement stack using list.
stack = []

while True:
    print("\n1. Push  2. Pop  3. Peek  4. Display  5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to push: ")
        stack.append(item)
        print(item, "pushed to stack")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty (underflow)")
        else:
            print("Popped element =", stack.pop())
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element =", stack[-1])
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack (bottom to top) =", stack)
    elif choice == 5:
        break
    else:
        print("Invalid choice")