#Program for demonstrating single thread name - python program and whose name "MainThread"
#DefaultThreadEx1.py
import threading
t=threading.current_thread()
print("Default Thread Name:",t.name)
print("This is Multi Therading class")
print("Started Today")
print("Number of Active Threads=",threading.active_count())