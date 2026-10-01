def finndmaxprofit(price):
    min_price=float('inf')
    max_profit=0
    for i in range(len(price)):  
        if price[i]<min_price:
            min_price=price[i]
        elif price[i]-min_price>max_profit:
            max_profit=price[i]-min_price
    return max_profit


price=[7,1,5,3,6,4,15]
maxprofit=finndmaxprofit(price)
print(f" Max profit:{maxprofit} ")