#ATMOperations.py--File and Module Name
from ATMExceptions import DepositError, WithdrawError ,InSuffFundError
bal=500.00 # global variable
def  deposit():
	damt=float(input("Enter the amount for Deposit:")) # ValueError---damt---  -5000
	if(damt<=0):
		raise DepositError  # Hitting the exception
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxxx123 Credited with INR:{}".format(damt))
		print("Now Ur Account xxxxxxx123 Bal INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter the amount for Withdraw:")) # ValueError---
	if(wamt<=0):
		raise WithdrawError # Hitting the exception
	elif((wamt+500)>bal):
		raise InSuffFundError # Hitting the exception
	else:
		bal=bal-wamt
		print("Ur Account xxxxxxx123 Debitted with INR:{}".format(wamt))
		print("Now Ur Account xxxxxxx123 Bal INR:{}".format(bal))

def  balenq():
	print("Ur Account xxxxxxx123 Bal INR:{}".format(bal))