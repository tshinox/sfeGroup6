import unittest
from os import system
from datetime import date
import ATM_Simulation


class TestCases(unittest.TestCase):
    def test_Invalid_ID(self):
        self.assertFalse(ATM_Simulation.idCheck(970520))

    def test_Valid_ID(self):
        self.assertTrue(ATM_Simulation.idCheck(9705205613084))

    def test_withdraw(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(fund.withdraw(100), fund.balance)

    def test_deposit(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(fund.deposit(100), fund.balance)

    def test_getID(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(fund.getId(), fund.id)

    def test_getDateCreated(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(fund.getDateCreated(), fund.dateCreated)

    def test_getBalance(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(fund.getBalance(), fund.balance)

    def test_savings_Monthly_Interest_Rate(self):
        fund = ATM_Simulation.SavingsAccount()
        self.assertEqual(fund.getMonthlyInterestRate(), fund.monthlyInterestRate)

    def test_savings_Monthly_Interest(self):
        fund = ATM_Simulation.SavingsAccount()
        bal = ATM_Simulation.Account()
        self.assertEqual(fund.getMonthlyInterest(), (fund.monthlyInterestRate * bal.balance))

    def test_OverDraft(self):
        fund = ATM_Simulation.CheckingAccount()
        self.assertEqual(fund.getOverdraft(), fund.overdraft)

    def test_Display(self):
        fund = ATM_Simulation.Account()
        self.assertEqual(ATM_Simulation.display(), "Available balance: R" + str(fund.balance))

    def test_Menu(self):
        self.assertEqual(ATM_Simulation.Menu(), "1. Check the balance\n2. Withdraw\n3. Deposit\n4. Exit")


if __name__ == '__main__':
    unittest.main()
