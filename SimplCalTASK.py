# Simple CLI calculator.
print("Welcome to Simple CLI Calculator")

is_running = True

while is_running:
    # Processing Calculations....
    print("Starting Calculator Process.")
    user_operation = input(
        "What operation would you like to perform?\nPick any of['+','-','*','/']")

    # Get user numbers
    try:  # Try to get user numbers if they are valid intergers or floats

        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))

    except:
        print("Failed,invalid number...")
        continue

    if user_operation == "+":
        # perform addition
        print(no1+no2)
    elif user_operation == "-":
        # perform Subtraction
        print(no1-no2)
    elif user_operation == "*":
        # perform multiplication
        print(no1*no2)
    elif user_operation == "/":
        # perform division
        print(no1 / no2)
    else:

        print("Invalid operation entered, Try again.")

    choice = input("Would you like to run anoither calculation, [y,n]")
    if choice == "y":
        pass

    if choice == "n":
        is_running = False
