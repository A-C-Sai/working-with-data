#(A) write a server side program in such a way that it must accept Employee number from the client and gives other details of the Employee to the client. 
#EmpDataServer.py
import socket
import cx_Oracle
s=socket.socket()
s.bind(("localhost",6666))
s.listen(2)
print("SSP ie ready to accept any CSP Request")
while(True):
	try:
		cs,ca=s.accept()
		eno=int(cs.recv(1024).decode())
		#PDBC Code
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %eno)
		record=cur.fetchone()
		if(record==None):
			cs.send("Employee Record does not exist".encode())
		else:
			cs.send(str(record).encode())
	except ValueError:
		cs.send("Don't enter strs , symbols and alnums for enos".encode())
	except cx_Oracle.DatabaseError as db:
		cs.send("Prob in DB:"+str(db).encode())
	



