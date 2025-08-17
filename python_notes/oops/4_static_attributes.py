# a static attribute called a class attribute
#it is an attribute that belongs to class itself not to any specific instance
#instance attributes are contained in unique instance 
#static attribute is defined in a class that can be used by instances

class User:
    user_count = 0        #constant attributes
    def __init__(self,username,email): #instance attributes
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")




# user1 = User("dant", "dant@123")
# user2 = User("bant", "bant@123")
# #everytime we create an instance we increement the static attribute

# print(User.user_count)
# print(user1.user_count)
# print(user2.user_count)




# #static methods

# class BankAccount:
#     MIN_BALANCE = 100

#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         if amount>0:
#             self.balance += amount
#             print(f"{self.owner}'s new balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positve")

#     @staticmethod
#     def is_valid_interest_rate(rate):
#         return 0<= rate <= 5
    

# account = BankAccount("navya", 500)
# account.deposit(200)

# print(BankAccount.is_valid_interest_rate(5))
# print(BankAccount.is_valid_interest_rate(10))
# print(account.is_valid_interest_rate(2))

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self.balance += amount
            self.__log_transaction("deposit", "amount")
        else:
            print("Deposit amount must be positve")


    def _is_valid_amount(self,amount):
        return amount >0
    

    def __log_transaction(self,transaction_type,amount):
        print(f"Logging {transaction_type} of ${amount}> New Balance: ${self.balance}")


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5
    


account = BankAccount("navya", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(5))
print(BankAccount.is_valid_interest_rate(10))
print(account.is_valid_interest_rate(2))












