# 250. Write a Python Program to implement priority queue using list.
# Lower priority number = higher priority (served first).
pq = []

while True:
    print("\n1. Insert  2. Remove highest priority  3. Display  4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        priority = int(input("Enter priority (lower number = higher priority): "))
        pq.append((priority, item))
        pq.sort(key=lambda pair: pair[0])   # keep sorted by priority
        print(item, "added with priority", priority)
    elif choice == 2:
        if len(pq) == 0:
            print("Priority queue is empty")
        else:
            priority, item = pq.pop(0)
            print("Removed element =", item, "(priority", priority, ")")
    elif choice == 3:
        if len(pq) == 0:
            print("Priority queue is empty")
        else:
            print("Priority queue (priority, element) =", pq)
    elif choice == 4:
        break
    else:
        print("Invalid choice")