#TrainResEx1.py
import threading,time
class Train:
	@classmethod
	def getlock(cls):
		cls.L=threading.Lock() #Step-1
	@classmethod
	def totalseats(cls):
		cls.seats=5
	def reservation(self,nos):
		Train.L.acquire() #Step-2
		if(nos>Train.seats):
			print("Hi {}, {} Seats Not available--Sorry".format(threading.current_thread().name,nos))
		else:
			Train.seats=Train.seats-nos
			print("Hi, {}, {} Seats Reserved-Hpy Journey".format(threading.current_thread().name,nos))
			time.sleep(3)
			print("Now Available Seats=",Train.seats)
		Train.L.release() #Step-3

#main program
Train.getlock()
Train.totalseats()
t1=threading.Thread(target=Train().reservation, args=(35,))
t2=threading.Thread(target=Train().reservation, args=(13,))
t3=threading.Thread(target=Train().reservation, args=(20,))
t4=threading.Thread(target=Train().reservation, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()