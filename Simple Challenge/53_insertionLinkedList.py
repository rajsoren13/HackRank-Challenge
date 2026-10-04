
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertion_at_front(self,data):
        c=Node(data)
        c.next=self.head
        self.head=c
    ## Insertion at middle
    def insertion_at_middle(self,data,position):
        if position==0:
            return self.insertion_at_front(data)
        new_node=Node(data)
        prev=self.head
        for a in range(position-1):
            if prev is None:
                raise IndexError("position out of bounds")
            prev=prev.next
        if prev is None:
            raise IndexError("position out of bounds")
        new_node.next=prev.next
        prev.next=new_node

    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next
        print("None")

ll=LinkedList()
ll.insertion_at_front(10)
ll.insertion_at_front(20)
#insert the value at front
ll.insertion_at_front(5)
ll.print_list()
#insert the value at middle
ll.insertion_at_middle(15, 2)          
ll.print_list()  

