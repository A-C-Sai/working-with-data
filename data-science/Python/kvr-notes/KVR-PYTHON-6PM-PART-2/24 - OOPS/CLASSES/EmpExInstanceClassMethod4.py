#Program for Reading  and display Employee Data by using classes and objects who are working same company by using Instance and Class Level Methods
#EmpExInstanceClassMethod4.py
class Employee: 
	@classmethod
	def  getcompdet(cls):   # Class Level Method
		cls.cname="TCS"  # Class Level Data Member
		cls.getcompaddr() # Calling Class Level Method w.r.t cls
	@classmethod
	def getcompaddr(cls):  # Class Level Method
		Employee.addr="HYD" # Class Level Data Member

	def readempdata(self):  # Instance Method
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))

	def dispempdata(self): # Instance Method
		Employee.getcompdet() # Calling Class Level Method w.r.t Class Name
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Salary:{}".format(self.sal))
		print("Employee Comp Name:{}".format(self.cname))
		print("Employee Comp Addr:{}".format(self.addr))

#main program
e1=Employee() # Object Creation
e2=Employee() # Object Creation
#Read First Employee Data
print("Enter First Employee Details")
print("-"*40)
e1.readempdata()
#ReadSecond Employee Data
print("Enter Second  Employee Details")
print("-"*40)
e2.readempdata()
print("-"*40)
print("First Employee Details:")
print("-"*40)
e1.dispempdata()
print("-"*40)
print("Second Employee Details:")
print("-"*40)
e2.dispempdata()
print("-"*40)