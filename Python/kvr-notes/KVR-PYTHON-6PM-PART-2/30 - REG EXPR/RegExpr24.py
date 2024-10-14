#Program for searching Number of occurences of a letter with + (One or More)
#RegExpr24.py
import re
matres=re.finditer("K+","KVKKVKKKVKV")
print("-"*50)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr24.py
-----------------------------------------------------
Start Index:0  End Index:1  Value:K
Start Index:2  End Index:4  Value:KK
Start Index:5  End Index:8  Value:KKK
Start Index:9  End Index:10  Value:K
------------------------------------------------------
"""