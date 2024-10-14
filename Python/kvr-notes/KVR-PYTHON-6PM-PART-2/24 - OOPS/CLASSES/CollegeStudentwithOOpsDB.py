#Program for student marks report
#StudentMarksReport.py
#accept Student Number
#CollegeStudentwithOOpsDB.py
import cx_Oracle,sys
class CollegeStudent:
	def acceptstudentdata(self):
		while(True):
			self.sno=int(input("Enter Student Number(100-200):"))
			if(200>=self.sno>=100):
				break
			print("Invalid Student Number-Try again")

		#Accept Student Name
		self.sname=input("Enter Student Name:")
		#accept C lang Marks--100
		while(True):
			self.cm=int(input("Enter Marks C:")) # 99
			if(0<=self.cm<=100):
				break
			print("Invalid Marks in C--try again")
		#accept C++ lang Marks--100
		while(True):
			self.cpp=int(input("Enter Marks C++:")) # 56
			if(0<=self.cpp<=100):
				break
			print("Invalid Marks in C++--try again")
		#accept Python lang Marks--100
		while(True):
			self.pym=int(input("Enter Marks Python:")) 
			if(0<=self.pym<=100):
				break
			print("Invalid Marks in Python--try again")
		#cal total marks and percentage of marks
		self.totmarks=self.cm+self.cpp+self.pym
		self.percent=(self.totmarks/300)*100
		#Decide the grade for fail or pass
		if(self.cm<40) or   (self.cpp<40)  or   (self.pym<40) :
			self.grade="FAIL"
		else:
			#deciding Passed Grade
			if(self.totmarks>=250)  and   (self.totmarks<=300):
				self.grade="DISTINCTION"
			elif(self.totmarks>=200)  and   (self.totmarks<=249):
				self.grade="FIRST"
			elif(self.totmarks>=150)  and   (self.totmarks<=199):
				self.grade="SECOND"
			elif(self.totmarks>=120)  and   (self.totmarks<=149):
				self.grade="THIRD"

		#Dislay Marks Report	
		print("="*50)
		print("\tS t u d e n t  M a r k s  R e p o r t")
		print("="*50)
		print("\tStudent Number:{}".format(self.sno))
		print("\tStudent Name:{}".format(self.sname))
		print("\tStudent Marks in C:{}".format(self.cm))
		print("\tStudent Marks in C++:{}".format(self.cpp))
		print("\tStudent Marks in Python:{}".format(self.pym))
		print("-"*50)
		print("\tStudent Total Marks :{}".format(self.totmarks))
		print("\tStudent Percent of Marks :{}".format(round(self.percent,2)))
		print("\tStudent Exam Result :{}".format(self.grade))
		print("-"*50)
		print("="*50)
	
	def  savestuddata(self):
		#write PDBC CODE
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		#query
		iq="insert into student values(%d,'%s',%d,%d,%d,%d,%f,'%s')"
		cur.execute(iq %(self.sno,self.sname,self.cm,self.cpp,self.pym,self.totmarks,self.percent,self.grade))
		con.commit()
		print("\nStudent record Saved sucessfully in Student table")
#main program
cs=CollegeStudent()
while(True):
	cs.acceptstudentdata()
	cs.savestuddata()
	ch=input("\nDo u want to insert another stuident record:")
	if(ch.lower()=="no"):
		sys.exit()
	
