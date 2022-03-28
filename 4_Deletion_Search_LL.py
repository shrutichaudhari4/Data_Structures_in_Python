class Node:
    def __init__(self,data):
        self.__data = data
        self.next = None
    
    def get_data(self):
        return self.__data

class LinkList:
    def __init__(self):
        self.head = None
    def print_ll(self):
        node = ll.head
        while node is not None:
            print(node.get_data())
            node = node.next
    def search(self,ele):
        node = ll.head
        while node is not None:
            if node.get_data() == ele:
                print(str(ele) + " element found")
                break
            elif node.get_data() is not ele and node.next is None:
                print("ele not found")
            node = node.next


    def del_by_value(self,del_node):
        if self.head is None:
            print("link list is empty...")
            return
        elif del_node == self.head:
            self.head = self.head.next
        else:
            node = self.head
            while node is not None:
                if del_node == node.next:
                    node.next = node.next.next
                else:
                    node = node.next

        

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

ll = LinkList()
ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
ll.print_ll()
ll.search(30)

ll.print_ll()
print("delete")
ll.del_by_value(n3)
print("after delete")
ll.print_ll()
