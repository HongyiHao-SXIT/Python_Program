def register():
    print("\n--- Register ---")
    account = input("Enter account: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as f:
        f.write(f"{account},{password}\n")

    print("✅ Registration successful!\n")


def login():
    print("\n--- Login ---")
    account = input("Enter account: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("⚠ No users registered yet. Please register first.\n")
        return False

    for user in users:
        acc, pwd = user.strip().split(",")
        if account == acc and password == pwd:
            print("✅ Login successful!\n")
            return True

    print("❌ Login failed. Wrong account or password.\n")
    return False


def main():
    while True:
        choice = input("Choose an option: [1] Register  [2] Login  [3] Exit : ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
