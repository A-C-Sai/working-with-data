#Program for performing all types of  Aops
#AnnymousFunEx2.py
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

#main program
while(True):
	aopmenu()
	ch=int(input("Enter Ur Choice:"))
	match (ch):
		case 1: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
			res=addop(a,b)
			print("sum({},{})={}".format(a,b,res))
		case 2: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
			res=subop(a,b)
			print("sub({},{})={}".format(a,b,res))
		case 3: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
			res=mulop(a,b)
			print("mul({},{})={}".format(a,b,res))
		case 4: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
			res=divop(a,b)
			print("div({},{})={}".format(a,b,res))
		case 5: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
			res=flrdivop(a,b)
			print("floor div({},{})={}".format(a,b,res))
		case 6: 
			a=float(input("Enter First Value:"))
			b=float(input("Enter Second Value:"))
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