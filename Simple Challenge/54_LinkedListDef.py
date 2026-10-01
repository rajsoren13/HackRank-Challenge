class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
a.next=b
current=a
while current is not None:
                print(current.data,end="->")
                current=current.next
print("None")