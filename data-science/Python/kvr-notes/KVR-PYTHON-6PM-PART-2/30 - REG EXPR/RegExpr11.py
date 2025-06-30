#Program for searching for all   except alphabets(lower and upper)
#RegExpr11.py
import re
gd="AKY$7@5PqR9C&Hr#6Zm4!"
matres=re.finditer("[^A-Za-z]",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

""""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr11.py
--------------------------------------------------
Given data= AKY$7@5PqR9C&Hr#6Zm4!
Start Index:3  End Index:4  Value:$
Start Index:4  End Index:5  Value:7
Start Index:5  End Index:6  Value:@
Start Index:6  End Index:7  Value:5
Start Index:10  End Index:11  Value:9
Start Index:12  End Index:13  Value:&
Start Index:15  End Index:16  Value:#
Start Index:16  End Index:17  Value:6
Start Index:19  End Index:20  Value:4
Start Index:20  End Index:21  Value:!
--------------------------------------------------
"""