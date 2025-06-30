#satranjan.py
dic={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"FIve", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
digit=int(input("Enter a digit:"))
#res=dict.get(digit) if dict.get(digit)!=None else "Not a digit"
print("{} is {}".format(digit,dic.get(digit) if dic.get(digit)!=None else "Not a digit"))
