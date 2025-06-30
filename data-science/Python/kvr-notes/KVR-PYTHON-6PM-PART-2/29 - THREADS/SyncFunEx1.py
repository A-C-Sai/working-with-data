#SyncFunEx1.py
import threading,time
def multable(n):
	L1.acquire() #Step-2--obtain the lock
	if (n<=0):
		print("{}--->{} is invalid".format(threading.current_thread().name, n))
	else:
		print("-"*50)
		print("{}--Mul Table for {}".format(threading.current_thread().name, n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
			time.sleep(1)
		print("-"*50)
	L1.release()  # Step-3 Relase the lock	
#main program
#Step-1---create an object of Lock Class of threading
L1=threading.Lock()
#Create sub threads
t1=threading.Thread(target=multable,args=(10,))
t2=threading.Thread(target=multable,args=(12,))
t3=threading.Thread(target=multable,args=(-19,))
t4=threading.Thread(target=multable,args=(16,))
#dispatch  the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
