import user
import login

def main():
    while True:
        print("=== Welcome ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user.register()
        elif choice == "2":
            user_info = login.login()
            if user_info:
                print(f"Welcome back, {user_info['account']}!")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
