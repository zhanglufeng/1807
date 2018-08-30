from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.bind("",12333)
s.sendto("哈哈".encode("gb2312"),("192.168.43.191",8080))
while True:
	msg = s.recvfrom(1024)
	print(msg[0].decode("gb2312"))
	print(msg[1][0])
	#print(msg[1][1])
s.close()
