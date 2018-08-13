class Phone():
	count = 0

	def __init__(self,color):
		self.color = color
		Phone.count+=1 
	def dadianhua(self):
		print("打电话")
	
		
xiaomi = Phone("白色")
print(xiaomi.count)
