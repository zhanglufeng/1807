#coding = utf-8
try:
#	open("1.txt","r")
	11/0
except (FileNotFoundError,NameError):
	print("报错了")
except Exception as ret:
	print("报错了",ret)
else:
	print("没有错执行")
finally:
	print("有没有错都执行")
