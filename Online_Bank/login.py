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
        try:
            user_data = user.strip().split(",")
            if len(user_data) < 5:
                print(f"⚠ Invalid user data in file: {user.strip()}. Skipping.")
                continue

            ID, acc, pwd, phone, address = user_data
        except ValueError:
            print(f"⚠ Error reading user data: {user.strip()}. Skipping.")
            continue

        if account == acc and password == pwd:
            print("✅ Login successful!\n")

            return {"ID": ID, "account": acc, "phone": phone, "address": address}

    print("❌ Login failed. Wrong account or password.\n")
    return False