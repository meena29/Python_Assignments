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


def cuberoot(number):
	if((number < 0 and number > -1) or (number > 0 and number < 1) ):
		for item in getnum(0,number*100,0.01):
			#print(item)
			if item*item*item < number:
				print(item)
				break
	elif(number <= -1 or number >= 1):
		for item in getnum(0,number/2,1):
			if item*item*item > number:
				print(item)
				break		

cuberoot(-0.125)