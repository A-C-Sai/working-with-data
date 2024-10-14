#Program for searching for all space characters
#RegExpr18.py
import re
gd="A Y$7@5Pq9C &r#6Z m4!"
matres=re.finditer("\s",gd)
print("-"*50)
print("Given data=",gd)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr18.py
--------------------------------------------------
Given data= A Y$7@5Pq9C &r#6Z m4!
Start Index:1  End Index:2  Value:
Start Index:11  End Index:12  Value:
Start Index:17  End Index:18  Value:
--------------------------------------------------
"""