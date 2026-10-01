
def twoPointerApp(arr,target):
    l=0
    r=len(arr)-1
    for i in range(len(arr)-1):
        if arr[l]+arr[r]==target:
            return l,r
        elif arr[l]+arr[r]>target:
            r=r-1
        else:
            l=l+1
    return -1,-1

arr = [20,37,40,50,64,90,102]
target=90
result=twoPointerApp(arr,target)
print(result)