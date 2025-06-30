#Write a client side program which will accept Employee number send to the server side program and gets other details of Employee.
#EmpDataClient.py
import socket
s=socket.socket()
s.connect(("localhost",6666))
print("CSP get Connection from SSP")
empno=input("\nEnter Employee Number:")
s.send(empno.encode())
empdata=s.recv(1024).decode()
print("-"*50)
print("Employee Data")
print("-"*50)
print(empdata)
print("-"*50)
