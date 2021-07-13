from os import system
from datetime import date
from time import sleep
import random


class Account:
    def __init__(self, idNum, balance, dateCreated):
        self.id = idNum
        self.balance = balance
        self.dateCreated = dateCreated

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getDateCreated(self):
        return self.DateCreated

    def setAccount(self, Id, Balance):
        self.id = Id
        self.balance = Balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance


class CheckingAccount(Account):
    def __init__(self, overdraft):
        self.overdraft = overdraft

    def overdraft(self):
        return self.overdraft


class SavingsAccount(Account):
    def __init__(self, annualInterestRate, monthlyInterestRate):
        self.annualInterestRate = annualInterestRate
        self.monthlyInterestRate = monthlyInterestRate

    def getMonthlyInterestRate(self):
        self.monthlyInterestRate = (self.annualInterestRate / 100.0) / 12.0
        return self.monthlyInterestRate

    def getMonthlyInterest(self):
        return self.balance * self.monthlyInterestRate


def idCheck(idNum):
    if len(idNum) == 13 and idNum.isnumeric():
        return True
    else:
        return False


def display():
    print("Available balance: R" + str(acc.getBalance()))


def menu():
    print("1. Check the balance\n2. Withdraw\n3. Deposit\n4. Exit")


savings = []
checking = []
option = 0

while True:
    sleep(1.0)
    system('cls')
    identity = input("Enter your ID number:")
    acc = Account(identity, 0, date.today())
    if idCheck(identity):
        # accNum = random.choice(savings)
        menu()
        option = eval(input("Choose an option:"))
        while option != 4:
            if option == 1:
                display()
            elif option == 2:
                out = eval(input("Enter the amount to withdraw: "))
                acc.withdraw(out)
                print("Money out:-R"+str(out))
            elif option == 3:
                dep = eval(input("Enter the amount to deposit:"))
                acc.deposit(dep)
                print("Amount of R" + str(dep) + " was deposited to the account\n ref:" + acc.getId())

            else:
                print("Invalid option!!!.")
            option = eval(input("Choose an option:"))
    else:
        print("Please enter a valid ID number!!!.")
