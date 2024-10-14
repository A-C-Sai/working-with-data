#Program for searching for all   alpha-numerics
#RegExpr15.py
import re
gd="AKY$7@5PqR9C&Hr#6Zm4!"
matres=re.finditer("[A-Za-z0-9]",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)
"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr15.py
--------------------------------------------------
Given data= AKY$7@5PqR9C&Hr#6Zm4!
Start Index:0  End Index:1  Value:A
Start Index:1  End Index:2  Value:K
Start Index:2  End Index:3  Value:Y
Start Index:4  End Index:5  Value:7
Start Index:6  End Index:7  Value:5
Start Index:7  End Index:8  Value:P
Start Index:8  End Index:9  Value:q
Start Index:9  End Index:10  Value:R
Start Index:10  End Index:11  Value:9
Start Index:11  End Index:12  Value:C
Start Index:13  End Index:14  Value:H
Start Index:14  End Index:15  Value:r
Start Index:16  End Index:17  Value:6
Start Index:17  End Index:18  Value:Z
Start Index:18  End Index:19  Value:m
Start Index:19  End Index:20  Value:4
--------------------------------------------------
"""















