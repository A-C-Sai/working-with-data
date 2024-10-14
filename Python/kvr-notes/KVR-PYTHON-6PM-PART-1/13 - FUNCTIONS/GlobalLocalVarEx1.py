#Program for demonstrating Global and Local Variables
#GlobalLocalVarEx1.py
lang="PYTHON"   # Global Variable
def   learnML():
	sub1="ML"  # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub1,lang))
	#print(sub2,sub3)---error bcoz sub2 and sub3 are local variables in learnDL() and LearnIOT()
def   learnDL():
	sub2="DL" # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub2,lang))
	#print(sub1,sub3)---error bcoz sub1 and sub3 are local variables in learnML() and LearnIOT()

def   learnIOT():
	sub3="IOT" # local Variable
	print("To develop '{}' Programs, we need '{} ' Lang".format(sub3,lang))
	#print(sub1,sub2)---error bcoz sub1 and sub1 are local variables in learnML() and LearnDL()

#main program
learnML()
learnDL()
learnIOT()