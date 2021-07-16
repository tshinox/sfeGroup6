from os import system
from datetime import date
from time import sleep

checking = [5]
savings = [5]


class Account:
    def __init__(self, idNum, balance, dateCreated, index):
        self.id = idNum
        self.balance = balance
        self.dateCreated = dateCreated
        self.index = index
        interest = 0

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getDateCreated(self):
        return self.DateCreated

    def setAccount(self):
        savings[self.index] = self.id
        checking[self.index] = self.id
        self.balance = self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        if self.balance < 0:
            checking[self.index] = CheckingAccount(self.balance)
            self.balance = amount + checking[self.index].getOverdraft()
            return self.balance
        else:
            savings[self.index] = SavingsAccount(12)
            self.balance += savings[self.index].getMonthlyInterest()
            self.balance = amount + self.balance
            return self.balance


class CheckingAccount(Account):
    def __init__(self, overdraft):
        self.overdraft = overdraft

    def getOverdraft(self):
        return self.overdraft


class SavingsAccount(Account):
    def __init__(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate
        self.monthlyInterestRate = 0

    def getMonthlyInterestRate(self):
        self.monthlyInterestRate = (self.annualInterestRate / 100.0) / 12.0
        return self.monthlyInterestRate

    def getMonthlyInterest(self):
        self.getMonthlyInterestRate()
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


option = 0
i = 0

while True:
    sleep(1.0)
    system('cls')
    identity = input("Enter your ID number:")
    acc = Account(identity, 0, date.today(), i)
    acc.setAccount()
    if idCheck(identity):
        menu()
        option = eval(input("Choose an option:"))
        while option != 4:
            if option == 1:
                display()
            elif option == 2:
                out = eval(input("Enter the amount to withdraw: "))
                acc.withdraw(out)
                print("Money out:-R" + str(out))
            elif option == 3:
                dep = eval(input("Enter the amount to deposit:"))
                acc.deposit(dep)
                print("Amount of R" + str(dep) + " was deposited to the account\n ref:" + acc.getId())

            else:
                print("Invalid option!!!.")
            option = eval(input("Choose an option:"))
    else:
        print("Please enter a valid ID number!!!.")
    i += 1
