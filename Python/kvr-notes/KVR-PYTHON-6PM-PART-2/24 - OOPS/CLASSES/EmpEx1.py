#Program for Reading  and display Employee Data by using classes and objects who are working same company.
#EmpEx1.py
class Employee:
	cname="Infosys"  # Class Level Data Member

#main program
e1=Employee() # Object Creation
e2=Employee() # Object Creation
#Read Employee Data for e1 object
print("Enter First Employee Details")
print("-"*40)
e1.eno=int(input("Enter Employee Number:"))
e1.ename=input("Enter Employee Name:")
e1.sal=float(input("Enter Employee Salary:"))
print("-"*40)
#Read Employee Data for e2 object
print("Enter Second Employee Details")
print("-"*40)
e2.eno=int(input("Enter Employee Number:"))
e2.ename=input("Enter Employee Name:")
e2.sal=float(input("Enter Employee Salary:"))
print("-"*40)
print("First Employee Details:")
print("-"*40)
print("Employee Number:{}".format(e1.eno))
print("Employee Name:{}".format(e1.ename))
print("Employee Salary:{}".format(e1.sal))
print("Employee Comp Name:{}".format(Employee.cname))
print("-"*40)
print("Second Employee Details:")
print("-"*40)
print("Employee Number:{}".format(e2.eno))
print("Employee Name:{}".format(e2.ename))
print("Employee Salary:{}".format(e2.sal))
print("Employee Comp Name:{}".format(Employee.cname))
print("-"*40)
