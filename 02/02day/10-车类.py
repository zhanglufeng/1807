class Car():
	def __init__(self):
		self.color = "蓝色"
		self.type = "xxx"
	def run(self):
		print("移动")
	def music(self):
		print("听音乐")
	def __str__(self):
		msg = "颜色是%s,型号是%s"%(self.color,self.type)
		return msg
	#def introduce(self):
	#	print("颜色是%s,型号是%s"%(self.color,self.type))

car = Car()
car.run()
car.music()
print(car)
#car.introduce()

