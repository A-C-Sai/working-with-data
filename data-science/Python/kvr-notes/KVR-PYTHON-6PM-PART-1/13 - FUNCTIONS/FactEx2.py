#Program for cal Factorial of a given number
#FactEx2.py
def  fact():
	n=int(input("Enter any value:"))
	if(n<0):
		print("{} is invalid Input:".format(n))
	else:
		f=1
		for i in range(n,0,-1):
			f=f*i
		else:
			print("Fact({})={}".format(n,f))

#main program

fact()#Function Call