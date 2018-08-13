class Dog():
	def __init__(self):
		self.__age = 0
	def sleep(self):
		print("sleep")

	def setAge(self,age):
		if age > 15 or age < 1:
			print("年龄不符")
		else:
			self.__age = age
	def getAge(self):
		return self.__age


hashiqi = Dog()
hashiqi.setAge(100)
print(hashiqi.getAge())




