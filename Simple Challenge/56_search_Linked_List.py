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

    def search_by_value(self,data):
        current=self.head
        position=0
        while current is not None:
            if current.data==data:
                return position
            current=current.next
            position=position+1
        return -1

     
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
searchvalue=100
valueposition=ll.search_by_value(searchvalue)
print(f"Value {searchvalue} is at the position:{valueposition} in a node")

