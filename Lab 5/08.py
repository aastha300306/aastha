def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)
    print(f"{item} has been enqueued.")

def dequeue(queue):
    if not is_empty(queue):
        item = queue.pop(0)  
        print(f"{item} has been dequeued.")
    else:
        print("Queue is empty! Cannot dequeue.")

def peek(queue):
    if not is_empty(queue):
        print(f"Front element is: {queue[0]}")
    else:
        print("Queue is empty! No front element.")

def display(queue):
    if not is_empty(queue):
        print("Queue:", queue)
    else:
        print("Queue is empty.")

def menu():
    queue = []

    while True:
        print("\nQueue Menu:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Peek at the front element")
        print("4. Display the queue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            element = input("Enter the element to enqueue: ")
            enqueue(queue, element)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            peek(queue)
        elif choice == '4':
            display(queue)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

menu()