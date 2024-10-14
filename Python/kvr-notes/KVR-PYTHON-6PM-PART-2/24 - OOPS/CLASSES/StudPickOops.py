#StudPickOops.py---file name ans module name
from Student import Student
import sys
import pickle
class StudPick:
	def  savestuddata(self):
		#open the file stud.data in binary format with 'a' mode
		with open("stud.pick","ab") as fp:
			while(True):
				try:
					#Accept student data from KBD
					print("-"*50)
					sno=int(input("Enter Student Number:"))
					sname=input("Enter Student Name:")
					marks=float(input("Enter Student Marks:"))
					#create an object of Student
					s=Student() 
					s.appendstuddata(sno,sname,marks)
					#write student object data into file 
					pickle.dump(s,fp)
					print("-"*50)
					print("Student record saved successfully in file")
					print("-"*50)
					ch=input("Do u want insert another student record(yes/no):")
					if(ch.lower()=="no"):
						break
				except ValueError:
					print("Don't enter alnums,.strs and symbols for sno and marks")

