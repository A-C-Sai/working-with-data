#Program for searching for all digits
#RegExpr22.py
import re
gd="A Y$7@5Pq9C &r#6Z m4!"
matres=re.finditer("\d",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr22.py
--------------------------------------------------
Given data= A Y$7@5Pq9C &r#6Z m4!
Start Index:4  End Index:5  Value:7
Start Index:6  End Index:7  Value:5
Start Index:9  End Index:10  Value:9
Start Index:15  End Index:16  Value:6
Start Index:19  End Index:20  Value:4
--------------------------------------------------
"""