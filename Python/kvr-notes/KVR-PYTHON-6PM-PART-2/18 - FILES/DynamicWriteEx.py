#DynamicWriteEx.py
print("Enter the data from Key Board (press 'quit' to terminate the program)")
with open("Hyd.info","a") as fp:
    while(True):
        kbddata=input()
        if(kbddata.lower()!='quit'):
            fp.write(kbddata+"\n")
        else:
            print("Data Written to the file--Verify")
            break




