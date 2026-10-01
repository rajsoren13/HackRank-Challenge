def fib1(n):
    
    if n<=1:
        return n
    else:
        return fib1(n-1)+fib1(n-2)



n=8
for i in range(n):
    print(fib1(i),end=" ")


