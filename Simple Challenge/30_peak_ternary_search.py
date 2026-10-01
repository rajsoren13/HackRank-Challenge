def peak_search(arr,low,right):
    # If we have 2 or fewer items, just return the biggest one
    if right-low<2:
        if arr[low]>=arr[right]:
            return low
        else:
            return right
    
    mid1=low+(right-low)//3
    mid2=right-(right-low)//3
    if arr[mid1]<arr[mid2]:
        # Peak is on the right side
        return peak_search(arr,mid1+1,right) 
    else:
        # Peak is on the left side
        return peak_search(arr,low,mid2-1)


arr=[1, 3, 7, 12, 9, 5, 2]
low=0
right=len(arr)-1
result=peak_search(arr,low,right)
print(f"the peak value:{arr[result] }  present at index:{result}")