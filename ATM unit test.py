import unittest
from os import system
from datetime import date
from ATM_Simulation import *


class TestCases(unittest.TestCase):
    def test_Invalid_ID(self):
        self.assertFalse(idCheck(970520))

    def test_Valid_ID(self):
        self.assertTrue(idCheck(9705205613084))

    def test_withdraw(self):
        fund = Account()
        self.assertEqual(fund.withdraw(100), fund.balance)

    def test_deposit(self):
        fund = Account()
        self.assertEqual(fund.deposit(100), fund.balance)

    def test_getID(self):
        fund = Account()
        self.assertEqual(fund.getId(), fund.id)

    def test_getDateCreated(self):
        fund = Account()
        self.assertEqual(fund.getDateCreated(), fund.dateCreated)

    def test_getBalance(self):
        fund = Account()
        self.assertEqual(fund.getBalance(), fund.balance)

    def test_savings_Monthly_Interest_Rate(self):
        fund = SavingsAccount()
        self.assertEqual(fund.getMonthlyInterestRate(), fund.monthlyInterestRate)

    def test_savings_Monthly_Interest(self):
        fund = SavingsAccount()
        bal = Account()
        self.assertEqual(fund.getMonthlyInterest(), (fund.monthlyInterestRate * bal.balance))

    def test_OverDraft(self):
        fund = CheckingAccount()
        self.assertEqual(fund.getOverdraft(), fund.overdraft)

    def test_Display(self):
        fund = Account()
        self.assertEqual(display(), "Available balance: R" + str(fund.balance))

 
if __name__ == '__main__':
    unittest.main()
