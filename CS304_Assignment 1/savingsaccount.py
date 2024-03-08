from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner_name, bank_name, initial_balance, interest_rate):
        super().__init__(owner_name, bank_name, initial_balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return True
        else:
            return False

    def accrue_interest(self):
        self.balance += self.balance * self.interest_rate