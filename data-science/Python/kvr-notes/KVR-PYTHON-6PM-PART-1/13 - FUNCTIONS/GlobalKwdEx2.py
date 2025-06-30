#Program for demonstrating  global keyword
#GlobalKwdEx2.py
a=1
b=2  # Here  a  and b  are called Global Varaibles

def   fun1():
	global a,b
	a=a+1
	b=b+1

def   fun2():
	global a,b
	a=a*2
	b=b*2


#main program
fun()
print("in main Program before fun1()  a={} and b={}".format(a,b))
fun1()
print("in main Program after fun1()  a={} and b={}".format(a,b))
fun2()
print("in main Program after fun2()  a={} and b={}".format(a,b))


