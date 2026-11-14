# 249. Write a Python Program to implement deque using list.
deque = []

while True:
    print("\n1. Insert at front  2. Insert at rear  3. Delete from front")
    print("4. Delete from rear  5. Display  6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        deque.insert(0, item)
    elif choice == 2:
        item = input("Enter element: ")
        deque.append(item)
    elif choice == 3:
        if len(deque) == 0:
            print("Deque is empty")
        else:
            print("Deleted from front =", deque.pop(0))
    elif choice == 4:
        if len(deque) == 0:
            print("Deque is empty")
        else:
            print("Deleted from rear =", deque.pop())
    elif choice == 5:
        if len(deque) == 0:
            print("Deque is empty")
        else:
            print("Deque (front to rear) =", deque)
    elif choice == 6:
        break
    else:
        print("Invalid choice")



        