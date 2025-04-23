def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(f"{item} has been pushed onto the stack.")

def pop(stack):
    if not is_empty(stack):
        item = stack.pop()
        print(f"{item} has been popped from the stack.")
    else:
        print("Stack is empty! Cannot pop.")

def peek(stack):
    if not is_empty(stack):
        print(f"Top element is: {stack[-1]}")
    else:
        print("Stack is empty! No top element.")

def display(stack):
    if not is_empty(stack):
        print("Stack:", stack)
    else:
        print("Stack is empty.")


def menu():
    stack = []

    while True:
        print("\nStack Menu:")
        print("1. Push an element onto the stack")
        print("2. Pop an element from the stack")
        print("3. Peek at the top element")
        print("4. Display the stack")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            element = input("Enter the element to push: ")
            push(stack, element)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            peek(stack)
        elif choice == '4':
            display(stack)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

menu()