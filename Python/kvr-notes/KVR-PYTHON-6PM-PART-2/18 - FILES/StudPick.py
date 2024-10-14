#Program for accepting student details and save them in file by using pickling
#StudPick.py---Program-(A)
import pickle
def   savestuddata():
	with open("studinfo.data","ab") as fp:
		while(True):
			try:
				#accept the student data  from KBD
				print("-"*50)
				sno=int(input("Enter Student Number:"))
				sname=input("Enter Student Name:")
				marks=float(input("Enter Student Marks:"))
				print("-"*50)
				#create an iterable obj(list) and append the data
				lst=list()
				lst.append(sno)
				lst.append(sname)
				lst.append(marks)
				#save list object data to the file
				pickle.dump(lst,fp)
				print("Student Data Saved in File Successfully")
				print("-"*50)
				ch=input("Do u want to insert another record(yes/no):")
				if(ch.lower()=="no"):
					print("Thx for using this program")
					break
			except ValueError:
				print("Don't enter strs,alnums and symbols for numbers and marks")
			except:
				print("Ooops some thing went wrong--try again")

#main program
savestuddata()
