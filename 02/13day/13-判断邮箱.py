import re 
def chceckphone(phone):
	ret = re.match(r"1[3456789]\d{9}$",phone)
	if ret:
		return True
	else:
		return False

ret = chceckphone("14578978988")
print(ret)
