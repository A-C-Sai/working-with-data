#Program for demonstrating Global and Local Variables
#GlobalLocalVarEx3.py
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
lang="PYTHON"   # Global Variable
learnML()
learnDL()
learnIOT()