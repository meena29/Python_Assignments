def dutch_flag(arr,num):
    
    low = 0
    mid = 0 
    high = len(arr)-1
    while mid <= high:
        temp = arr[mid]
        if temp < num:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif temp == num:
            mid += 1
        elif temp > num:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)

#arr = [1,2,3,3,9,4,4,4,5,4,332,124,24,4,4,2134,213,9,313,2,1]
#arr = []
#arr = [1,31,13]
arr = [1,2,3,3,4,4,4,5,4,332,124,24,4,4,2134,213,313,2,1]
num = 9
dutch_flag(arr,num)
arr1 = [1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
num1 = 4
dutch_flag(arr1,num1)
arr2 = [1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
num2 = 1
dutch_flag(arr2,num2)