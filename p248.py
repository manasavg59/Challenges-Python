# 248. Write a Python Program to implement circular queue using list.
size = int(input("Enter size of circular queue: "))
queue = [None] * size
front = 0
rear = -1
count = 0

while True:
    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if count == size:
            print("Queue is full (overflow)")
        else:
            item = input("Enter element to enqueue: ")
            rear = (rear + 1) % size
            queue[rear] = item
            count += 1
            print(item, "added to queue")
    elif choice == 2:
        if count == 0:
            print("Queue is empty (underflow)")
        else:
            print("Dequeued element =", queue[front])
            queue[front] = None
            front = (front + 1) % size
            count -= 1
    elif choice == 3:
        if count == 0:
            print("Queue is empty")
        else:
            items = []
            for i in range(count):
                items.append(queue[(front + i) % size])
            print("Queue (front to rear) =", items)
    elif choice == 4:
        break
    else:
        print("Invalid choice")