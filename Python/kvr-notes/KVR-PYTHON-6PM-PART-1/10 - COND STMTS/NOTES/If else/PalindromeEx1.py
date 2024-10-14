#Program accepting  word and decide whether it is palindrome or not
#PalindromeEx1.py
word=input("Enter a word :")
if(word==word[::-1]):
	print("{} is a Palindome:".format(word))
else:
	print("{} is not a Palindome:".format(word))


