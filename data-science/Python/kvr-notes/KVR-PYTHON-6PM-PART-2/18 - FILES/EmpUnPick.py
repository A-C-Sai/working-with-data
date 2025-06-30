#Program for  reading employee records which are present employee file by using Un-Pickling
#EmpUnPick.py---Program-(B)
import pickle
def reademprecords():
    try:
        with open("empinfo.data","rb") as fp:
            print("*"*60)
            print("\tENO\tNAME\tSALARY")
            print("*"*60)
            while(True):
                try:
                    emprecs=pickle.load(fp)
                    for val in emprecs:
                        print("\t{}".format(val),end=" ")
                    print()
                except EOFError:
                    print("*" * 60)
                    break

    except FileNotFoundError:
        print("File does not exist")

#main program
reademprecords()