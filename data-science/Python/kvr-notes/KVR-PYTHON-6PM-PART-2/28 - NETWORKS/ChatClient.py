#ChatClient.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",3600))
	csdata=input("Student Msg-->")
	s.send(csdata.encode())
	ssdata=s.recv(1024).decode()
	print("Teracher Msg-->{}".format(ssdata))

