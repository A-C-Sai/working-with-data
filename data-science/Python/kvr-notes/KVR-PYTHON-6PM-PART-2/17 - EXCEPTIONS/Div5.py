#Program for cal Division of Two Numbers by accepting from KBD
#Div5.py
print("Program execution Strated..")
try:
	print("i am in try block")
	s1=input("\nEnter First value:")
	s2=input("Enter Second value:")
	#convert s1 and s2 into integer values
	a=int(s1) # ValueError----------x
	b=int(s2) # ValueError----------x
	c=a/b  #  ZeroDivisionError----x
except:  # default except block 
	print("Ooooops, some thing went wrong!!!")
else:
	print("\n---I am from Else Block---")
	print("Div=",c)
finally:
	print("i am finally block")
