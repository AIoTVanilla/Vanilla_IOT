from threading import Thread
import subprocess

t1 = Thread(target=subprocess.run, args=(["python3", "socket_client.py"],))
t2 = Thread(target=subprocess.run, args=(["python3", "HC-SR04_RGB.py"],))

t1.start()
t2.start()

t1.join()
t2.join()