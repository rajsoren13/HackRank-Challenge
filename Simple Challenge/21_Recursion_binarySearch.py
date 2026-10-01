

def recurbinarysearch(arr,target,low,high):
  

    while low<=high:
                
          mid=low+(high-low)//2
          if arr[mid]==target:
            return mid
          elif arr[mid]<target:
            return recurbinarysearch(arr,target,low+1,high)
          else:
            return recurbinarysearch(arr,target,low,mid-1)
    return -1


arr=[23,35,36,41,47,53]
low=0
high=len(arr)-1
target=47
result=recurbinarysearch(arr,target,low,high)
print(f"Element present at index:{result}")