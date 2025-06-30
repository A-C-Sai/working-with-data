#Program for searching Number of occurences of a letter with ? (Zero or One )
#RegExpr26.py
import re
matres=re.finditer("K?","KVKKVKKKVKV")
print("-"*50)
for res in matres:
	print("Start Index:{}  End Index:{}  Value:{}".format(res.start(),res.end(),res.group()))
print("-"*50)

"""
D:\KVR-PYTHON-6PM\REG EXPR>py RegExpr26.py
--------------------------------------------------
Start Index:0  End Index:1  Value:K
Start Index:1  End Index:1  Value:
Start Index:2  End Index:3  Value:K
Start Index:3  End Index:4  Value:K
Start Index:4  End Index:4  Value:
Start Index:5  End Index:6  Value:K
Start Index:6  End Index:7  Value:K
Start Index:7  End Index:8  Value:K
Start Index:8  End Index:8  Value:
Start Index:9  End Index:10  Value:K
Start Index:10  End Index:10  Value:
Start Index:11  End Index:11  Value:
--------------------------------------------------
"""