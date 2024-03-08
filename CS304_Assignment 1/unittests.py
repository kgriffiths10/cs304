import unittest

from chequingaccount import ChequingAccount
from savingsaccount import SavingsAccount

class TestChequingAccount(unittest.TestCase):
    def test_deposit(self):
        chequing = ChequingAccount("John Doe", "Canadian Bank", 1000, 0.5)
        chequing.deposit(500)
        self.assertEqual(chequing.balance, 1500)

    def test_withdraw_sufficient_funds(self):
        chequing = ChequingAccount("John Doe", "Canadian Bank", 1000, 0.5)
        self.assertTrue(chequing.withdraw(800))
        self.assertEqual(chequing.balance, 199.5)  # 1000 - 800 - 0.5

    def test_withdraw_insufficient_funds(self):
        chequing = ChequingAccount("John Doe", "Canadian Bank", 1000, 0.5)
        self.assertFalse(chequing.withdraw(1200))
        self.assertEqual(chequing.balance, 1000)  # No change in balance

    def test_make_purchase(self):
        chequing = ChequingAccount("John Doe", "Canadian Bank", 1000, 0.5)
        chequing.make_purchase(800)
        self.assertEqual(chequing.balance, 199.5)  # 1000 - 800 - 0.5

class TestSavingsAccount(unittest.TestCase):
    def test_deposit(self):
        savings = SavingsAccount("Jane Smith", "American Bank", 2000, 0.02)
        savings.deposit(1000)
        self.assertEqual(savings.balance, 3000)

    def test_withdraw_sufficient_funds(self):
        savings = SavingsAccount("Jane Smith", "American Bank", 2000, 0.02)
        self.assertTrue(savings.withdraw(1500))
        self.assertEqual(savings.balance, 500)

    def test_withdraw_insufficient_funds(self):
        savings = SavingsAccount("Jane Smith", "American Bank", 2000, 0.02)
        self.assertFalse(savings.withdraw(2500))
        self.assertEqual(savings.balance, 2000)

    def test_accrue_interest(self):
        savings = SavingsAccount("Jane Smith", "American Bank", 2000, 0.02)
        savings.accrue_interest()
        self.assertEqual(savings.balance, 2040)  # 2000 + (2000 * 0.02)


if __name__ == "__main__":
    unittest.main()