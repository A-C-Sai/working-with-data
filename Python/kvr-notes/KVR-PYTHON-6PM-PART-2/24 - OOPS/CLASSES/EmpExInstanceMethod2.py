#Program for Reading  and display Employee Data by using classes and objects who are working same company by using Instance Methods
#EmpExInstanceMethod2.py
class Employee: 
	def readempdata(self):  # Instance Method
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))
		self.dispempdata() # Calling Instance Method from another Instance Method w.r.t self

	def dispempdata(self): # Instance Method
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Salary:{}".format(self.sal))

#main program
e1=Employee() # Object Creation
e2=Employee() # Object Creation
#Read First Employee Data
print("Enter First Employee Details")
print("-"*40)
e1.readempdata()
#ReadSecond Employee Data
print("\nEnter Second  Employee Details")
print("-"*40)
e2.readempdata()
print("-"*40)