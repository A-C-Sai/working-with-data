#Program accepting list of words
#PalWordsEx1.py
print("Enter List of Words  Separated by Comma:")
palwords=[word for word in input().split(",") if word==word[::-1] ]
print("List of Palindrome Words=",palwords)
