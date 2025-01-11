# In-memory storage for registered users
users = {}

# Register function
def register():
    print("*** Welcome to the password validator program, REGISTER NOW! ***")
    
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if len(username) < 1 or len(password) < 1:
        print("Username or password cannot be empty!")
        return False
    elif len(username) < 3:
        print("Username must be at least 3 characters long!")
        return False
    elif len(password) < 8:
        print("Password must be at least 8 characters long!")
        return False
    elif username in users:
        print("This username is already taken. Please choose a different one.")
        return False
    else:
        users[username] = password
        print("Registration successful!")
        return True

# Login function
def login():
    print("*** Login to your account ***")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if len(username) < 1 or len(password) < 1:
        print("Username or password cannot be empty!")
        return False
    elif username in users and users[username] == password:
        print(f"Welcome back, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

# Main Program
def main():
    print("Welcome to the User System!")
    while True:
        action = input("Do you already have an account? (yes/no/exit): ").strip().lower()

        if action == "yes":
            if login():
                break  # Login successful, exit.
        elif action == "no":
            if register():
                print("You can now log in!")
                if login():
                    break  # Login successful after registration
        elif action == "exit":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please type 'yes', 'no', or 'exit'.")
        print("\n")

main()
