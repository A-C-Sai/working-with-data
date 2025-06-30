#Covid19.py
class Hospital:
	def __init__(self,name,cap,occ):
		self.name=name
		self.cap=cap
		self.occ=occ
	def admit_patient(self):
		if(self.occ<self.cap):
			self.occ=self.occ+1
			print("patient admitted successfully")
		else:
			print( 'sorry. please try another hospital.')


	
	
#main program
hospital = Hospital('Healthline',301,300)
hospital.admit_patient()
