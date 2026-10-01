
def bunarysearch(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:

             low=mid+1
        else:
            high=mid-1


nums=[3, 7, 12, 18, 23, 29, 33, 41, 47, 55, 62, 70]
target=18
result=bunarysearch(nums,target)
print(f"position of target item: {result}")