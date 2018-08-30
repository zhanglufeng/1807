
m socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",5632))
s.listen(5)
s1,info = s.accept()
print("有新连接")
print(s1.recv(1024).decode("decode"))
s1.send("哈哈".encode("gb2312"))
s1.close()
s.close()
