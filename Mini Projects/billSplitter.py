def add():
    totalAmt = float(input('Enter total amount: ₹'))
    totalPerson = float(input('Enter total person: '))
    
    if totalPerson == 0 or totalAmt == 0:
        print("Error: The number of persons or total amount cannot be zero.")
        return
    if totalAmt < 0 or totalPerson < 0:
        print("Error: Total amount and total persons must be positive numbers.")
        return
    
    amountPerPerson = f"{(totalAmt / totalPerson):.2f}"
    print('Amount per person is', amountPerPerson)
add() 