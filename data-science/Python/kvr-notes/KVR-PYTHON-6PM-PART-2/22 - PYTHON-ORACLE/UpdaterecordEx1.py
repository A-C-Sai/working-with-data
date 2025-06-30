#UpdaterecordEx1.py
import cx_Oracle
def updaterecord():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #accept the employee number and company name
        empno=int(input("Enter Elpoyee Number:"))
        cmpname=input("Enter Company name for updation:")
        #prepare and execute the query
        uq="update employee set sal=sal+sal*20/100,cname='%s' where eno=%d"
        cur.execute(uq %(cmpname,empno))
        con.commit()
        if(cur.rowcount!=0):
            print("{} Record(s) Updated--Verify".format(cur.rowcount))
        else:
            print("Employee Record Does not exist")
    except cx_Oracle.DatabaseError as db:
        print("Problem in DB:",db)
    except ValueError:
        print("Don't enter alnums,strs and symbols for employee Number:")
    except:
        print("Some thing went wrong!!!")

#main program
updaterecord()
