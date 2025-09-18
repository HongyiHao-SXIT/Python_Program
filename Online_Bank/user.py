class User():
    def __init__(self, ID="Default", Name="Default", Address="Default", 
                 Phone_Num="Default", Age="Default", Account="Default", 
                 Password="Default", Balance=0.0):
        self.ID = ID
        self.Name = Name
        self.Address = Address
        self.Phone_Num = Phone_Num
        self.Age = Age
        self.Account = Account
        self.Password = Password
        self.Balance = Balance
        
    def save_money(self, money: float):
        self.Balance += money
        print(f"${money} has been added. New balance: ${self.Balance}")
        
    def display_user_info(self):
        print(f"User ID: {self.ID}")
        print(f"Name: {self.Name}")
        print(f"Address: {self.Address}")
        print(f"Phone Number: {self.Phone_Num}")
        print(f"Age: {self.Age}")
        print(f"Account: {self.Account}")
        print(f"Balance: ${self.Balance}")
