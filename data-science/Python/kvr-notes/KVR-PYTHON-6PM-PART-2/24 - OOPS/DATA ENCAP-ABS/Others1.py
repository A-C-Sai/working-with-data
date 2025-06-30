#Others1.py--main program---Abstraction is used for extarcting req Information without considering Hidden data
from Account1 import Account
ac=Account() # Object creation
#print("Account Number:{}".format(ac.acno))  
print("Account holder Name:{}".format(ac.cname))
#print("Account Balance:{}".format(ac.bal)) can't access
#print("Account Pin:{}".format(ac.pin))  can't access
print("Account Branch Name:{}".format(ac.bname))


