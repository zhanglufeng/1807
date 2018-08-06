
name = input("请输入要备份的文件名(添加后缀名)")
f = open(name,"r")


position = name.rfind(".")
newname = name[:position]+"备份"+name[position:]

f1 = open("备份.txt","w")
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
f.close()
f1.close()

