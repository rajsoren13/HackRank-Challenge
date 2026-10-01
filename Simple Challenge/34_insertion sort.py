arr=[70,20,50,30,90,5,15]
n=len(arr)
for i in range(1, n): 
    # Outer Loop: Selects the 'key'
    # The value we want to insert
    key = arr[i]
    # Look at the sorted portion to the left             
    j = i - 1                
     # Inner Loop: Shift elements
    while j >= 0 and key < arr[j]:
        # Move the larger element right
        arr[j + 1] = arr[j] 
        # Move pointer left 
        j -= 1               
    # Place the key in the gap    
    arr[j + 1] = key         

print(f"insertion SOrt:{arr}")



