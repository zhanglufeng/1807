from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("192.168.43.191",8679))
s.send("哈哈哈".encode("gb2312"))
while True:
	msg = s.recv(1024).decode("gb2312")
	print(msg)
