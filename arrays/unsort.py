
def Unsorted(arr):
        temp = 0
        leng = len(arr)
        for i in range(1, leng):
            if arr[i] < arr[i-1]:
                temp = min(arr[i:])
                break

        if temp == 0:
            print(arr)
            print("Already sorted")
            return 0
    
        for i in range(leng):
            if arr[i] > temp:
                start = i
                break

        for i in range(leng-2, -1, -1):
            if arr[i] > arr[i+1]:
                temp = max(arr[0:i+1])
                break

        for i in range(leng-1, -1, -1):
            if arr[i] < temp:
                end = i
                break
        print(arr)
        print(arr[start:end+1])

arr = []
arr1 = [0,2,5,3,1,8,6,9]
arr2 = [1,2,4,5,3,5,6,7,9]
arr3 = [3,1,5,2,6,4,7,8,9]
arr4 = [1,3,5,2,6,4,7,8,9]
arr5 = [1,2,3,4,5,6,7,8,9]

Unsorted(arr)
Unsorted(arr1)
Unsorted(arr2)
Unsorted(arr3)
Unsorted(arr4)
Unsorted(arr5)