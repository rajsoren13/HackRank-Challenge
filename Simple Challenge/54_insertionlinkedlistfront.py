class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedListFront:
    def __init__(self):
        self.head=None


    def insertion_at_front(self,data):
         c=Node(data)
         c.next=self.head
         self.head=c
    def print_list(Self):
        current=Self.head
        while current is not None:
             print(current.data,end="-->")
             current=current.next
        print("None")
          
ll=LinkedListFront()
ll.insertion_at_front(10)
ll.insertion_at_front(20)
#Insert 5 at the front
ll.insertion_at_front(5)
ll.print_list()