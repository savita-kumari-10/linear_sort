def linear_sort(arr,size):
    for i in range(1,size):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr=[23,4,12,5,6,20]
size_=len(arr)
result= linear_sort(arr,size_)
print(result)
