#ATMOperationsDemo.py--main program
from ATMMenu import menu
from ATMExceptions import DepositError, WithdrawError ,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
while(True):
	try:
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1: 
				try:
					deposit()
				except ValueError:
					print("Don't enter alnums,strs and symbols for deposit amount:")
				except DepositError:
					print("Don't Deposit Zero / -ve Value ")
			case 2:
				try:
					withdraw()
				except WithdrawError:
					print("Don't withdraw  Zero / -ve Value ")
				except ValueError:
					print("Don't enter alnums,strs and symbols for withdraw amount:")
				except InSuffFundError:
					print("Ur account does not have suff funds--Read PYTHON NOTES")
			case 3:
				balenq()
			case 4: 
				print("Thx for using program")
				break
			case _:
				print("Ur Selection of Operation is Wrong-Try again")
	except	 ValueError:
		print("Don't enter alnums, strs and special symbols for choice")