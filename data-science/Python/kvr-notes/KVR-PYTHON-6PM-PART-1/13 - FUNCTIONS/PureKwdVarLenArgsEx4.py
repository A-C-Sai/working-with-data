#PureKwdVarLenArgsEx4.py
def disp(id,name,*vals,crs="PYTHON PROG",**kwds):
	print('-'*50)
	print(id,name)
	print("Course for all=",crs)
	print("Var length=",vals, type(vals),len(vals))
	print("Key word Var length=",kwds,type(kwds),len(kwds))

#main program
disp(111,"TR",10,20,30,40,a=1.2,b=2.3)
disp(222,"RS",10,20,30,40,50,p="Python",q="Data Sci",r="Django")
disp(333,"MC","Java","Spring",k="Python",v="AI",r="ML",h="DL",m="Tablea")
disp(444,"Naveen")
disp(555,"Praveen",1.2,2.3)
disp(666,"Suresh",a=100,b="X",c=True)

"""
def   functionname(list of Pos Params, Var len nParams,default params, kwd Var len params):pass

"""
