#ChatServer.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",3600))
s.listen(2)
print("SSP is Ready to Recive the Request from CSP")
while(True):
	clientsoc,caddr=s.accept()
	csdata=clientsoc.recv(1024).decode()
	print("Student Msg-->{}".format(csdata))
	ssdata=input("Teacher Msg-->")
	clientsoc.send(ssdata.encode())


