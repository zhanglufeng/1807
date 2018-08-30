import os
pid = os.fork()
print(pid)
if pid == 0:
	print("子进程是%d"%os.getpid())
else:
	print("父进程是%d"%os.getpid())
