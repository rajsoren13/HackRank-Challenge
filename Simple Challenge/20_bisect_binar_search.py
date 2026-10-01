import bisect
nums=[3, 7, 12, 18, 23, 29, 33, 41, 47, 55, 62, 70]
target=47
result=bisect.bisect_left(nums,target)
if result<len(nums) and nums[result]==target:
    print(f"Found at index {result}")
else:
    print("Target not found")

