#Program for displaying Squares and Cubes without threads
#Non-ThreadEx1.py
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
print("Default Thread Name -main progfram:",threading.current_thread().name)
lst=[12,4,-5,6,13,19,5,35,17]
squares(lst)
cubes(lst)
et=time.time()
print("Total Execution time of non-threading Prog={}".format(et-bt))
