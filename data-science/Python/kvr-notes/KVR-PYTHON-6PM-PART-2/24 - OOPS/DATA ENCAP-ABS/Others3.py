#Others3.py--main program---Abstraction is used for extarcting req Information without considering Hidden data
from Account3 import Account
ac=Account() # Object creation
print(ac.__dict__)
#ac.getacdetails() can't access
#print("Account Number:{}".format(ac.acno))   
#print("Account holder Name:{}".format(ac.cname))
#print("Account Balance:{}".format(ac.bal))  
#print("Account Pin:{}".format(ac.pin))   
#print("Account Branch Name:{}".format(ac.bname))
