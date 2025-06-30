#Program for searching for all  except digits
#RegExpr23.py
import re
gd="A Y$7@5Pq9C &r#6Z m4!"
matres=re.finditer("\D",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)
s="Python Program"
"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr23.py
--------------------------------------------------
Given data= A Y$7@5Pq9C &r#6Z m4!
Start Index:0  End Index:1  Value:A
Start Index:1  End Index:2  Value:
Start Index:2  End Index:3  Value:Y
Start Index:3  End Index:4  Value:$
Start Index:5  End Index:6  Value:@
Start Index:7  End Index:8  Value:P
Start Index:8  End Index:9  Value:q
Start Index:10  End Index:11  Value:C
Start Index:11  End Index:12  Value:
Start Index:12  End Index:13  Value:&
Start Index:13  End Index:14  Value:r
Start Index:14  End Index:15  Value:#
Start Index:16  End Index:17  Value:Z
Start Index:17  End Index:18  Value:
Start Index:18  End Index:19  Value:m
Start Index:20  End Index:21  Value:!
--------------------------------------------------
"""