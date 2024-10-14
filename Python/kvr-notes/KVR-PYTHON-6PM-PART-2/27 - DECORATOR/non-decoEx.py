#non-decoEx.py
def   getval():  # Defined by  X Programmer
	n=int(input("Enter a Number:"))
	return n

#Y Person want to compute Square val of  getVal()
def   getYRes():
	y=getval()
	res=y**2
	print("Square({})={}".format(y,res))

#Z Person want to compute Square Root of val of  getVal()
def getZRes():
	z=getval()
	res=z**0.5
	print("SquareRoot({})={}".format(z,res))

#main program
getYRes()
getZRes()