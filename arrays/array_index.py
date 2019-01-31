import numpy as np

# length = input()
# l = []
# for i in range(0,length):
# 	l.append(int(input()))	
# arr = np.array(l)


#use arrays [3,20,4,6,7,2,1,2], [3,5,4,6,7,-1,1,2], [3,5,4,6,7,2,1,2],[3,5,2,6,7,2,1,2] 


arr = np.array([3,5,4,6,7,2,1,2])
print(arr)
length = arr.size
index = 0
count = 0

while count < 100:
	if index == -1:
		break
	elif index >= length:
		break
	count = count + 1	
	index = arr[index]	

print(count)	
			


