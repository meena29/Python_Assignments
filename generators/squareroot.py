def getnum(start,stop,step):
	if(start < stop):
		while (start<stop):
			num = start+step
			yield num
			start = num
	elif(start > stop):
		while(start > stop):
			num = start-step
			yield num
			start = num	

def squareroot(number):
	if(number < 0):
		print("wrong input")
	elif(number < 1):
		for item in getnum(0,number*100,0.01):
			a = item ** 2
			print(a >= number, a)
			if a >= number:
				print(item)
				break
	elif(number >= 1):
		for item in getnum(0,number/2,0.01):
			if item*item >= number:
				print(item)
				break
						
squareroot(69.72316)						