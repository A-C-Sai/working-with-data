#program generating Fibonocci Series
#FibEx.py
def   fibnocciseries(n): # here n is called formal Parameters
	if(n<2):
		print("Invalid Input")
	else:
		n1,n2=0,1
		print("Fibocci Sereies:")
		print(n1)
		print(n2)
		for i in range(2,n):
 			n3=n1+n2    # here n1,n2,n3 are called Local Variables.
			n1=n2
			n2=n3
			print(n3)
	
#main program
m=int(input("Enter How Many Fibonocci Numbers u want:"))
fibnocciseries(m) # here m is called argument