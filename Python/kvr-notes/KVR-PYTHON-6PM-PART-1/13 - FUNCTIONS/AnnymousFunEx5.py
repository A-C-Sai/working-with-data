#Program for performing all types of  Aops
#AnnymousFunEx5.py

ispaindrome=lambda wrd: wrd.upper()==wrd[::-1].upper()  # Anoinymous Function

#main program
word=input("Enter a word:").upper()
res=ispaindrome(word)
if(res):
	print("{} is Paindrome:".format(word))
else:
	print("{} is not Paindrome:".format(word))


	
