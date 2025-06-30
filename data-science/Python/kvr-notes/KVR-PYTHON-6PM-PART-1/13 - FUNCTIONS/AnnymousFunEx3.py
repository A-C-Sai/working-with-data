#Program for performing all types of  Aops
#AnnymousFunEx3.py
import sys

#Anonymous Functions for aops
addop=lambda x,y:x+y
subop=lambda x,y:x-y
mulop=lambda x,y:x*y
divop=lambda a,b:a/b
flrdivop=lambda a,b:a//b
modop=lambda a,b:a%b
expop=lambda a,b : a**b

def  aopmenu():
	print("-"*50)
	print("\tArithmetic Operations")
	print("-"*50)
	print("\t1.Addition")
	print("\t2.Substraction")
	print("\t3.Multiplication")
	print("\t4.Division")
	print("\t5.Floor Division")
	print("\t6.Modulo Division")
	print("\t7.Exponentiation")
	print("\t8.Exit")
	print("-"*50)

def readvalues(op):
	a=float(input("Enter First value for performing '{}':".format(op)))
	b=float(input("Enter Second value for performing '{}':".format(op)))
	return a,b

#main program
while(True):
	aopmenu()
	ch=int(input("Enter Ur Choice:"))
	match (ch):
		case 1: 
			a,b=readvalues("Addition")  # Function Call with Multi Line assignment
			res=addop(a,b)
			print("sum({},{})={}".format(a,b,res))
		case 2: 
			a,b=readvalues("Sub")  # Function Call with Multi Line assignment
			res=subop(a,b)
			print("sub({},{})={}".format(a,b,res))
		case 3: 
			a,b=readvalues("Mul")
			res=mulop(a,b)
			print("mul({},{})={}".format(a,b,res))
		case 4: 
			k,v=readvalues("Div")
			r=divop(k,v)
			print("div({},{})={}".format(k,v,r))
		case 5: 
			t=readvalues("Floor Div")  # Function Call with Multi Line assignment
			res=flrdivop(t[0],t[1])
			print("floor div({},{})={}".format(t[0],t[1],res))
		case 6: 
			a,b=readvalues("Moduls")  # Function Call with Multi Line assignment
			res=modop(a,b)
			print("mod({},{})={}".format(a,b,res))
		case 7:
			a=float(input("Enter Base:"))
			b=float(input("Enter Power:"))
			res=expop(a,b)
			print("power({},{})={}".format(a,b,res))
		case 8:
			print("Thx for Using This Program")
			sys.exit()
		case _:
			print("Ur Selection of Operation is Wrong--try again")