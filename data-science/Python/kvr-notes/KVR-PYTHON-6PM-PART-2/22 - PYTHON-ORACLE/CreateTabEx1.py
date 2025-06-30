#CreateTabEx1.py
import cx_Oracle # Step-1
def tablecreation():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe") # Step-2
        cur=con.cursor() # Step-3
        #step-4
        cq="create table student (sno number(3) primary key,sname varchar2(10),sub varchar2(8))"
        cur.execute(cq)
        print("Student Table Created Sucessfully")
    except cx_Oracle.DatabaseError as db:
        print("Problem in DB:",db)

#main program
tablecreation()
