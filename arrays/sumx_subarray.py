def sumxSubarray(arr,val): 
    currSum = arr[0] 
    start = 0 
    i = 1
    while i <= len(arr):  
        #if current sum exceeds the required sum, remove elements from start
        while currSum > val and start < i-1:           
            currSum = currSum - arr[start] 
            start += 1
        if currSum == val: 
            print(arr[start:i])
            return 1 
        if i < len(arr): 
            currSum = currSum + arr[i] 
        i += 1
    print ("[]") 
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23] 
val = 23  
sumxSubarray(arr,val)


arr = [9,5,14,7,2,10,1,3,5,8] 
val = 8
sumxSubarray(arr,val)

arr = [9,5,14,7,2,10,1,1,5,8] 
val = 4
sumxSubarray(arr,val)

arr = [10,5,6,7] 
var = 13 
sumxSubarray(arr,var)