class IncorrectAmount(Exception):
	pass
	
class InsufficientFunds(Exception):
	pass




class Bank:
	def __init__(self,balance=5000):
		self.balance = balance
	
	def deposit(self,amount):
		if (self.__validamount(amount)):
			self.balance += amount
			
	def withdraw(self,amount):
		if (self.__validamount(amount) and self.__minimumfunds(amount)):
			self.balance -= amount

	def __validamount(self,amount):
		if amount > 0 :
			return True
		else:
			raise IncorrectAmount('Entered amount should be greater than 0')
		
	def __minimumfunds(self,amount):
		if self.balance-amount >= 5000:
			return True
		else:
			raise InsufficientFunds('Balance will go below the minimum required')
			

pat = Bank()

try:
	pat.deposit(int(input('How Much Would You Like To Deposit: ')))
	pat.withdraw(int(input('How Much Would You Like To Withdraw: ')))
except IncorrectAmount as e:
	print(e)
except InsufficientFunds as i:
	print(i)
except Exception as p:
	print(p)
else:
	print(pat.balance)

