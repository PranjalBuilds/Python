def calculator():
    print('Welcome to the calculator!')
    print('Select an Operation: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulus')
    print('6. Floor Division')
    print('7. Exponentiation')
    print('8. Exit')

    while True:
        choice = input('Enter your choice from 1 2 3 4 5 6 7 8: ')

        for choice in choice:
            if (choice != '8'):
                num1 = int(input('Enter the first number: '))
                num2 = int(input('Enter the second number: '))
            else:
                continue

        match choice:
            case '8':
                print('Exiting...')
                break

            case '1':
                print('The sum is: ', num1 + num2)
            case '2':
                print('The difference is: ', num1 - num2)
            case '3':
                print('The product is: ', num1 * num2)
            case '4':
                if num2 != 0:
                    print('The division is: ', num1 / num2)
                else:
                    print('Cannot divide by zero')
            case '5':
                print('The modulus is: ', num1 % num2)
            case '6':
                print('The floor division is: ', num1 // num2)
            case '7':
                print('The exponentiation is: ', num1 ** num2)
            case _:
                print('Invalid choice')
            
calculator()