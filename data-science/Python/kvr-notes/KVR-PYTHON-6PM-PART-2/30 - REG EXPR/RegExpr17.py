#Program for searching for all special symbols
#RegExpr17.py
import re
gd="AKY$7@5PqR9C&Hr#6Zm4!"
matres=re.finditer("[^A-Za-z0-9]",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr17.py
--------------------------------------------------
Given data= AKY$7@5PqR9C&Hr#6Zm4!
Start Index:3  End Index:4  Value:$
Start Index:5  End Index:6  Value:@
Start Index:12  End Index:13  Value:&
Start Index:15  End Index:16  Value:#
Start Index:20  End Index:21  Value:!
--------------------------------------------------
"""