#Program for searching for all upper alphabets
#RegExpr6.py
import re
gd="AKY$7@5PqR9C&Hr#6Zm4!"
matres=re.finditer("[A-Z]",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)
""""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr6.py
--------------------------------------------------
Given data= AKY$7@5PqR9C&Hr#6Zm4!
Start Index:0  End Index:1  Value:A
Start Index:1  End Index:2  Value:K
Start Index:2  End Index:3  Value:Y
Start Index:7  End Index:8  Value:P
Start Index:9  End Index:10  Value:R
Start Index:11  End Index:12  Value:C
Start Index:13  End Index:14  Value:H
Start Index:17  End Index:18  Value:Z
--------------------------------------------------
"""