#Program for generating 1 to n numbers after each and every second by using threads
#NumnberGenerateEx1.py
import threading,time  #Step-1
def numbergenerate(n):  #step-2
	print("Therad Name in numbergenerate()={}".format(threading.current_thread().name))
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("-"*50)
		print("Numbers within:{}".format(n))
		print("-"*50)
		for i in range(1,n+1):
			print("\t{}-->Value of i={}".format(threading.current_thread().name,i))
			time.sleep(1)
		else:
			print("-"*50)

#main program
print("Main Therad Name:{}".format(threading.current_thread().name))
#create sub thread--Step-3
t1=threading.Thread(target=numbergenerate,args=(int(input("Enter How Many Numbers u want to generate")),))
t1.name="KVR" # Setting user-friendly name to the thread
print("is t1 under execution before start={}".format(t1.is_alive())) # False
print("Number of active threads before start={}".format(threading.active_count()))
#dispatch the sub thread
t1.start() # Step-4
print("Number of active threads after start={}".format(threading.active_count())) # 2
print("is t1 under execution after start={}".format(t1.is_alive())) # True
t1.join()
print("Line-29->is t1 under execution after completion of its execution={}".format(t1.is_alive())) # False
