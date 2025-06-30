#Program for demonstrating Global and Local Variables
#GlobalLocalVarEx4.py
def   learnML():
	sub1="ML"  # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub1,lang))

def   learnDL():
	sub2="DL" # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub2,lang))

def   learnIOT():
	sub3="IOT" # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub3,lang))

#main program
#learnML()
#learnDL()
#learnIOT()
lang="PYTHON"   # Global Variable at line 19, we can't Global variable lang in learnML(), learnDL() and learnIOT()