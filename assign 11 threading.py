print("create a threading process such that it sleeps for 5 seconds amd then prints out the message-\n")
import threading
from threading import Thread
import time
def display():
	time.sleep(5)
	print("it was slept for 5 seconds")
t1=Thread(target=display)
t1.start()
print("\n###############")



print("thread that prints 1-10 after 1-1 seconds")
import threading 
from threading import Thread
import time
def display():
	for x in range(1,11):
		time.sleep(1)
		print("value of x is:",x)
t1=Thread(target=display)
t1.start()


print("make list of 5 sec.create threading process that prints the 5 elements of the list with a delay of multiple of 2sec b/w each display")
import threading 
from threading import Thread
import time
def display():
	s=2

	for x in li:
		print("elements in list are:",x)
		time.sleep(s)
		s=s+2

li=[1,5,3,7,4]
t=Thread(target=display())
t.start()


print("call factorial function using thread")
import threading 
from threading import Thread
import time
def factorial():
	n=int(input("enter the no: "))
	fact=1
	for x in range(1,n+1):
		fact=fact*x
	print(fact)
t1=Thread(target=factorial)
t1.start()