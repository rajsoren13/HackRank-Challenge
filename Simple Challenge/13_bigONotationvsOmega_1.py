def searcvalue(arr,target):
    for i in range(len(arr)):
       
        if arr[i]==target:
            return i


arr=[1,2,3,4,5]
target=1
output=searcvalue(arr,target)
print(f'target found at :{output}')

# Best case → target is at the START → found in 1 step → Ω(1)
