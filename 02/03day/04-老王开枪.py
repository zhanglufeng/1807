import random
import time
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def zhuangzidan(self,dj,zd):
		dj.addzd(zd)
	def zhuangdanjia(self,dj,gun):
		gun.addDanjia(dj)
	def naqiang(self,gun):
		self.gun = gun
	def kaiqiang(self,diren):
		self.gun.kaihuo(diren)
	def diaoxue(self,count):
		self.hp -= count
		if self.hp <= 0:
			print("挂了学量剩%d"%self.hp)
		else:
			print("敌人%s还剩%d"%(self.name,self.hp)) 
class Gun():
	def __init__(self,name):
		self.name = name
		self.dj = None
	def addDanjia(self,dj):
		self.dj = dj
	def kaihuo(self,diren):
		zidan = self.dj.tanzidan()
		zidan.sharen(diren)

class Zidan():
	def __init__(self,name,sh):
		self.name = name
		self.sh = sh
	def sharen(self,diren):
		diren.diaoxue(self.sh)
		
class Danjia():
	def __init__(self,rl):
		self.rl = rl
		self.zds = []
	def addzd(self,zd):
		self.zds.append(zd)
	def tanzidan(self):
		return self.zds.pop(0)


lw = Person("老王")
print("老王出生")
time.sleep(1)
gun = Gun("ak47")
print("出现一把ak47")
time.sleep(1)
dj = Danjia("40")
print("装子弹中")
for i in range(40):
	zd = Zidan("5.56",random.randint(1,100))
	lw.zhuangzidan(dj,zd)
lw.zhuangdanjia(dj,gun)
time.sleep(1)
lw.naqiang(gun)
print("老王拿起枪")
time.sleep(1)
ls = Person("老宋")
print("出现一个敌人老宋")
while True:
	time.sleep(1)
	print("老王开枪")
	lw.kaiqiang(ls)
	if ls.hp <= 0:
		break

