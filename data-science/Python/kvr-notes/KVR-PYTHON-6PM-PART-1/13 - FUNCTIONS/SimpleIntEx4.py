#Program for cal simple Interest and total amoun to pay
#SimpleIntEx4.py
def simpleint():
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter Time:"))
	r=float(input("Enter Rate of Interest:"))
	si=(p*t*r)/100
	totamt=p+si
	return p,t,r,si,totamt

#main program
p,t,r,si,totamt=simpleint() # Function Call with multi line assigment.
print("-"*50)
print("Interest Calculation on Loan Amount:")
print("-"*50)
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\t Rate of Interest:{}".format(r))
print("\tSimple Interest on Principle:{}".format(si))
print("\tTotal Amount to Pay:{}".format(totamt))
print("-"*50)
print("=============OR=================")
sires=simpleint()  # Function Call and sires is of type tuple 
print("-"*50)
print("Interest Calculation on Loan Amount:")
print("-"*50)
print("\tPrinciple Amount:{}".format(sires[0]))
print("\tTime:{}".format(sires[1]))
print("\t Rate of Interest:{}".format(sires[2]))
print("\tSimple Interest on Principle:{}".format(sires[3]))
print("\tTotal Amount to Pay:{}".format(sires[4]))
print("-"*50)