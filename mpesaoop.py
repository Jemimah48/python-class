# define the userclass
class Users:
    def __init__(self, user_id, name,phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.account=account(self) # creating an account for the user

    def __repr__(self):

        return f"user({self.user_id},{self.name},{self.phone})"


class account(Users):
    def __init__(self, user):
        self.user = user
        self.balance = 0.0
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"{amount} deposited.New balance: {self.balance}")
        else:
            print("deposited amount must be positive")
    def withdraw(self,amount):
        if 0< amount<=self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. new balance: {self.balance}")
        else:
            print("insuficient ammount")


    def __repr__(self):
        return f"account(User:{self.user.name}Balance:{self.balance},)"
# define transaction class
class Transaction:
    def __init__(self, account,  amount,transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
    def proccess(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("invalid transaction type")
    def __repr__(self):

         return f"Transaction(Account:{self.account.user.name}"

# example usage
user1=Users(1,"Jemimah kibor","070880054")
print(user1)

user3=Users(3,"Asher","011345667")
print(user3)
# deposit ammount
user1.account.deposit(1000)

# withdraw
user1.account.withdraw(500)

transaction1=Transaction(user1.account,200,'deposit')
transaction1.proccess()

transaction2=Transaction(user1.account,200,'withdraw')
transaction2.proccess()
print(user1.account)

user2=Users(2," Njoki","0117277466")
print(user2)
user2.account.deposit(4000)
user2.account.withdraw(2000)
transaction2=Transaction(user2.account,200,'deposit')
transaction2.proccess()
transaction2=Transaction(user2.account,400,'withdraw')
transaction2.proccess()
print (user2.account)