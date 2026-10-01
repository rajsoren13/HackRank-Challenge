'''arr=[70,20,50,30,90,5,15]
pass 1:[20,50,30,70,5,15,90]
pass 2:[20,30,5,15,50,70,90]
pass 3:[20,5,15,30,50,70,90]
pass 4:[5,15,20,30,50,70,90]
pass 5:[5,15,20,30,50,70,90]
pass 6:[5,15,20,30,50,70,90]

'''
arr=[70,20,50,30,90,5,15]
n=len(arr)
for i in range(n-1):
    for j in range(0,n-i-1):        
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print(f"step {i}: {arr}")

#print(arr)