#Program for searching for all except  space characters
#RegExpr19.py
import re
gd="A Y$7@5Pq9C &r#6Z m4!"
matres=re.finditer("\S",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr19.py
--------------------------------------------------
Given data= A Y$7@5Pq9C &r#6Z m4!
Start Index:0  End Index:1  Value:A
Start Index:2  End Index:3  Value:Y
Start Index:3  End Index:4  Value:$
Start Index:4  End Index:5  Value:7
Start Index:5  End Index:6  Value:@
Start Index:6  End Index:7  Value:5
Start Index:7  End Index:8  Value:P
Start Index:8  End Index:9  Value:q
Start Index:9  End Index:10  Value:9
Start Index:10  End Index:11  Value:C
Start Index:12  End Index:13  Value:&
Start Index:13  End Index:14  Value:r
Start Index:14  End Index:15  Value:#
Start Index:15  End Index:16  Value:6
Start Index:16  End Index:17  Value:Z
Start Index:18  End Index:19  Value:m
Start Index:19  End Index:20  Value:4
Start Index:20  End Index:21  Value:!
--------------------------------------------------

"""




