
def recursivebinarysearch(nums,target,low,high):
   
    if low>high:
        return -1
    
    mid=(low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return recursivebinarysearch(nums,target,mid+1,high)
    else:
        return recursivebinarysearch(nums,target,low,mid-1)

nums=[3, 7, 12, 18, 23, 29, 33, 41, 47, 55, 62, 70]
target=47
low=0
high=len(nums)-1
result=recursivebinarysearch(nums,target,low,high)
print(f"target value is at index: {result}")