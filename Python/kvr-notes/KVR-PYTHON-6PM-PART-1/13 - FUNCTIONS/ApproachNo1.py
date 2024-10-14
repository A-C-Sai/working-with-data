#Function for mul of two numbers
#ApproachNo1.py
#Input---->Function Call
#Processing-->Function Body
#Output-------->Function Call
def  mulop(k,v=10):
	r=k*v
	return r
	
#main program
m=int(input("Enter First value:"))
n=int(input("Enter Second value:"))
res=mulop(m,n) # Function Call
print("Mul({},{})={}".format(m,n,res))

