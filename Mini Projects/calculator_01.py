def calculator():
    print("Welcome to the calculator!")
    print("Enter the operation you want to perform: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Exponentiation")
    print("8. Exit")


    while True:
        choice = int(input("Enter your choice: "))

        if choice == 8:
            print('Exiting...')
            break

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if choice == 1:
            print("The sum is: ", num1 + num2)
        elif choice == 2:
            print("The difference is: ", num1 - num2)
        elif choice == 3:
            print("The product is: ", num1 * num2)
        elif choice == 4:
            if(choice != 0):
                print(f"The division is: ", num1 / num2)
            else:
                print("Cannot divide by zero")
        elif choice == 5:
            print("The modulus is: ", num1 % num2)
        elif choice == 6:
            print("The floor division is: ", num1 // num2)
        elif choice == 7:
            print("The exponentiation is: ", num1 ** num2)
        
        else:
            print("Invalid choice")

    print('\n')
    print("Thank you for using the calculator!")

calculator()