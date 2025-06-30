#Program for menu Driven Operations on Pickling and Unpikcling Operations
#RunStudPickUnPickDemo.py
import sys
from StudPickOops import StudPick
from StudUnPickOops import StudUnPick
class PickUnPickOperations:
	@staticmethod
	def menu():
		print("*"*50)
		print("\t1.Pickling Operation")
		print("\t2.Un-Pickling Operation")
		print("\t3. Exit")
		print("*"*50)
	
	def  operationtype(self,op):
		match(op):
			case 1:
				sp=StudPick()
				sp.savestuddata()
			case 2:
				sp1=StudUnPick()
				sp1.readrecord()
			case 3:
				print("Thx for using Program:")
				sys.exit()
			case _:
				print("Ur selection of Operation is wrong-try again")
#main program
while(True):
	try:
		PickUnPickOperations.menu()
		ch=int(input("Enter Ur Choice:"))
		op=PickUnPickOperations()
		op.operationtype(ch)
	except ValueError:
		print("Plz don't enteer alnums,strs and symbols for choice:")

