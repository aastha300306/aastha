while True:
    try:
        a = input("Enter an integer: ")
        number = int(a)
        print(f"You entered a valid integer: {number}")
        break  
    except ValueError:
        print(" Error: That is not a valid integer. Please try again.")