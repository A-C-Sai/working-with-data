#FilterMapReduceExTableCpmre.py
import functools
print("Enter Salaries of employee between 0 to 1000 separated by space:")
lst=[int(sal) for sal in input().split() if 0<=int(sal)<=1000]
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
print("Old Sal0-500\tHikedsal0-500")
print("-"*50)
for  osl,nsl  in zip(sal0_500,hksal0_500):
	print("\t{}\t{}".format(osl,nsl))
print("Total Paying in the range 0 to 500:{}".format(totsalhksal0_500))
print("-"*50)
print("Old Sal501-1000\tHikedsal501-1000")
print("-"*50)
for  osl,nsl  in zip(sal501_1000,hksal501_1000):
	print("\t{}\t{}".format(osl,nsl))
print("Total Paying in the range 501 to 1000:{}".format(totsalhksal501_1000))
print("-"*50)
	
