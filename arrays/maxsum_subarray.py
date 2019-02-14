# Given an array of integers, find the contiguous subarray with the maximum sum. The array can contain both negative and positive integers.

def maxsum_subarray(arr):
		maxSum = 0
		currMax = 0
		#start and end holds the maxSum subarray
		start = 0
		end = 0
		#begin is for current traversal
		begin = 0

		for i in range(0,len(arr)):		
			currMax = currMax + arr[i];
			#reset the values if curr max sum hits negative 
			if currMax < 0:
				currMax = 0	
				begin = i + 1
			#update if a new higher sum is found
			if (maxSum < currMax):
				maxSum = currMax
				start = begin
				end = i

		if(maxSum == 0):
			maxSum = sum(arr[start:end+1])
		print(maxSum)
		print(arr[start:end+1])

arr = [-2,1,-3,4,-1,2,1,-5,4]
arr1 = [8,-7,-3,5,6,-2,3,-4,2]
arr2 = []
arr3 = [-1,-2,-3]
arr4 = [-1,0,1]
maxsum_subarray(arr)
maxsum_subarray(arr1)
maxsum_subarray(arr2)
maxsum_subarray(arr3)
maxsum_subarray(arr4)
