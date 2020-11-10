from random import randint
# first we need to import the random function

class BankAccount:
  def __init__(self, full_name):
    self.full_name = full_name
    self.account_number = randint(100000000, 999999999)
    # this is generaters a number with 9 digits
    self.routing_number = 23984576
    # the routing number is always the same so we keep it like that
    self.balance = float(0)
  
  def deposit(self, amount):
    self.balance += float(amount)
    return f"Amount Deposited: ${amount}"
  
  def withdraw(self, amount):
    self.balance -= float(amount)
    if self.balance >= 0:
      return f"Amount Withdraw: ${amount}"
    else: 
      self.balance -= 10 
      return f"Insufficient funds. An overdraft fee of $10 has been charged."
  
  def get_balance(self):
    return f"Thank for using Chase Bank, your current account balance is ${self.balance}"

  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest
    return f"Your interest got added for this month!"

  def print_receipt(self):
    return f"{self.full_name}\nAccount No.: {self.account_number}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}"

rafa_account = BankAccount("rafa vaz")
sam_account = BankAccount("sam madergal")
alex_account = BankAccount("alex turk")
rick_account = BankAccount("rick jacob")

print(rafa_account.withdraw(10))
print(rafa_account.deposit(1000))
print(sam_account.withdraw(100))
print(sam_account.print_receipt())