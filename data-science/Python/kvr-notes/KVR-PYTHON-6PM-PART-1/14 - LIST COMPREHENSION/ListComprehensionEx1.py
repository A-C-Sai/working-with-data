#ListComprehensionEx1.py
lst=[10,20,-34,-56,-100,150,-135,56]
pslist=[ val     for val in lst  if val>0 ]
nslist=[val     for val in lst  if val<0]

print(pslist)
print(nslist)