#SubThreadCreateEx1.py
import threading  # Step-1
def  hello(sname):  # Step-2
	print("\n{}, welcome to Multi Threading".format(sname))
	print("Name of sub thread={}".format(threading.current_thread().name))


#main program
print("Main Therad Name:{}".format(threading.current_thread().name))
t1=threading.Thread(target=hello,args=("Rossum",) ) # Step-3
t1.name="SandeepURS"  #t1.setName("Sandeep")----Not Recommended
t1.start()  # Step-4
