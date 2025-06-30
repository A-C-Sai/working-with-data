#Program for searching for   Lower alphabets
#RegExpr8.py
import re
gd="AKY$7@5PqR9C&Hr#6Zm4!"
matres=re.finditer("[a-z]",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)
"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr8.py
--------------------------------------------------
Given data= AKY$7@5PqR9C&Hr#6Zm4!
Start Index:8  End Index:9  Value:q
Start Index:14  End Index:15  Value:r
Start Index:18  End Index:19  Value:m
--------------------------------------------------
"""