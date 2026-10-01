
def searchvalue(matrix,target,x,y):
    #i=0
    
    for i in matrix:
       # print(i,"==>")
        x=x+1
        y=-1
        for j in i: 
           # print(j,"<==",end=" ")
            y=y+1  
           # print("value of x y=> value",x,y,j)
            if j==target:
                return x,y


    return -1,-1    #print()


matrix = [
 [1, 3, 5, 7],
 [8, 11, 13, 20], 
[22, 25, 28, 29]
 ]

target=13
x=-1
y=-1
result= searchvalue(matrix,target,x,y)
print(f"Index  value is :{result}")