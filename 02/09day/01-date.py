import time 

date = input("请输入日期，格式yyyymmdd")
y = int(date[0:4])
m = int(date[4:6])
d = int(date[6:])

ly = False

if y%400 == 0 or (y%4 == 0 and y%100 == 0):
	ly = True
else:
	ly = False


if ly == True:
	ms = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
	ms = [31,28,31,30,31,30,31,31,30,31,30,31]

days = 0

for i in range(1,13):
	if i == m:
		for j in range(i-1):
			days += ms[j]
print("%s是%d年的第%d天"%(date,y,(days+d)))



