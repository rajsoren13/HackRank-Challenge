
def selection_sort(arr,n):

    for i in range(n): 
     
        min=i

        for j in range(i+1,n):

            if arr[j]<arr[min]:
                min=j
        if min!=i:
            arr[i],arr[min]=arr[min],arr[i]     
    return arr     





arr=[70,20,50,30,90,5,15]
n=len(arr)
result=selection_sort(arr,n)
print(f"selection sort:{result}")