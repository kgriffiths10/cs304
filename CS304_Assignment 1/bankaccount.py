
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner_name, bank_name, initial_balance):
        self.owner_name = owner_name
        self.bank_name = bank_name
        self.balance = initial_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __iadd__(self, amount):
        self.balance += amount
        return self

    def __isub__(self, amount):
        self.balance -= amount
        return self

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance