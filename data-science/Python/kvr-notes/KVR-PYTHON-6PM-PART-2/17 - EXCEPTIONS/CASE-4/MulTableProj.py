#MulTableProj.py--module name

from MulExceptions import ZeroError,NegativeNumberError
from MulTable import table
def runmulproj():
	try:
		n=int(input("Enter a number for generating mul table:"))
		table(n) # Function Call with result or exception
	except ZeroError:
		print("\nDON'T ENTER ZERO FOR MUL TABLE:")
	except NegativeNumberError:
		print("\nDON'T ENTER Negative Number FOR MUL TABLE:")
	except ValueError:
		print("\nDON'T alnums,strs, symbols for mul tables")
	except:
		print("Some Thing went wrong")