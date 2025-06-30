#Program for generating 1 to n numbers after each and every second by using threads--with OOPs
#NumnberGenerateEx2.py
import threading,time # Step-1
class Numbers:  # Step-2
	def generate(self,n): #Step-3
		if(n<=0):
			print("{} is invalid".format(n))
		else:
			print("-------------------------------------------------")
			print("Numbers within {}".format(n))
			print("-------------------------------------------------")
			for i in range(1,n+1):
				print("\t{}-->Val of i={}".format(threading.current_thread().name,i))
				time.sleep(1)
			else:
				print("-------------------------------------------------")


#main program
no=Numbers()
t1=threading.Thread(target=no.generate,args=(10,)) #Step-4
t1.start() #Step-5
