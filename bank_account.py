class BankAccount:
    def __init__(self, ownersName, balance):
        self.ownersName = ownersName
        self.balance = balance

    @classmethod
    def withdraw(cls):
        return cls.withdraw()

    @classmethod
    def deposit(cls):
        return cls.deposit()

    @classmethod
    def display_balance(cls):
        return cls.display_balance()


account1 = BankAccount(ownersName="Bob", balance=50000)
print(account1.ownersName)
print(account1.balance)