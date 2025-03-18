import random

'''
Stone Paper Scissor (vs PC):
Logic: 
loss scenarios:
1. stone vs paper
2. paper vs scissor
3. scissor vs stone
scene :         1 : stone,  2: paper , 3 scissor
score logic:    0 for draw, 1 for win, -1 for loss 
'''

def check(comp, user):
    if comp == user:
        return 0
    elif user == 1 and comp == 2:
        return -1
    elif user == 2 and comp == 3:
        return -1
    elif user == 3 and comp == 1:
        return -1
    return 1

choice = ['stone', 'paper', 'scissor']

def main():
    compPts = 0
    userPts = 0
    
    while True: 
        comp = random.randint(1, 3)
        try:
            user = int(input("Enter 1 for Stone, 2 for Paper, 3 for Scissor: "))
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
            continue

        if user not in [1, 2, 3]:
            print("Alas! INVALID choice!")
            continue

        score = check(comp, user)
        user_choice = choice[user - 1]
        comp_choice = choice[comp - 1]

        print(f"You: {user_choice}")
        print(f"Comp: {comp_choice}")
        print()

        if score == 0:
            print("DRAW!")
            print()
            print(f"User score: {userPts}")
            print(f"Computer Score: {compPts}")
            print()

        elif score == -1:
            compPts += 1
            print("Oops! You Lost!")
            print()
            print(f"User score: {userPts}")
            print(f"Computer Score: {compPts}")
            print()

        elif score == 1:
            userPts += 1
            print("Whoo! You Won!")
            print()
            print(f"User score: {userPts}")
            print(f"Computer Score: {compPts}")
            print()

        while True:
            try:
                userRes = int(input("Enter 0 to exit, any other number to continue: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        if userRes == 0:
            print("Thanks for Playing!")
            break

main()