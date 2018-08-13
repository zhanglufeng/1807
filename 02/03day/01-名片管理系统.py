class Cardmn():
	def __init__(self):
		self.cards = []
	def insert(self):
		d = {}
		nmae = input("姓名")
		age = input("年龄")
		d["name"] = name
		d["age"] = age
		cards.append(d)
	def find(self):
		pass
	def change(self):
		pass
	def delete(self):
		pass
	def meun(self):
		while True:
			num = int(input("请选择功能1、添加 2、查看"))
			if num == 1:
				self.insert()
			if num == 2:
				self.find()
	def save(self):
		with open("data.data","w") as f:
			f.write(str(self.cards))
	def open(self):
		with open("data.data","r") as f:
		self.cards = eval(f.read())
		
			

