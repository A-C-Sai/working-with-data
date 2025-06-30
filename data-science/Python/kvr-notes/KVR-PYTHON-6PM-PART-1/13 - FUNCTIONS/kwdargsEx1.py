#Program for demonstrating Keyword Arguments
#kwdargsEx1.py
def  disp(a,b,c,d):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#main program
print("-"*50)
print("\ta\tb\tc\td")
print("-"*50)
disp(10,20,30,40) # Function call with Pos Args
disp(d=40,a=10,b=20,c=30)#  Function call with Key word args
disp(b=20,a=10,d=40,c=30)#  Function call with Key word args
disp(10,20,d=40,c=30)# Function Call with Pos args and Key word args
#disp(b=20,a=10,40,30)# Function Call with Key word args Pos args--SyntaxError: positional argument follows keyword argument
disp(10,d=40,c=30,b=20) # Function Call with Pos args and Key word args
print("-"*50)
