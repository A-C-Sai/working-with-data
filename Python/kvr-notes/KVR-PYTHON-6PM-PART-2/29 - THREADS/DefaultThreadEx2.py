#Program for demonstrating single thread name - python program and whose name "MainThread"
#DefaultThreadEx2.py
import threading
def  hello():
	print("\nDefault Thread Name Line 5--hello():",threading.current_thread().name)
	print("Hello, Good Evening")

def hi(msg):
	print("\nDefault Thread Name Line 9--hi():",threading.current_thread().name)
	print("Hi {}, Good Night".format(msg))

def welcome():
	print("\nDefault Thread Name Line 13--welcome():",threading.current_thread().name)
	print("Wel come to Python Classes")

#main program
print("-------------------------------------------------")
print("Program Execution Started--Line:15")
print("-------------------------------------------------")
print("Default Thread Name Line:20:",threading.current_thread().name)
hello()
print("\nMainThread came to main Program-22")
hi("Rossum")
print("\nMainThread came to main Program-24")
welcome()
print("\nMainThread came to main Program-26")
print("-------------------------------------------------")
print("Program Execution Ended")
print("-------------------------------------------------")