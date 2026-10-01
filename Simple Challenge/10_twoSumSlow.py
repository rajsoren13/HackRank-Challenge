def two_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print({nums[i]},{nums[j]})
            if nums[i] + nums[j] == target:
               
                return [i, j]
            

nums=[12,7,11,2]
target=9
d=two_sum_slow(nums,target)
print(f"\nInput:  {nums}")
print(f"Target: {target}")
print(f"Goal:   Find two numbers that add up to {target} are :{d} ")