# Given an array of integers, find the continuous subarray, which when sorted, 
# results in the entire array being sorted. 
# For example: A = [0,2,5,3,1,8,6,9], result is the subarray [2,5,3,1,8,6]
# because, [2,5,3,1,8,6] when sorted => [1,2,3,5,8,6] will result in [0,1,2,3,5,8,6,9]

# [1,2,4,5,3,5,6,7,9] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.
# [1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] - indices 1 to 5

# import numpy as np

# #arr = np.array([0,2,5,3,1,8,6,9])
# arr = np.array([1,2,4,5,3,5,6,7,9])
# length = arr.size
# print(length)
# start = 0
# i = 0
# while i < length : 
# 	for j in range(i+1,length):
# 		if(arr[i] > arr[j]):
# 			if start == 0:
# 				start = i+1
# 				print(start)
# 			elif start != 0:
# 				end = j	
# 				print(end)
# 		i = i + 1
# 	i + j + 1
# print(start,end)			


import numpy as np

def findUnsortedSubarray(arr):
	l = len(arr)
    for i in range(1, l):
        if arr[i] < arr[i-1]:
            temp = min(arr[i:])
            break

    if temp == None:
        return 0

    start = None     
    for i in range(l):
        if arr[i] > temp:
            start = i
            break

    temp = None
    for i in range(l-2, -1, -1):
        if arr[i] > arr[i+1]:
            temp = max(arr[0:i+1])
            break

    end = None
    for i in range(l-1, -1, -1):
        if arr[i] < temp:
            end = i
            break
    print(start)
    print(end)
    print(nums[start:end+1])
    #return end - start + 1

#arr = np.array([0,2,5,3,1,8,6,9])
#arr = np.array([1,2,4,5,3,5,6,7,9])
#arr = np.array([3,1,5,2,6,4,7,8,9])
arr = np.array([])
findUnsortedSubarray(arr)