
for i in range(100,200):
	j = 2
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		print(i)
