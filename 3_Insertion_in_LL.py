class Node:
    def __init__(self,data):
        self.__data=data
        self.next=None
    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head=None
    def print_elements(self):
        node=l1.head
        while(node!=None):
            print(node.get_data())
            node=node.next
    def Insert_First(self,data):
        new_node=Node(data)
        new_node.next=l1.head
        l1.head=new_node

    def Insert_end(self,data):
        new=Node(data)
        node=l1.head
        while(node.next!=None):
            node=node.next
        node.next=new
        new.next=None

    def Insert_Between(self,position,data):
        new2=Node(data)
        node=l1.head
        i=0
        while(i!=position-1):
            node=node.next
            i+=1
        new2.next=node.next
        node.next=new2  

l1=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

l1.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None

print(l1.print_elements())
l1.Insert_First(1)
print(l1.print_elements())
l1.Insert_end(100)
print(l1.print_elements())
l1.Insert_Between(3,66)
print(l1.print_elements())
