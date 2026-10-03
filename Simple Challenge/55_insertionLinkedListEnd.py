class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_middle(self, data, position):
        if position == 0:
            self.insert_at_front(data)
            return
        new_node = Node(data)
        prev = self.head
        for _ in range(position - 1):
            if prev is None:
                raise IndexError("Position out of bounds")
            prev = prev.next
        if prev is None:
            raise IndexError("Position out of bounds")
        new_node.next = prev.next
        prev.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.print_list()                 # 10-->20-->30-->None

ll.insert_at_front(5)
ll.print_list()                 # 5-->10-->20-->30-->None

ll.insert_at_middle(15, 2)
ll.print_list()                 # 5-->10-->15-->20-->30-->None

ll.insert_at_end(100)
ll.print_list()                 # 5-->10-->15-->20-->30-->100-->None