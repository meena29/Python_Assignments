# Given an array of integers, find the contiguous subarray with the maximum sum. The array can contain both negative and positive integers.

# Given an array of positive integers, find the contiguous subarray that sums to a given number X.

# Given an array of integers, find the contiguous subarray that sums to 0. The array can contain both negative and positive integers.

def maxsum_subarray(arr):
#stores maximum sum sub-array found so far
		maxSoFar = 0

		#stores maximum sum of sub-array ending at current position
		maxEndingHere = 0

		#stores end-points of maximum sum sub-array found so far
		start = 0
		end = 0

		#stores starting index of a positive sum sequence
		beg = 0

		#traverse the given array
		for i in range(0,len(arr)):		
			#update maximum sum of sub-array "ending" at index i
			maxEndingHere = maxEndingHere + arr[i];

			#if maximum sum is negative, set it to 0
			if maxEndingHere < 0:
				maxEndingHere = 0	# empty sub-array
				beg = i + 1

			#update result if current sub-array sum is found to be greater
			if (maxSoFar < maxEndingHere):
				maxSoFar = maxEndingHere
				start = beg
				end = i

		print(maxSoFar)
		print(arr[start:end+1])

arr = [-2,1,-3,4,-1,2,1,-5,4]
maxsum_subarray(arr)