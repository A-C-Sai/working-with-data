#Program for displaying Squares and Cubes with threads
#WithThreadEx1.py
import time,threading
def squares(lst):
	for val in lst:
		print("{}--Squares({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
def cubes(lst):
	for val in lst:
		print("{}--Cubes({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#main program
bt=time.time()
print("Default Thread Name -main progfram:",threading.current_thread().name)#MainTherad
lst=[12,4,-5,6,13,19,5,35,17]
#create a thread object for exeucting squares
t1=threading.Thread(target=squares,args=(lst,)) # t1--object---Name: Thread-1
t1.name="Rossum"
#create a thread object for exeucting Cubes
t2=threading.Thread(target=cubes,args=(lst,)) # t2--object---Name: Thread-2
t2.name="Travis"
print("Number of active Threads before dispatch=",threading.active_count())
#dispatch the therads
t1.start()
t2.start()
print("Number of active Threads before dispatch=",threading.active_count())
#Join the sub threads with MainThread
t1.join()
t2.join()
print("Number of active Threads after joining=",threading.active_count())
et=time.time()
print("Main Program, Total Execution time of with threads Prog={}".format(et-bt))