class showError(Exception):
	def __init__(self,name):
		self.name = name



class Input():
	
	def input(self):
		self.name = input("请输入名字")
		try:
			if self.name == "老王":
				raise showError(self.name)
		except showError as ret:
			print("名字不能是%s"%(ret.name))


lw = Input()
lw.input()


		





	
