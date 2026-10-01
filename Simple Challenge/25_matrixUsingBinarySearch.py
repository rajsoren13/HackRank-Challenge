






matrix = [
 [1, 3, 5, 7],
 [8, 11, 13, 20], 
[22, 25, 28, 29]
 ]
k=[]
target=25
for i in matrix:
    for j in i:
        #print (j, end=" ")
        k.append(j)

print(f"\n value of k:{k}")
x=0
y=len(k)-1
row=0
column=0
no_of_column=len(matrix[0])

while x<=y:
    mid=x+(y-x)//2
    if k[mid]==target:
        row=mid//no_of_column
        column=mid%no_of_column
        
        break
    elif k[mid]<target:
         x=mid+1
    else:
        y=mid-1
print(f"value is present at in a row major search: {mid}")      
print(f"\nvalue is present at index: [{row}][{column}]")
        
