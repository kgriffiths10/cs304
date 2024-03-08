from bankaccount import BankAccount

class ChequingAccount(BankAccount):
    def __init__(self, owner_name, bank_name, initial_balance, transaction_fee):
        super().__init__(owner_name, bank_name, initial_balance)
        self.transaction_fee = transaction_fee

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount - self.transaction_fee >= 0:
            self.balance -= (amount + self.transaction_fee)
            return True
        else:
            return False

    def make_purchase(self, amount):
        if self.withdraw(amount):
            print("Purchase successful")
        else:
            print("Insufficient funds")