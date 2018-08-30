from multipracecssing import Process
import time
def show(name):
	for i in range(10):
		time.sleep(2)
		print(name)

p = Process(target=show,args("割草",))
p.start()


time.sleep(3)
p.terminate()
print("吃喝玩乐")
