#Program for searching either A  or B or C
#RegExpr4.py
import re
#here [ABC] is called Search pattern
#here  "AKY$7@5PqR9C&Hr#6Zm4!" is given data
matres=re.finditer("[ABC]","AKY$7@5PqR9C&Hr#6Zm4!")
print("-"*50)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
OUTPUT
-------------
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr4.py
--------------------------------------------------
Start Index:0  End Index:1  Value:A
Start Index:11  End Index:12  Value:C
--------------------------------------------------
"""