#Porogram for reading the data of the file
#FileReadEx1.py
try:
    filename=input("Enter the file name to view its content:")
    with open(filename) as fp:
        filedata=fp.read()
        print("content of file")
        print("------------------------------")
        print(filedata)
        print("------------------------------")
except FileNotFoundError:
    print("File does not exist")
