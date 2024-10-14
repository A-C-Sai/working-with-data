#Program for accepting employee details and save them in file by using pickling
#EmpPick.py---Program-(A)
import pickle
def  saveempdata():
	with open("empinfo.data","ab") as fp:
		noe=int(input("Enter How Many employee data u have:")) # noe=4
		if(noe<=0):
			print("{} is invalid input--try again".format(noe))
		else:
			for i in range(1,noe+1):
				print("-"*50)
				print("Enter {} Employee Information:".format(i))
				print("-"*50)
				eno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				sal=float(input("Enter Employee Salary:"))
				print("-"*50)
				lst=[]
				lst.append(eno)
				lst.append(ename)
				lst.append(sal)
				pickle.dump(lst,fp)
				print("Employee Data Saved in File Successfully")

#main program
saveempdata()