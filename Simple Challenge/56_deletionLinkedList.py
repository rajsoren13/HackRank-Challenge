class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertion_at_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insertion_at_middle(self,data,position):
        if position==0:
            return self.insertion_at_front(data)
        new_node=Node(data)
        prev=self.head
        for a in range(position-1):
            if prev is None:
                 raise IndexError("position out of bouds")
            prev=prev.next
        if prev is None:
            raise IndexError("position out of bounds")
        new_node.next=prev.next
        prev.next=new_node
    def insertion_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def deletion_by_value(self,data):
        current=self.head
        position=0
        while current is not None:
            if current.data==data:
                return self.deletion_at_position(position)
            current=current.next
            position=position+1
        raise ValueError(f"{data} not found in list")

    def deletion_at_position(self,position):
        if self.head is None:
            raise IndexError("List is empty")
        if position==0:
            self.head=self.head.next
            return
        prev=self.head
        
        for a in range(position-1):
            if prev is None:
                raise IndexError("position out of bound")
            prev=prev.next
        if prev is None or prev.next is None:
            raise IndexError("position out of bound")
        prev.next=prev.next.next

        
        

        
    
     
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next
        print("None")

    



        
ll=LinkedList()
ll.insertion_at_front(10)
ll.insertion_at_front(20)
ll.insertion_at_front(30)
ll.insertion_at_front(40)
ll.insertion_at_front(100)
ll.insertion_at_front(50)
ll.insertion_at_front(60)
ll.print_list()
ll.insertion_at_middle(15,1)
ll.insertion_at_end(25)
ll.print_list()
ll.deletion_at_position(1)
ll.print_list()
ll.deletion_by_value(100)
ll.print_list()

