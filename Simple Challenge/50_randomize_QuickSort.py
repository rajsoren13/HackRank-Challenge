import random
def randomize_QuickSort(number):
    if len(number)<=1:
        return number
    
    pivot_index=random.randint(0,len(number)-1)
    pivot=number[pivot_index]
    left=[]
    right=[]
    print("pivot_index:",pivot_index)

   
    for i,val in enumerate(number):
        if i==pivot_index:
            continue
        if val<pivot:
            left.append(val)
        else:
            right.append(val)
    return randomize_QuickSort(left) +[pivot]+randomize_QuickSort(right)

number=[7, 2, 9, 4, 1, 5]
result=randomize_QuickSort(number)
print(result)