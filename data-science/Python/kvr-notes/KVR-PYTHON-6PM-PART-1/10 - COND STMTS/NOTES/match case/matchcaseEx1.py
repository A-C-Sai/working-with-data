#Program for implementing all Arithmetic Operations by using match case
#matchcaseEx1.py
import sys
print("-"*50)
print("\tArithemetic Operations")
print("-"*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("-"*50)
ch=int(input("Enter Ur Choice:"))
#Use match case
match(ch):
	
	case 1:
		a,b=float(input("Enter First Value for Addition:")),float(input("Enter Second Value for Addition:"))
		print("sum({},{})={}".format(a,b,a+b))
	case 2: 
		x=float(input("Enter First Value for Sub:"))
		y=float(input("Enter Second Value for Sub:"))
		print("Sub({},{})={}".format(x,y,x-y))
	case 3: 
		x=float(input("Enter First Value for Mul:"))
		y=float(input("Enter Second Value for Mul:"))
		print("Mul({},{})={}".format(x,y,x*y))
	case 4:
		x=float(input("Enter First Value for Division:"))
		y=float(input("Enter Second Value for Division:"))
		print("Div({},{})={}".format(x,y,x/y))
		print("Floor Div({},{})={}".format(x,y,x//y))
	case 5:
		x=float(input("Enter First Value for Modulo Division:"))
		y=float(input("Enter Second Value for Modulo Division:"))
		print("Mod({},{})={}".format(x,y,x%y))
	case 6:
		a=float(input("Enter Base--->"))
		b=float(input("Enter Power-->"))
		print("pow({},{})={}".format(a,b,a**b))

	case 7:
		print("Thx for  for using this program")
		sys.exit()
	case _:
		print("Ur Selection of Operation is wrong--try again!!")	

print("\nProgram execution completed")