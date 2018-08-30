class Dog():
	__instance = None
	__flag = False
	def __init__(self,name):
		if Dog.__flag == False:
			self.name = name
			Dog.__flag = True
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance


dog1 = Dog("旺财")
print(id(dog1))

dog2 = Dog("二哈")
print(id(dog2))
