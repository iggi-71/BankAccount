import random

class BankAccount:
    def __init__(self, full_name, account_number, balance, routing_number):
        self.full_name = full_name
        self.account_number = random.randint(10000000,99999999)
        self.balance = 0
        self.routing_number = random.randint(100000000,999999999)

    def printthings(self):
        print(f"my account number is {self.account_number}")

bank = BankAccount('my_name', 'some_symbol', random.randint(0,9), random.randint(10000000,99999999))
print(bank.routing_number)