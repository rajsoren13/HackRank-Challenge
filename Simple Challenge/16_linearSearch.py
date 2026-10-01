

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[45,34,90,14,71,3,10]
target=14
result=linearSearch(arr,target)
print(f"value is at index: {result}")