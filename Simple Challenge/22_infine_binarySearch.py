
def searchinfinitevalue(x,target,i,j):
 
    while i<=j:
           mid=i+(j-i)//2
           if x[mid]==target:
                 return mid
           elif x[mid]<target:
                 i=mid+1
           else:
                 j=mid-1
    return -1

arr=[-45, float('inf'), 67, -12, 3, float('inf'), 89, -7]
target=float('inf')
arr.sort()
print(f"Sorted Array:{arr}")
x=[]
x=list(arr)
#x=x[:n-1]
i=0  
j=len(x)-1

result=searchinfinitevalue(x,target,i,j)
print(f"index of infine value is:{result}")