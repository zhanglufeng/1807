
name = input("请输入要备份的文件名(添加后缀名)")
f = open(name,"r")
content = f.read()

position = name.rfind(".")
newname = name[:position]+"备份"+name[position:]

f1 = open("备份.txt","w")

f1.write(content)

f.close()
f1.close()

