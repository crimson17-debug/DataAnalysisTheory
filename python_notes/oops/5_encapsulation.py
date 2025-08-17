
# class BadBankAccount:
#     def __init__(self,balance):
#         self.balance = balance


# account = BadBankAccount(0.0)
# account.balance =-1
# print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0.0  #encapsulating to be used within the class only

    @property
    def balance(self):
        return self._balance
    

    def deposit(self,amount):
        if amount <=0:
            raise ValueError("deposit amount must be positive")
        else:
            self._balance += amount

    
    def withdraw(self,amount):
        if amount<= 0:
            raise ValueError("Withdraw amount must be positve")
        if amount >self.balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount 



account = BankAccount()

print(account.balance)
account.deposit(1000)
print(account.balance)
account.withdraw(20)
print(account.balance)