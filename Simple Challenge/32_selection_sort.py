'''
Pass 0: arr=[70,20,50,30,90,5,15]
Pass 1: arr=[20,20,50,30,90,5,15]


'''
arr=[70,20,50,30,90,5,15]
n=len(arr)
for i in range(n-1):
   
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j        
        
    if min!=i:
        arr[i],arr[min]=arr[min],arr[i]
print(f"{arr}")