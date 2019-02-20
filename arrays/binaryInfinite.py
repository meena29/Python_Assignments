def binaryInfinite(arr,low,high,val):
	if high >= low:
		mid = low + (high-low)/2
		if arr[mid] == val:
			return mid
		if arr[mid] > val:
			return binaryInfinite(arr,low,mid-1,val)
		return binaryInfinite(arr,mid+1,high,val)
	return None

def findbounds(arr,val):
	low = 0
	high = 1
	temp = arr[0]
	while temp < val:
		low = high
		high = 2 * high
		temp = arr[high]
	return binaryInfinite(arr,low,high,val)

arr = [4,5,7,12,34,45,51,68,73,100,389,470,501,699,712,999,1000,1200,1567,1789,1900,2100,2400,2567,2600,2890,3456]
val = 501
ans = findbounds(arr,val)
print(ans)		
