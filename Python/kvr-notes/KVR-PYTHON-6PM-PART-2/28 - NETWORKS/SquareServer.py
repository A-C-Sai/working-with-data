#Write a SSP, in such a way that, It must accept a Number from CSP, Square it and give Result as  Response to CSP.-------Program--(A)
#SquareServer.py
import socket
s=socket.socket()
s.bind(("localhost",8558))
s.listen(2)
print("SSP is Ready to Accept any CSP Request:")
while(True):
	try:
		cs,ca=s.accept()
		#reading CSP Data
		cdata=cs.recv(1024).decode()
		n=int(cdata)
		print("Value of Client at Server={}".format(n))
		#Process CSP Request
		res=n**2
		#SSP Must give Response to CSP
		cs.send(str(res).encode())
	except ValueError:
		cs.send("Don't enter alnums,strs,symbols".encode())



