#DigitEx3.py
dictobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",8:"EIGHT",7:"SEVEN",9:"NINE"}
d=int(input("Enter a digit:"))
res=dictobj.get(d)
if(res!=None):
	print("{} is {}".format(d,res))
else:
	print("{} is not a Digit:".format(d))