#program for finnding Vowels from line of text
#Vowels.py
word=input("Enter Line of Text:") # Apple
print("Given Line:{}".format(word))
i=0
now=0
while(i<len(word)):
    if(word[i] in ["a","e","i","o","u","A","E","I","O","U"]):
        print("\t{}".format(word[i]), end=" ")
        now=now+1
    i=i+1
else:
    print("\nNumber of Vowels Found={}".format(now))

