class User:
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

u1 = User(Name="Alice", Balance=100.5)
print(u1.Name, u1.Balance)
