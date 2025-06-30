#Program for generating 1 to n numbers after each and every second by using threads--with OOPs
#NumnberGenerateEx4.py
import threading,time # Step-1
class Numbers:  # Step-2
	def __init__(self,n):
		self.n=n
	def generate(self): #Step-3
		if(self.n<=0):
			print("{} is invalid".format(self.n))
		else:
			print("-------------------------------------------------")
			print("Numbers within {}".format(self.n))
			print("-------------------------------------------------")
			for i in range(1,self.n+1):
				print("\t{}-->Val of i={}".format(threading.current_thread().name,i))
				time.sleep(1)
			else:
				print("-------------------------------------------------")


#main program
no=Numbers(10)
t1=threading.Thread(target=no.generate) #Step-4
t1.start() #Step-5
