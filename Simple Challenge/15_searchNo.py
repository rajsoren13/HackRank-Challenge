
def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
        
    return -1
arr=[1,4,3,6,7,8]
x=6
result=linearsearch(arr,x)

print(f"value is present at {result} ")

d=[1,4,3,6,7,8]
d.insert(4,14)
print(f"insert:{d}")

p=[1,4,3,6,7,8]
p.remove(3)
print(f"remove:{p}")

p1=[1,4,3,6,3,8]
a=p1.count(3)
print(f"count:{a}")


p2=[1,4,3,6,3,8]
b=p2.pop(3)
print(f"delete:{b}")

p3=[1,4,3,6,3,8]
p3.sort()
print(f"Sort:{p3}")


p6 = [10, 20]  # Defining p2 first
p7 = [1, 4, 3, 6, 3, 8]

# Add7elements of p4 to p2
p6.extend(p7)
print(p6)