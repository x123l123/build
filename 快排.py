def quick(arr):
    def quick_sort(arr,low,high):
        if low<high:
            mid=average(arr,low,high)
            quick_sort(arr,low,mid-1)
            quick_sort(arr,mid+1,high)
    def average(arr,low,high):
        num=0
        count=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<count:
                i+=1
                num=arr[j]
                arr[j]=arr[i]
                arr[i]=num
        num=arr[high]
        arr[high]=arr[i+1]
        arr[i+1]=num
        return i+1
    quick_sort(arr,0,len(arr)-1)
    return arr

arr=[21,51,31,81,11,91,71,41,61,10]
a=quick(arr)
print(arr)