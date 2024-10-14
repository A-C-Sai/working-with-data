#SyncOopsEx1.py
import threading,time
class Table:
	def multable(self,n):
		L.acquire() #Step-2
		if (n<=0):
			print("{}--{} is invalid".format(threading.current_thread().name, n))
		else:
			print("-"*50)
			print("{}--Mul Table for {}".format(threading.current_thread().name, n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} x {}={}".format(n,i,n*i))
				time.sleep(0.25)
			print("-"*50)
		L.release() # step-3

#main program
L=threading.Lock() # Step-1
t1=threading.Thread(target=Table().multable,args=(10,))
t2=threading.Thread(target=Table().multable,args=(12,))
t3=threading.Thread(target=Table().multable,args=(-19,))
t4=threading.Thread(target=Table().multable,args=(16,))
t1.start()
t2.start()
t3.start()
t4.start()
