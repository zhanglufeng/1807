class Zuoditie():
	def zuoditie(self):
		money = 0
		d = float(input("输入"))
		for i in range(1,31):
			print("第%d天坐地铁"%i)
			for j in range(1,3):
				print("%d"%j)
				if d <= 6:
					p = 3
				elif d > 6 and d <= 12:
					p = 4
				elif d > 12 and d <= 22:
					p = 5
				elif d > 22 and d <= 32:
					p = 6
				else:
					if (d-32)%20 == 0:
						p = 6+(d-32)/20
					else:
						p = 6+int((d-32)/20)+1
				if money >100 and money<=150:
					p= p*0.8
				elif money > 150 and money <=400:
					p = p*0.54
				money = money+p
		print("%f"%money)

zdt = Zuoditie()
zdt.zuoditie()
