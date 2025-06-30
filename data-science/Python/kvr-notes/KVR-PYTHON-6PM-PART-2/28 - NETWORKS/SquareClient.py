#b) Write a CSP in such a way that , It read a number from keyboard , send it to SSP and CSP must obtain Its Square from SSP----Program-(B)
#SquareClient.py
import socket
s=socket.socket()
s.connect(("localhost",8558))
print("CSP Got Connection SSP")
#get a number from KBD
n=input("Enter a Number for getting its Square:")
s.send(n.encode())
#receive the result from SSP
result=s.recv(1024).decode()
print("Square({})={}".format(n,result))
