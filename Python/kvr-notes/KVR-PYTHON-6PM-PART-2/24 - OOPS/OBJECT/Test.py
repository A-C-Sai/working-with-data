#Test.py
class Student1:
	def   disp1(self):
		print("disp1()--student1 class")
		s2=Student2 ()
		s2.disp()

class Student2:
	def  disp(self):
		print("disp2()--Student2 class")

#main program
s1=Student1()
s1.disp1()