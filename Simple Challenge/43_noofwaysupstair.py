
def noofways(n):
    if n<=1:
        return n
    else:
        return noofways(n-1)+noofways(n-2)


n=4
result=noofways(n)
print(result)