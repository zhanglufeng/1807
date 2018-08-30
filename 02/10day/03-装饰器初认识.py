def w1(fun):
	def inner():
		print("检查登录")
		fun()
	return inner


@w1 #相当于pay = w1(pay) 语法糖 
def pay():
	print("支付中")

@w1
def pay1():
	print("支付成功")


#pay()
#inner = w1(pay)
#inner()
#pay = w1(pay)
pay()
pay1()
