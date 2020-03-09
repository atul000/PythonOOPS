from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self, name, initialDeposit):
        return 0

    @abstractmethod
    def authenticate(self, name, accountNumber):
        return 0

    @abstractmethod
    def withdraw(self, withdrawlAmount):
        return 0

    @abstractmethod
    def deposit(self, depositAmount):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0


class SavingAccount(Account):
    def __init__(self):
        # [key][0] => name ; [key][1] => balance
        self.savingAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]
        # {12345: ['atul', '$1000'], 98765: ['alex', '$5000']}
        print("Account creation has been successful. Your account number: ",
              self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authenticate Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawlAmount
            print("Withdrawl was successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()

    def displayBalance(self):
        print("Available balance: ",
              self.savingAccounts[self.accountNumber][1])


savingAccount = SavingAccount()
while True:
    print("Enter 1: To create Account")
    print("Enter 2: To access an existing account")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposits: ")
        deposit = int(input())
        savingAccount.createAccount(name, deposit)
    elif userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1: To withdraw")
                print("Enter 2: To Deposit")
                print("Enter 3: To display available balance")
                print("Enter 4: To go back to the previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter a withdrawl amount")
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingAccount.displayBalance()
                elif userChoice is 4:
                    break
        elif userChoice is 3:
            quit()
