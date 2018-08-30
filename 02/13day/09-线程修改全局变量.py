from threading import Thread 
import time
num = 0
def work1():
	global num
	for i in range(100000):
		num += 1
	print("thread-1")
	print(num)
def work2():
	global num
	for i in range(100000):
		num += 1
	print("thread-2")
	print(num)
t1 = Thread(target=work1)
t1.start()
t1.join()
t2 = Thread(target=work2)
t2.start()
print(num)