def getElement(matrix,target,x,y):
    i=0
    j=0
 
    for i in matrix:
        x=x+1
        y=-1
        for j in i:
            y=y+1
            print(j,end=" ")
            if j==target:
                print()
                return True
        print()

    return False
matrix = [
 [1, 3, 5, 7],
 [8, 11, 13, 20], 
[22, 25, 28, 29]
 ]
target=28
x=-1
y=-1

result=getElement(matrix,target,x,y)
print(f"\nValue is present:{result}")