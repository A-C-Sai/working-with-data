#Program for cal simple Interest and total amoun to pay
#SimpleIntEx3.py
def simpleint(p,t,r):
	si=(p*t*r)/100
	totamt=p+si
	print("-"*50)
	print("Interest Calculation on Loan Amount:")
	print("-"*50)
	print("\tPrinciple Amount:{}".format(p))
	print("\tTime:{}".format(t))
	print("\tRate of Interest:{}".format(r))
	print("\tSimple Interest on Principle:{}".format(si))
	print("\tTotal Amount to Pay:{}".format(totamt))
	print("-"*50)

#main program
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
simpleint(p,t,r)  
