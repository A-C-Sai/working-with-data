#DecEx3.py
def squareroot(gv):  # Decorator Function
	def cal():  # Inner Function
		n=gv()
		res=n**0.5
		return res
	return cal

@squareroot	
def   getval():  # Defined by  X Programmer
	n=float(input("Enter a Number:"))
	return n

#main program
result=getval()
print("Square Root=",result)
