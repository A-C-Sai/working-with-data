#College.py---File Name and acts as module name
from Univ import Univ
class College(Univ):
	def getCollDet(self):
		self.cname=input("Enter College Name:")
		self.cloc=input("Enter College Location:")
		self.getUnivDet()
	def dispCollDet(self):
		print("College Name:{}".format(self.cname))
		print("College Location:{}".format(self.cloc))
		print("-"*50)