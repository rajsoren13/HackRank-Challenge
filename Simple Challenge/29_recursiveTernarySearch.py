def ternarysearch(arr,target,l,r):
    
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if arr[mid1]==target:
            return mid1
        if arr[mid2]==target:
            return mid2
    
        if arr[mid1]>target:
            #r=mid1-1
            return ternarysearch(arr,target,l,mid1-1)
        elif arr[mid2]<target:
            #l=mid2+1
            return ternarysearch(arr,target,mid2+1,r)
        else:
            return ternarysearch(arr,target,mid1+1,mid2-1)
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
l=0
r=len(arr)-1
target=5
result=ternarysearch(arr,target,l,r)
print(f"target value is present at index:{result}")