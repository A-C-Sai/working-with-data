#program for demonstarting Variable length arguments
#PureVarLengthArgsEx1.py

def  disp( *param ):  # Here *param is called Var leg Parameter and type is tuple
	print("-"*50)
	print("Number of Values:",len(param))
	for val in param:
		print("{}".format(val),end=" ")
	print()

#main program--Family of similar Function calls with Var length args
disp(10)  # Function Call-1
disp(10,20) # Function Call-2
disp(10,20,30) # Function Call-3
disp(10,20,30,40) # Function Call-4
disp(10,20,30,40,50) # Function Call-5
disp(10,20,30,40,50,"KVR") # Function Call-6
disp()# Function Call-7

