import random
class youxi():
	def shi(self):
		print("1:石头\n2:剪刀\n3:布")
		for i in range(10):
			computer = random.randint(1,3)
			player = int(input("请选择"))
			if player > 0 and player < 4:
				if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
					print("玩家赢")
				elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
					print("电脑赢")
				else:
					print("平局")
			else:
				print("非法输入")

s = youxi()
s.shi()
