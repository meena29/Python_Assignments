def binary(arr,val):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2
		if  arr[mid] < val :
			low = mid + 1
		elif arr[mid] > val:
			high = mid - 1
		else:
			#check for array bounds
			if mid - 1 < 0:
				return mid
			#if the index is the first occurence	
			if arr[mid - 1] != val:
				return mid
			#if the index is not the first occurence	
			high = mid - 1	
	return None			

arr = 	[-4,-1,4,107,107,345,345,345,800,890]
val = 4
ans = binary(arr,val)
print(ans)		
