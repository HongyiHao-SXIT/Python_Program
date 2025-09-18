import re

def register():
    print("\n--- Register ---")
    
    ID = input("Please Enter your ID Number: ")
    
    account = input("Set your account: ")
    with open("users.txt", "r") as f:
        existing_accounts = [line.split(",")[0] for line in f.readlines()]
    if account in existing_accounts:
        print("❌ Account already exists. Please choose another account.")
        return
    
    password = input("Set your password: ")
    if len(password) < 6:
        print("❌ Password too short. It must be at least 6 characters.")
        return
    
    Phone_Num = input("Tell me your phone number: ")
    if not Phone_Num.isdigit() or len(Phone_Num) != 10:
        print("❌ Invalid phone number. It must be 10 digits.")
        return
    
    Address = input("Set your address: ")

    with open("users.txt", "a") as f:
        f.write(f"{ID},{account},{password},{Phone_Num},{Address}\n")

    print("✅ Registration successful!\n")
