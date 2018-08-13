import random
class youxi:
	def caishuzi(self):
		number = random.randint(1,100)
		for i in range(10):
			num = int(input("请输入一个数"))
			if num > number:
				print("猜大了")
			elif num < number:
				print("猜小了")
			elif num == number:
				print("猜对了")
				break

csz = youxi()
csz.caishuzi()

