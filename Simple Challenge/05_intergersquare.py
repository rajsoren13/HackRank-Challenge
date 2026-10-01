'''

Task:
The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .
'''


if __name__=='__main__':
    n = int(input())
    for i in range(0,n):
        if i>=0:
            print(i*i)
    

w=[7,3,23,42]
x=w[1:]
y=w[1:]
z=w
y[0]=10
z[1]=20
print(w)