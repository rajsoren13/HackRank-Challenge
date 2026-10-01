
def findmaxmin(arr,i,j):
    if i==j:
        max_val=arr[i]
        min_val=arr[j]
    elif i==j-1:
        if i<j:
            max_val=arr[j]
            min_val=arr[i]
        else:
            max_val=arr[i]
            min_val=arr[j]
    else:
        mid=i+(j-i)//2
        max_l,min_l=findmaxmin(arr,i,mid)
        max_r,min_r=findmaxmin(arr,mid+1,j)
        #combine
        if max_l<max_r:
            max_val=max_r
        else:
            max_val=max_l
        if min_l<min_r:
            min_val=min_l
        else:
            min_val=min_r

    return max_val,min_val




arr=[34,56,12,59,70,29,90,67,20]
i=0
j=len(arr)-1
max_val,min_val=findmaxmin(arr,i,j)
print("maximum and min",max_val,min_val)