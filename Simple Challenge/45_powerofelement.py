def findPower(a,n):
    if n==0:
        return 1
    
    elif n<1:
        a=1/a
        n=-n
        result=findPower(a,n)
        return result
    elif n==1:
        return a

    else:
        mid=n//2
        result=findPower(a,mid)
        if n%2==0:
            return result*result
        else:
            return result*result*a      


a=2
n=5
finalresult=findPower(a,n)
print(f"Power of element 2^{n}:", finalresult)