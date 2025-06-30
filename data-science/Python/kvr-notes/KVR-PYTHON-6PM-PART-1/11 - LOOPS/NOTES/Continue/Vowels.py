#program for finnding Vowels from line of text
#Vowels.py
word=input("Enter Line of Text:") # Apple
print("Given Line:{}".format(word))
for ch in word:
    if(ch in ["a","e","i","o","u","A","E","I","O","U"]):
        print("\t{}".format(ch),end=" ")

