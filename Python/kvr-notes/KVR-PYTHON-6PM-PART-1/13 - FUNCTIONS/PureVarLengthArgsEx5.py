#program for finding sum of Variable Length arguments
#PureVarLengthArgsEx5.py
def  findsum(sno,sname, *vals,un="KV-Univ"):
	print("-"*50)
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student University:{}".format(un))
	print("-"*50)
	s=0
	for val in vals:
		print("{}".format(val),end=" ")
		s=s+val
	print()
	print("sum={}".format(s))
	print("-"*50)	

#main program
findsum(8,"RT",1,2,3,un="KV-UNIV")
findsum(1,"RS",10)  # Function Call-1
findsum(2,"WK",10,20) # Function Call-2
findsum(3,"KV",10,20,30) # Function Call-3
findsum(4,"TR",10,20,30,40) # Function Call-4
findsum(5,"MC",10,20,30,40,50) # Function Call-5
findsum(6,"ZS",10,20,30,40,50,60,1.2) # Function Call-6
findsum(7,"KVR",un="HYD-UNIV")

