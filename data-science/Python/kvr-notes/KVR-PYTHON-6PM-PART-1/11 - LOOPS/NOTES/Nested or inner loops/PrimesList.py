#Write a python program which will accept list of numerical values and displayed only prime numbers
#PrimesList.py
n=int(input("Enter How many values u have:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=[]
	print("Enter {} Values:".format(n))
	for i in range(1,n+1):
		lst.append(int(input()))
	else:
		print("Given List of Values:{}".format(lst)) # [5,12, 23, -4, 0, 11, 9]
		#Code for Primes
		print("List of Primes:")
		for num in lst:
			if(num<=1):pass
	
			else:
				res=True
				for i in range(2,num):
					if(num%i==0):
						res=False
						break
				if(res):	
					print("\t{}".format(num))
			



