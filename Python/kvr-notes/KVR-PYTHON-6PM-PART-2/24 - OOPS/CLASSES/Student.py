#Student.py--File name and module name
class Student:
	def  appendstuddata(self, sno,sname,marks):
		self.sno=sno
		self.sname=sname
		self.smarks=marks
	def dispstuddet(self):
		print("\t{}\t{}\t{}".format(self.sno,self.sname,self.smarks))


