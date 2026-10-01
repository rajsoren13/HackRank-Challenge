# O(n) — convert list to SET first
def common_element(a,b):
     # O(n) — build set once
    b_set=set(b)
    common=[]
    # O(n) loop
    for i in a:
        # O(1) set lookup ← safe!
        if i in b_set:
            common.append(i)
    return common

a=[1,2,3,4,5]
b=[7,5,6,3,8]
result=common_element(a,b)
print(f"common element in list:{result}")
