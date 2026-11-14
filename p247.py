# 247. Write a Python Program to implement queue using list.
queue = []

while True:
    print("\n1. Enqueue  2. Dequeue  3. Front  4. Display  5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to enqueue: ")
        queue.append(item)
        print(item, "added to queue")
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty (underflow)")
        else:
            print("Dequeued element =", queue.pop(0))
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element =", queue[0])
    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue (front to rear) =", queue)
    elif choice == 5:
        break
    else:
        print("Invalid choice")