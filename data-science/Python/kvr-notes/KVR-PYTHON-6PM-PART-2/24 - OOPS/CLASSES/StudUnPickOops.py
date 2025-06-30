#StudUnPickOops.py--File name and module name
import pickle,sys
class StudUnPick:
	def  readrecord(self):
		with open("stud.pick","rb") as fp:
			print("-"*50)
			while(True):
				try:
					obj=pickle.load(fp)
					obj.dispstuddet()
				except EOFError:
					print("-"*50)
					break

