def findbin(nums,target,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            #low=mid+1
            return findbin(nums,target,mid+1,high)
        else:
           # high=mid-1
           return findbin(nums,target,low,mid-1)
    return -1

nums=[3, 7, 12, 18, 23, 29, 33, 41, 47, 55, 62, 70]
target=55
low =0
high=len(nums)-1
result=findbin(nums,target,low,high)
print("position of target:",result)