if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x={}
    x=list(set(arr) )
    x.sort()
    d=len(x)
    runner=x[d-2]    
    print(runner)
     



  