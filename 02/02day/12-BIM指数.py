class BIM():
	def bim(self):
		height = float(input("请输入身高:m"))
		weight = float(input("请输入体重:kg"))
		bim = weight/height**2
		if bim < 18.5:
			print("过轻")
		elif bim > 18.5 and bim <25:
			print("正常")
		elif bim > 25 and bim < 28:
			print("过重")
		elif bim > 28 and bim < 32:
			print("肥胖")
		else:
			print("严重肥胖")

b = BIM()
b.bim()


