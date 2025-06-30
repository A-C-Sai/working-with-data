#Account5.py---File Name and Module Name--Data Encapsulation applied
class Account:
	def  __init__(self):
		self.__acno=123
		self.cname="Ranjan Naik"
		self.__bal=3.4
		self.__pin=3456
		self.bname="SBI"
	def  dispAcInfo(self):
		#print("Account Number:{}".format(self.acno)) Invalid Access
		print("Account Number:{}".format(self.__acno))
		print("Account holder Name:{}".format(self.cname))
		print("Account Balance:{}".format(self.__bal)) 
		print("Account Pin:{}".format(self.__pin))  
		print("Account Branch Name:{}".format(self.bname))

#main program
ac=Account()
ac.dispAcInfo()