import numpy as np

#arr = np.array([3,5,4,6,7,2,1,2])
arr = np.array([])
print(arr)
length = arr.size
i = 0
l = []
while i < length:
	if arr[i] % 2 == 0:
		l.append(arr[i])
	l.append(arr[i])
	i = i + 1
arr = np.array(l)
print(arr)	


# l = list([3,5,4,6,7,2,1,2])
# #l = []
# print(l)
# length = len(l)
# i = 0
# while i < length:
# 	if(l[i] % 2 == 0):
# 		l[i:i] = list([l[i]])
# 		i = i + 1
# 	i = i + 1	
# print(l)	
