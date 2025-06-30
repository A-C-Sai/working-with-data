#DecEx2.py
def square(gv):  # Decorator Function
	def cal():  # Inner Function
		n=gv()
		res=n**2
		return res
	return cal

@square	
def   getval():  # Defined by  X Programmer
	n=float(input("Enter a Number:"))
	return n

#main program
result=getval()
print("Square=",result)