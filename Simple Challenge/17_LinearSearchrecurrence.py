
def linearSearch(arr,target):
    indices=[]
    for i in range(len(arr)):
        if arr[i]==target:
            indices.append(i)
    return indices
   
arr=[45,34,90,14,71,90,3,10,90]
target=90
result=linearSearch(arr,target)
print(f"value is at index: {result}")


def linearSearchEnu(arr,target):
    indicesv=[]
    for i,val in enumerate(arrv):
        if val==targetv:
            indicesv.append(i)
    return indicesv
   
arrv=[70,34,20,48,23,34,3,34,90]
targetv=34
resultv=linearSearchEnu(arrv,targetv)
print(f"recurrence value are at index: {resultv}")