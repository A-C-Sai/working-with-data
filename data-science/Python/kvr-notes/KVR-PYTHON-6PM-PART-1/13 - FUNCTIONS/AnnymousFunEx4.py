#Program for performing all types of  Aops
#AnnymousFunEx4.py

ispaindrome=lambda wrd: wrd==wrd[::-1]  # Anoinymous Function

#main program
word=input("Enter a word:")
res=ispaindrome(word)
if(res):
	print("{} is Paindrome:".format(word))
else:
	print("{} is not Paindrome:".format(word))