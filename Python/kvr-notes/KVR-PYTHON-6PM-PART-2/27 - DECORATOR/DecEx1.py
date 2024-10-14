#DecEx1.py
def   getval():  # Defined by  X Programmer
	n=int(input("Enter a Number:"))
	return n

def square(gv):  # Decorator Function
	def cal():  # Inner Function
		n=gv()
		res=n**2
		return res
	return cal
	
#main program
r=square(getval)
result=r()
print("Square=",result)