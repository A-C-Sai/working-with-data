#Program for cal Division of Two Numbers by accepting from KBD
#Div6.py--------This code written by KVR--2022 Dec 31st
print("Program execution Strated..")
try:
	print("i am in try block")
	s1=input("\nEnter First value:")
	s2=input("Enter Second value:")
	#convert s1 and s2 into integer values   
	a=int(s1) # ValueError----------x
	b=int(s2) # ValueError----------x
	c=a/b  #  ZeroDivisionError----x
	s="PYTHON"
	print(s[10])
except ZeroDivisionError:
	print("DON't ENTER ZERO For Den....")
except ValueError:
	print("DON't Enter alnums, strs and symbols")
except: # default except block
	print("OOOOPs Some thing went wrong")
else:
	print("\n---I am from Else Block---")
	print("Div=",c)
finally:
	print("i am finally block")
