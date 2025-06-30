#tlp.py
class Teacher:
	def  readnotes(self):
		print("Teacher Says: read Notes and Parctice")

class LazyStudent(Teacher):
	def readnotes(self):
		print("Lazy Student Neither read nor practice")
		super().readnotes()

class PerfectStudent(Teacher):
	def readnotes(self):
		super().readnotes()
		print("Perfect Student reads More and Practice More")

# main program
ls=LazyStudent()
ls.readnotes()
print("---------------------------------")
ps=PerfectStudent()
ps.readnotes()