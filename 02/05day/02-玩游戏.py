class Game():
	count = 3
	def __init__(self,name):
		self.name = name
	def play(self):
		print("大家一起玩游戏")
	classmethod
	def get(cls):
		return cls.count
	staticmethod
	def print_menu():
		print("开始游戏")
		print("结束游戏")
	

cq = Game("传奇")
cq.play()





