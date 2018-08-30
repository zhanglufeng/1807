def show(num):
	def inner(a,b):
		return a+b+num
	return inner

i = show(1)
print(i(1,5))


def line_conf(a,b):
	def line(x):
		return a*x+b
	return line

line = line_conf(2,3)
print(line(3))
print(line(5))

def line1(a,b,x):
	return a*x+b
line1(2,3,3)
line1(3,5,4)

