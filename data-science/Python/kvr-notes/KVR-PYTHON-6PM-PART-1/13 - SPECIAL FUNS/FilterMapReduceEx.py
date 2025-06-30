#FilterMapReduceEx.py
import functools
def  readvalues():
	lst=[]
	n=int(input("Enter How Many Sal Values u Have:"))
	if(n<=0):
		return lst
	else:
		print("Enter {} Values:".format(n))
		for i in range(1,n+1):
			lst.append(int(input()))
		return lst
#main program
lst=readvalues() 
if(len(lst)==0):
	print("List is empty and can't find sum of +Ve and _ve Values")
else:
	print("Old  Sal Values:{}".format(lst)) # [0, 250, 500, 501, 650, 750]
	sal0_500=list(filter(lambda sal : 0<=sal<=500,lst))
	sal501_1000=list(filter(lambda sal: 501<=sal<=1000, lst))
	print("Sal ranges 0 to 500:{}".format(sal0_500))
	print("Sal ranges 501 to 1000:{}".format(sal501_1000))
	hksal0_500=list(map(lambda sal:sal+sal*(5/100),sal0_500))
	hksal501_1000=list(map(lambda sal:sal+sal*(10/100),sal501_1000))
	totsalhksal0_500=functools.reduce(lambda a,b:a+b,hksal0_500)
	totsalhksal501_1000=functools.reduce(lambda a,b:a+b,hksal501_1000)
	print("-"*50)
	print("Sal ranges 0 to 500:{}".format(sal0_500))
	print("Hiked Salaries ranges 0 to 500:{}".format(hksal0_500))
	print("Total Paying in the range 0 to 500:{}".format(totsalhksal0_500))
	print("-"*50)
	print("\nSal ranges 501 to 1000:{}".format(sal501_1000))
	print("Hiked Salaries ranges 501 to 1000:{}".format(hksal501_1000))
	print("Total Paying in the range 501 to 1000:{}".format(totsalhksal501_1000))
	print("-"*50)
	
