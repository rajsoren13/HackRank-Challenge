def sel_proc(arr,k):
    if len(arr)<=1:
        return arr
    pivot_index=len(arr)//2
    pivot=arr[pivot_index]
    left=[]
    middle=[]
    right=[]
    for x in range(len(arr)):
        
        if arr[x]<pivot:
            left.append(arr[x])
        elif arr[x]>pivot:
            right.append(arr[x])
        else:
            middle.append(arr[x])
    if k<len(left):
        # Target is in the left partition
        return sel_proc(left,k)
    if k<len(left)+len(middle):
        # Target falls right inside the pivot/middle group
        return pivot
    else:
        # Target is in the right partition; shift k index accordingly
        return sel_proc(right,k-len(left)-len(middle))    

number = [7, 2, 9, 4, 1, 5]
smallest_indexnumber=3
result=sel_proc(number,smallest_indexnumber)
print(f"{smallest_indexnumber}th smallest number in array:",result)