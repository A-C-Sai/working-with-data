#ThreadEx1.py
import threading
t=threading.current_thread()  # getName()---deprecated on the name of "name"
print("Default Thread Name=",t.name  )
print("Number of Active Threads=",threading.active_count())