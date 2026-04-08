def bubble(arr):
    num=0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                num=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=num
    return arr
arr=[2,5,3,8,1,9,7,4,6,10]
a=bubble(arr)
print(a)