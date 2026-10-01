def quick_sort(arr):

    if len(arr)<=1:
            return arr

    pivot_index=len(arr)//2
    pivot=arr[pivot_index]
    left=[]
    right=[]
    
    for x in range(len(arr)):
        if x==pivot_index:
             continue
        if arr[x]<pivot:
            left.append(arr[x])
        else:
            right.append(arr[x])
    return quick_sort(left)+[pivot]+quick_sort(right)


number=[7, 2, 9, 4, 1, 5]
result=quick_sort(number)
print(result)