#Others2.py--main program---Abstraction is used for extarcting req Information without considering Hidden data
from Account2 import Account
ac=Account() # Object creation
ac.getacdetails()
#print("Account Number:{}".format(ac.acno))   can't access
print("Account holder Name:{}".format(ac.cname))
#print("Account Balance:{}".format(ac.bal))  can't access
#print("Account Pin:{}".format(ac.pin))   can't access
print("Account Branch Name:{}".format(ac.bname))
