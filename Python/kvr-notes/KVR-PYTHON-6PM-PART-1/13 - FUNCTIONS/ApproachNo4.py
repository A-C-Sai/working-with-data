#Function for mul of two numbers
#ApproachNo4.py
#Input------>Function Body
#Process--->Function Body
#Output----->Function Call

def mulop():
	a=int(input("Enter First Value:"))
	b=int(input("Enter Second Value:"))
	c=a*b
	return a,b,c # In Python, return statement can return one or more number of vals

#main program
x,y,z=mulop() # Function Call with Multi Line assignment
print("mul({},{})={}".format(x,y,z))
print("=========OR===============")
res=mulop() # Function Call --here res is type tuple
print("mul({},{})={}".format(res[0],res[1],res[2]))