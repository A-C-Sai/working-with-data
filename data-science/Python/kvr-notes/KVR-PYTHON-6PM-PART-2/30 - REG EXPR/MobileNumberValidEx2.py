#Program for mobile number validation by using Reg Expressions
#MobileNumberValidEx2.py
import re
while(True):
	mno=input("Enter Mobile Number:")
	if(len(mno)==10):
		res=re.search("[9][8]\d{8}",mno)
		if(res!=None):
			break
		else:
			print("Mobile Number Should not Contain Other than Digits-try again")
	else:
		print("Mobile Number length must be 10 Digits,try again")

print("\n{} Miobile is Valid:".format(mno))