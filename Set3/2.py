#Write Python Program to simulate a Bank Account with support for depositMoney, 
#withdrawMoney and showBalance Operations


# BankAccount class
class Bank_Account:
	def __init__(self):
		self.balance=0
# Function to deposite amount
	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\nAmount Deposited:",amount)
# Function to withdraw the amount
	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\nYou Withdrew:", amount)
		else:
			print("\nInsufficient balance ")

# Function to display the amount
	def display(self):
		print("\nNet Balance=",self.balance)

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
