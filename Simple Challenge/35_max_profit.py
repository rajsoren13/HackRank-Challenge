#time complexity:O{n^2)
#space complexity:O(1)
price=[7,1,5,3,6,4,15]
max=0
for i in range(len(price)):    
    for j in range(len(price)):                        
        val=price[j]-price[i]                 
        if val>max:
            max=val
            buy=price[i]
            sell=price[j]
print(f" buy:{buy}  sell:{sell}  Max profit:{max} ")
           



    
