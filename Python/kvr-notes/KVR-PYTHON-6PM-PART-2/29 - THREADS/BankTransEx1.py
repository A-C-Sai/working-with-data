#BankTransEx1.py
import threading,time
class Bank:
	@classmethod
	def getlock(cls):
		Bank.lock=threading.Lock()#step-1
		cls.getBal() #calling Class Level Method from another class level method
	@classmethod
	def getBal(cls):
		cls.totbal=10000
	def  withdraw(self,wcamt):
		Bank.lock.acquire() #Step-2
		if(wcamt>Bank.totbal):
			print("Hi {}, INR {} Check Bounce:".format(threading.current_thread().name,wcamt))
			time.sleep(3)
			print("Available Bal INR:{}".format(Bank.totbal))
		else:
			Bank.totbal=Bank.totbal-wcamt
			print("Hi {}, INR {} Check Cleared:".format(threading.current_thread().name,wcamt))
			time.sleep(3)
			print("Available Bal INR:{}".format(Bank.totbal))
		self.lock.release() #Step-3

#main program
print("----------------------------------------------------------------")
print("Program started {}=",threading.current_thread().name)
print("Number of active threads=",threading.active_count())
print("----------------------------------------------------------------")
Bank.getlock()
c1=threading.Thread(target=Bank().withdraw, args=(5000,))
c2=threading.Thread(target=Bank().withdraw, args=(2000,))
c3=threading.Thread(target=Bank().withdraw, args=(1000,))
c4=threading.Thread(target=Bank().withdraw, args=(1900,))
c1.start()
c2.start()
c3.start()
c4.start()
print("Number of active threads=",threading.active_count())
c1.join()
c2.join()
c3.join()
c4.join()
print("----------------------------------------------------------------")
print("Number of active threads=",threading.active_count())
print("Program execution Ended:{}=",threading.current_thread().name)

