from utils.usermanager import UserManager
from utils.dice_game import DiceGame

def main():
    user_manager = UserManager('user.txt')

    while True:
        print("\n\tWelcome to the Dice Game!")
        print("\n\t\t1. Register")
        print("\t\t2. Login")
        print("\t\t3. Exit")
        choice = input("\n\tEnter your choice: ")

        if choice == '1':
            username = input("\n\tEnter a username (at least 4 characters): ")
            if user_manager.validate_username(username):
                password = input("\n\tEnter a password (at least 8 characters): ")
                if user_manager.validate_password(password):
                    user_manager.register(username, password)
                    print("\n\tRegistration successful!")
                else:
                    print("\tPassword must be at least 8 characters. Please Try again.")
            else:
                print("\n\tInvalid username or Username Taken. Please try again.")

        elif choice == '2':
            username = input("\n\tEnter your username: ")
            password = input("\n\tEnter your password: ")
            if user_manager.login(username, password):
                print("\n\tLogin successful!")
                game = DiceGame(username)
                if not game.menu(username):
                    continue
            else:
                print("\n\tInvalid username or password. Please try again.")

        elif choice == '3':
            print("\n\tExiting the system.")
            break
        else:
            print("")

if __name__ == "__main__":
    main()
