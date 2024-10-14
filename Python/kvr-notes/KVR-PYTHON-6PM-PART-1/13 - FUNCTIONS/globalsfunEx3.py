#Program for demonstrating globals()
#globalsfunEx3.py
a=10
b=20 # here 'a' and 'b' are called global Varaibles
def  operation():
	d=globals()
	print("-"*50)
	for gn,gv in d.items():
		print("{}-->{}".format(gn,gv))
	print("="*70)
	print("Programmer-defined global Variable Names and Values")
	print("Global Var a=", d['a'])
	print("Global Var b=", d['b'])
	print("="*70)
	print("Programmer-defined global Variable Names and Values")
	print("Global Var a=", d.get('a'))
	print("Global Var b=", d.get('b'))
	print("="*70)
	print("Programmer-defined global Variable Names and Values")
	print("Global Var a=", globals()['a'])
	print("Global Var b=", globals()['b'])
	print("="*70)
	print("Programmer-defined global Variable Names and Values")
	print("Global Var a=",globals().get('a'))
	print("Global Var b=", globals().get('b'))

	
#main program
operation()
