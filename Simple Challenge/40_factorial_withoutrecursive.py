def fact(n):
    result=1
    if n==1 or n==0:
        return 1
    else:
        for i in range(2,n+1):
            result=result*i
        return result
            


n=8
result=fact(n)
print(f"factorial of {n} is {result}")