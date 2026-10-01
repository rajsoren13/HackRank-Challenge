from collections import Counter
import heapq
def topKfrequent(arr,k):
    if k==len(arr):
        return set(arr)
    count=Counter(arr)
    print(count)
    #Counter is a dictionary which contains unique values
    return heapq.nlargest(k,count.keys(),key=count.get)
    #key=count.get, you tell Python: "Don't rank the numbers by their own value.
    #  Instead, look inside the count dictionary, find out how many times they appeared,
    #  and rank them by that frequency."                      



arr=[1,1,1,1,2,2,2,3]
k=3
result=topKfrequent(arr,k)
print(f"the top k frquent element:{result}")